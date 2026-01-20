import pandas as pd
import sqlite3
import logging
from config import RAW_DATA_PATH, CLEANED_DATA_DB_PATH, LOG_FILE_PATH

# Configure logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    handlers=[
                        logging.FileHandler(LOG_FILE_PATH),
                        logging.StreamHandler()
                    ])

def extract(file_path: str) -> pd.DataFrame | None:
    """
    Extracts data from a CSV file.

    Args:
        file_path (str): The path to the CSV file.

    Returns:
        pd.DataFrame: The extracted data as a pandas DataFrame, or None if an error occurs.
    """
    logging.info(f"Extracting data from {file_path}...")
    try:
        df = pd.read_csv(file_path)
        logging.info("Data extracted successfully.")
        logging.info(f"DataFrame shape: {df.shape}")
        return df
    except FileNotFoundError:
        logging.error(f"Error: The file {file_path} was not found.")
        return None
    except Exception as e:
        logging.error(f"An unexpected error occurred during data extraction: {e}")
        return None


def transform(df: pd.DataFrame) -> pd.DataFrame:
    """
    Transforms the raw data.

    Args:
        df (pd.DataFrame): The raw data as a pandas DataFrame.

    Returns:
        pd.DataFrame: The transformed data as a pandas DataFrame.
    """
    logging.info("Starting data transformation...")
    df = df.replace(["null", "#NAME?"], pd.NA)
    df = df.drop(columns=["Vehicle Images"])
    df = df.drop_duplicates(subset=["Booking_ID"])
    df["Booking_Value"] = pd.to_numeric(df["Booking_Value"], errors="coerce")
    df["Ride_Distance"] = pd.to_numeric(df["Ride_Distance"], errors="coerce")
    df["Driver_Ratings"] = pd.to_numeric(df["Driver_Ratings"], errors="coerce")
    df["Customer_Rating"] = pd.to_numeric(df["Customer_Rating"], errors="coerce")
    df["bookings_date_time"] = pd.to_datetime(
        df["Date"],
        dayfirst=True,
        infer_datetime_format=True,
        errors="coerce"
    )
    df = df.drop(columns=['Date', 'Time'])
    logging.info("Data transformation completed.")
    return df


def load(df: pd.DataFrame, db_path: str):
    """
    Loads the transformed data into a SQLite database.

    Args:
        df (pd.DataFrame): The transformed data as a pandas DataFrame.
        db_path (str): The path to the SQLite database file.
    """
    logging.info("Starting data load into SQLite...")
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS bookings (
                booking_id TEXT PRIMARY KEY,
                booking_status TEXT,
                customer_id TEXT,
                vehicle_type TEXT,
                pickup_location TEXT,
                drop_location TEXT,
                v_tat INTEGER,
                c_tat INTEGER,
                canceled_rides_by_customer TEXT,
                canceled_rides_by_driver TEXT,
                incomplete_rides TEXT,
                incomplete_rides_reason TEXT,
                booking_value REAL,
                payment_method TEXT,
                ride_distance REAL,
                driver_ratings REAL,
                customer_rating REAL,
                bookings_date_time TEXT
            )
        """)

        df.to_sql("bookings", conn, if_exists="replace", index=False)

        cursor.execute("SELECT COUNT(*) FROM bookings")
        count = cursor.fetchone()[0]
        logging.info(f"🧾 Rows inserted into DB: {count}")

        conn.commit()
        conn.close()
        logging.info("Data load completed successfully.")
    except sqlite3.Error as e:
        logging.error(f"An error occurred during the database operation: {e}")
    except Exception as e:
        logging.error(f"An unexpected error occurred during data loading: {e}")


def main():
    """
    Main function to run the ETL pipeline.
    """
    df = extract(RAW_DATA_PATH)
    if df is not None:
        df_transformed = transform(df)
        load(df_transformed, CLEANED_DATA_DB_PATH)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logging.critical(f"The ETL pipeline failed with an unexpected error: {e}")
import pandas as pd 
import sqlite3

def extract():
    df = pd.read_csv('data/raw/Bookings.csv')
    print("Data extracted successfully.")
    print(df.shape)
    return df

def transform(df):
    print("Starting data transformation...")
    df= df.replace(["null" , "#NAME?"],pd.NA)
    df = df.drop(columns=["Vehicle Images"])
    df = df.drop_duplicates(subset=["Booking_ID"])
    df["Booking_Value"] = pd.to_numeric(df["Booking_Value"], errors="coerce")
    df["Ride_Distance"] = pd.to_numeric(df["Ride_Distance"], errors="coerce")
    df["Driver_Ratings"] = pd.to_numeric(df["Driver_Ratings"], errors="coerce")
    df["Customer_Rating"] = pd.to_numeric(df["Customer_Rating"], errors="coerce")
    df["bookings_date_time"]= pd.to_datetime(
        df["Date"],
        dayfirst= True,
        infer_datetime_format= True,
        errors = "coerce"
    )
    df = df.drop(columns=['Date','Time'])
    return df

def load(df):
    print("Starting data load into SQLite...")
    
    # 1. Connect to DB (creates file if not exists)
    conn = sqlite3.connect("data/cleaned/bookings.db")
    cursor = conn.cursor()
    
    # 2. Create table (replace if exists)
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
    
    # 3. Insert DataFrame into table
    df.to_sql("bookings", conn, if_exists="replace", index=False)
    
    # 4. Verify row count
    cursor.execute("SELECT COUNT(*) FROM bookings")
    count = cursor.fetchone()[0]
    print(f"🧾 Rows inserted into DB: {count}")
    
    conn.commit()
    conn.close()
    print("Data load completed successfully.")

def main():
    df = extract()
    df = transform(df)
    load(df)
if __name__ == "__main__":
    main()
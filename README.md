# Python Data Cleaning and ETL Project

This project demonstrates a basic ETL (Extract, Transform, Load) pipeline for cleaning messy booking data. The script reads raw data from a CSV file, performs several cleaning and transformation steps, and then loads the clean data into a SQLite database.

## Features

*   **Extract:** Reads booking data from a CSV file.
*   **Transform:**
    *   Replaces placeholder values (`"null"`, `"#NAME?"`) with proper Not a Number (NaN) values.
    *   Removes unnecessary columns (`Vehicle Images`).
    *   Ensures data integrity by dropping duplicate bookings based on `Booking_ID`.
    *   Converts data types for several columns to numeric for easier analysis (e.g., `Booking_Value`, `Ride_Distance`).
    *   Parses and standardizes the date and time of bookings.
*   **Load:**
    *   Establishes a connection to a SQLite database.
    *   Creates a `bookings` table with a defined schema.
    *   Loads the cleaned DataFrame into the SQLite table, replacing it if it already exists.
*   **Logging:** Logs the ETL process to both the console and a file (`etl.log`).
*   **Configuration:** File paths are configurable via `config.py`.

## Project Structure

```
.
├── 1-raw-messy-data-cleaning
│   ├── etl.py                # The main ETL script
│   ├── config.py             # Configuration file for file paths
│   ├── requirements.txt      # Project dependencies
│   ├── etl.log               # Log file
│   └── data
│       ├── cleaned
│       │   └── bookings.db   # Output SQLite database
│       └── raw
│           └── Bookings.csv  # Raw input data
├── Tutorials
│   └── ...                   # Additional Python tutorial files
└── README.md
```

## Getting Started

Follow these instructions to set up and run the project on your local machine.

### Prerequisites

*   Python 3.x

### Installation & Usage

1.  **Clone the repository:**
    ```sh
    git clone https://github.com/sudhanshu808-in/python-data-eng.git
    cd python-data-eng
    ```

2.  **Install dependencies:**
    Install the required dependencies from the `requirements.txt` file.
    ```sh
    pip install -r 1-raw-messy-data-cleaning/requirements.txt
    ```

3.  **Configuration:**
    The file paths for the raw data, cleaned database, and log file can be configured in `1-raw-messy-data-cleaning/config.py`.

4.  **Run the ETL script:**
    Execute the script from the `1-raw-messy-data-cleaning` directory. It will process the raw data and create the cleaned database.
    ```sh
    cd 1-raw-messy-data-cleaning
    python etl.py
    ```

    After running, you can find the cleaned database at `data/cleaned/bookings.db` and the log file at `etl.log`.

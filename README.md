# Python Data Cleaning and ETL Project

This project demonstrates a basic ETL (Extract, Transform, Load) pipeline for cleaning messy booking data. The script reads raw data from a CSV file, performs several cleaning and transformation steps, and then loads the clean data into a SQLite database.

## Features

*   **Extract:** Reads booking data from `data/raw/Bookings.csv`.
*   **Transform:**
    *   Replaces placeholder values (`"null"`, `"#NAME?"`) with proper Not a Number (NaN) values.
    *   Removes unnecessary columns (`Vehicle Images`).
    *   Ensures data integrity by dropping duplicate bookings based on `Booking_ID`.
    *   Converts data types for several columns to numeric for easier analysis (e.g., `Booking_Value`, `Ride_Distance`).
    *   Parses and standardizes the date and time of bookings.
*   **Load:**
    *   Establishes a connection to a SQLite database at `data/cleaned/bookings.db`.
    *   Creates a `bookings` table with a defined schema.
    *   Loads the cleaned DataFrame into the SQLite table, replacing it if it already exists.

## Project Structure

```
.
├── 1-raw-messy-data-cleaning
│   ├── etl.py                # The main ETL script
│   ├── requirements.txt      # Project dependencies
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
    The main dependency for this project is `pandas`. You can install it using pip.
    ```sh
    pip install pandas
    ```
    *(It is recommended to update the `1-raw-messy-data-cleaning/requirements.txt` file with the project's dependencies.)*

3.  **Run the ETL script:**
    Execute the script from the root directory. It will process the raw data and create the cleaned database.
    ```sh
    python 1-raw-messy-data-cleaning/etl.py
    ```

    After running, you can find the cleaned database at `1-raw-messy-data-cleaning/data/cleaned/bookings.db`.

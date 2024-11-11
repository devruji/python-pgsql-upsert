# PostgreSQL Upsert with Python

This project provides a Python script that performs an upsert operation in PostgreSQL. Using the `ON CONFLICT` clause, this project demonstrates how to insert data into a PostgreSQL table and update existing rows when conflicts arise. The project includes code for creating a test table, generating mock data, and verifying data in the database.

## Prerequisites

- **Python** (version 3.6 or higher)
- **PostgreSQL** (version 9.5 or higher)
- **Python Libraries**: `psycopg2` for connecting to PostgreSQL

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/postgres-upsert-python.git
   cd postgres-upsert-python
   ```
2. Install the required library:
    ```bash
    pip install psycopg2
    ```

## Database Setup

1. Make sure you have PostgreSQL installed and running.
2. Create a new PostgreSQL database and user (if not already done):
    ```sql
    CREATE DATABASE your_database;
    CREATE USER your_username WITH PASSWORD 'your_password';
    GRANT ALL PRIVILEGES ON DATABASE your_database TO your_username;
    ```

## Configuration

Update the `db_config` dictionary in the Python script with your PostgreSQL database details:
```python
db_config = {
    'dbname': 'your_database',
    'user': 'your_username',
    'password': 'your_password',
    'host': 'localhost',  # or your PostgreSQL server
    'port': '5432'
}
```

## Running the Script

Run the script to create the table, generate mock data, and perform upserts:
```bash
python upsert_script.py
```
The script will:
- Create a test_table with columns id, name, and email.
- Generate 10 mock records.
- Perform upsert operations, inserting or updating records based on conflicts.
- Print the final contents of test_table to verify the data.
  
## Code Explanation

- **Table Creation**: Creates a test_table with id, name, and email columns. id is the primary key, and email is unique.
- **Mock Data Generation**: Generates random names and emails.
- **Upsert Operation**: Uses the ON CONFLICT clause to handle data conflicts, updating name and email if the id already exists.
- **Verification**: Fetches and prints all rows to confirm the upsert worked as expected.
  
## Sample Output

```bash
The output should look similar to the following:
Inserted or updated 10 records successfully.
(1, 'ExampleName1', 'examplename1@example.com')
(2, 'ExampleName2', 'examplename2@example.com')
...
```

## Author

Developed By @devruji
import psycopg2
import random
import string

# Database connection parameters
db_config = {
    "dbname": "poc",
    "user": "postgres",
    "host": "localhost",  # or your PostgreSQL server
    "port": "5432",
}

# Table name
tbl_name = "test_upsert"

# Establish a database connection
conn = psycopg2.connect(**db_config)
cursor = conn.cursor()

# Create a test table with the appropriate DDL
create_table_sql = f"""
CREATE TABLE IF NOT EXISTS {tbl_name} (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    email VARCHAR(50) UNIQUE
);
"""
cursor.execute(create_table_sql)
conn.commit()


# Generate mock data
def generate_mock_data(num_records):
    data = []
    for i in range(num_records):
        name = "".join(random.choices(string.ascii_letters, k=10))
        email = f"{name.lower()}@example.com"
        data.append((i + 1, name, email))
    return data


# Insert mock data with upsert logic
def insert_mock_data(data):
    sql = f"""
    INSERT INTO {tbl_name} (id, name, email)
    VALUES (%s, %s, %s)
    ON CONFLICT (id) DO UPDATE
    SET name = EXCLUDED.name,
        email = EXCLUDED.email;
    """
    try:
        for record in data:
            cursor.execute(sql, record)
        conn.commit()
        print(f"Inserted or updated {len(data)} records successfully.")
    except Exception as e:
        print("Error during data insertion:", e)
        conn.rollback()


# Generate and insert 10 mock records
mock_data = generate_mock_data(10)
insert_mock_data(mock_data)

# Fetch and display the data to verify
cursor.execute(f"SELECT * FROM {tbl_name};")
rows = cursor.fetchall()
for row in rows:
    print(row)

# Close the cursor and connection
cursor.close()
conn.close()

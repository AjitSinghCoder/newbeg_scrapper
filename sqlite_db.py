import sqlite3

def insert_product_data(db_name, data_dict):
    """
    Insert product data into SQLite database
    """
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    
    # Create table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            price REAL,
            description TEXT,
            brand TEXT,
            rating_count INTEGER,
            rating REAL,
            total_reviews INTEGER,
            customer_reviews TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Get columns and values directly from data_dict
    columns = list(data_dict.keys())
    values = list(data_dict.values())
    placeholders = ['?' for _ in columns]
    
    # Build and execute query
    query = f"INSERT INTO products ({', '.join(columns)}) VALUES ({', '.join(placeholders)})"
    cursor.execute(query, values)
    
    # Get the ID of inserted row
    inserted_id = cursor.lastrowid
    
    conn.commit()
    conn.close()
    
    print(f"Data inserted successfully! Row ID: {inserted_id}")
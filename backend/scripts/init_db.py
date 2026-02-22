
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import os
import sys

# Load env vars manually or just use the ones we know
DB_USER = "postgres"
DB_PASS = "postgres"
DB_HOST = "localhost"
DB_PORT = "5432"
TARGET_DB = "en_shirube_system"

def create_database():
    try:
        # Connect to default 'postgres' database
        print(f"Connecting to 'postgres' database at {DB_HOST}:{DB_PORT} as {DB_USER}...")
        conn = psycopg2.connect(
            dbname="postgres",
            user=DB_USER,
            password=DB_PASS,
            host=DB_HOST,
            port=DB_PORT
        )
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cur = conn.cursor()
        
        # Check if exists
        cur.execute(f"SELECT 1 FROM pg_database WHERE datname = '{TARGET_DB}'")
        exists = cur.fetchone()
        
        if not exists:
            print(f"Creating database '{TARGET_DB}'...")
            cur.execute(f"CREATE DATABASE {TARGET_DB}")
            print("Database created successfully.")
        else:
            print(f"Database '{TARGET_DB}' already exists.")
            
        cur.close()
        conn.close()
        return True
        
    except Exception as e:
        print(f"Error creating database: {e}")
        return False

if __name__ == "__main__":
    success = create_database()
    if not success:
        sys.exit(1)

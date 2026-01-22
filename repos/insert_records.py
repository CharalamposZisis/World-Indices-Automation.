from api_request import fetch_data
import psycopg2
import time

# function to create the db inside container
def connect_to_db():
    print("Connecting to the PostgreSQL database...")
    try:
        conn = psycopg2.connect(
            host = "localhost",
            port = 5000,
            dbname = "db",
            user = "Mpampis",
            password = "db_password"
        )
        print("Connected successfully")
        return conn
    except psycopg2.Error as e:
            print(f"Database connection failed: {e}")

# function to create table for the db
def create_table(conn):
    print("create table if not exitst")
    try:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS stock_prices (
                symbol TEXT NOT NULL,
                date DATE NOT NULL,
                open NUMERIC,
                high NUMERIC,
                low NUMERIC,
                close NUMERIC,
                volume BIGINT,
                PRIMARY KEY (symbol, date)
            );
        """)
        conn.commit()
        print('Table was created')
    except psycopg2.Error as e:
        print(f"Failed to create table: {e}")
        raise e 
    
# conn = connect_to_db()
# create_table(conn)

def insert_record(conn, data):
    print("Inserting stock data into the database...")
    cursor = conn.cursor()
    
    for stock in data:
        cursor.execute("""
            INSERT INTO PUBLIC.stock_prices(
                symbol,
                date,
                open,
                high,
                low,
                close,
                volume
            ) VALUES (%s, %s, %s, %s, %s, %s, %s);
        """,(
            stock["ticker"],
            stock["last_trade_time"][:10],  # YYYY-MM-DD
            stock.get("day_open"),
            stock.get("day_high"),
            stock.get("day_low"),
            stock.get("price"),
            stock.get("volume")
        ))
    conn.commit()
    print("Data successfull inserted")
          
   
# Main script
def main():
    conn = connect_to_db()
    if not conn:
        return

    create_table(conn)

    stocks = ["AAPL", "MSFT", "GOOGL"]
    stock_data = fetch_data(stocks)

        # # Handle API rate limits
        # if "Note" in data:
        #     print(f"Rate limit reached, waiting 60 seconds...")
        #     time.sleep(60)
        #     data = fetch_data(stock)

    insert_record(conn, stock_data)
    time.sleep(15)  # Avoid hitting rate limit

    conn.close()
    print("DB connection closed")

if __name__ == "__main__":
    main()   
   

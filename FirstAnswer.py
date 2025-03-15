import pandas as pd
from sqlalchemy import create_engine

def load_orders(file_path):
    # Load CSV data into DataFrame
    df = pd.read_csv(file_path)

    # Create connection using SQLAlchemy
    engine = create_engine('mysql+mysqlconnector://root:root@localhost:3306/rutuja')

    # Insert data into the table (ignore duplicates using 'if_exists="append"')
    df.to_sql('orders', con=engine, if_exists='append', index=False, method='multi')

    print("Orders loaded successfully!")

# Example usage:
file_path = r"D:\pandas data\orders_file.csv"
load_orders(file_path)


import pandas as pd
from sqlalchemy import create_engine

def update_orders_and_export():
    # Connect to MySQL using SQLAlchemy
    engine = create_engine('mysql+mysqlconnector://root:root@localhost:3306/rutuja')

    # Update orders table with location details from ip_data
    with engine.connect() as connection:
        update_query = '''
            UPDATE orders o
            JOIN ip_data i ON o.ip_address = i.ip_address
            SET o.city = i.city, o.state = i.state, o.zip_code = i.zip_code
        '''
        connection.execute(update_query)

    # Export updated orders to CSV file
    export_query = '''
        SELECT order_number, city, state, zip_code 
        FROM orders 
        WHERE city IS NOT NULL
    '''
    df = pd.read_sql(export_query, con=engine)
    df.to_csv(r'D:\pandas data\updated_orders.csv', index=False)

    print("Orders updated and exported successfully!")

# Example usage:
update_orders_and_export()

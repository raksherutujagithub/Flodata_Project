import pandas as pd
from sqlalchemy import create_engine
import requests

# Function to get location from IP
def get_location_from_ip(ip):
    url = f"https://ipapi.co/{ip}/json/"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data.get('city'), data.get('region'), data.get('postal')
    return None, None, None

def load_ip_addresses(file_path):
    # Load CSV data into DataFrame
    df = pd.read_csv(file_path)

    # Connect to MySQL using SQLAlchemy
    engine = create_engine('mysql+mysqlconnector://root:root@localhost:3306/rutuja')

    # Read existing IPs to avoid duplicate processing
    existing_ips = pd.read_sql("SELECT ip_address FROM ip_data", con=engine)
    existing_ips_set = set(existing_ips['ip_address'])

    new_data = []
    for ip in df['ip_address']:
        if ip not in existing_ips_set:
            city, state, zip_code = get_location_from_ip(ip)
            if zip_code:
                new_data.append((ip, city, state, zip_code))

    # Insert new data into table
    if new_data:
        new_df = pd.DataFrame(new_data, columns=['ip_address', 'city', 'state', 'zip_code'])
        new_df.to_sql('ip_data', con=engine, if_exists='append', index=False)

    print("IP addresses processed successfully!")

# Example usage:
file_path = r'D:\pandas data\ip_addresses.csv'
load_ip_addresses(file_path)

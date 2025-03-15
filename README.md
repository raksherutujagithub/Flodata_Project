
1)First Script (load_orders):
Reads data from a CSV file (orders_file.csv) into a DataFrame.
Connects to a MySQL database using SQLAlchemy.
Loads data into the orders table, ignoring duplicates using if_exists='append'.
Prints a success message after loading data.
Second Script (load_ip_addresses)

2)Reads IP addresses from a CSV file (ip_address.csv):
Connects to a MySQL database using SQLAlchemy.
Fetches existing IP addresses from the ip_data table to avoid duplicates.
Uses an API (ipapi.co) to get the city, state, and postal code for each new IP address.
Inserts new data into the ip_data table.
Prints a success message after loading data.
Third Script (update_orders_and_export)

3)Connects to a MySQL database using SQLAlchemy:
Updates the orders table with location details from the ip_data table based on the ip_address column.
Exports the updated data to a CSV file (updated_orders.csv).
Prints a success message after updating and exporting data.

4)Fourth and Fifth Scripts (load_ip_addresses):
Similar to the second script.
Reads IP addresses from a CSV file.
Connects to a MySQL database.
Fetches existing IP addresses to avoid duplicates.
Uses an API to get location details for new IP addresses.
Inserts new data into the ip_data table.
Prints a success message after processing data.
The script avoids duplicate processing by checking existing IPs using a set for fast lookup (O(1)). It minimizes API calls by only processing new IPs and inserts data in batches using to_sql() for better performance. SQLAlchemy efficiently handles database connections and operations.


part-2 

1)First Python Script:
Loads sales data from an Excel file.
Filters data based on state and year.
Aggregates total sales by state, city, and quarter.
Saves the report to an Excel file.

2)Second Python Script:
Creates a sales table and inserts sample data.
Updates sales data for a specific order.
Retrieves data using a SQL query and processes it using pandas.
Aggregates sales data by city and quarter.
Saves the report to a CSV file.

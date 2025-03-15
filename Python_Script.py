import pandas as pd


def generate_quarterly_sales_report(file_path, state, year, output_file):
    """
    Generates a quarterly sales report for a given state and year.

    Parameters:
    file_path (str): Path to the input Excel file.
    state (str): State to filter data.
    year (int): Year to filter data.
    output_file (str): Path to save the output Excel file.
    """

    # Load data
    df = pd.read_excel(file_path)

    # Ensure necessary columns exist
    required_columns = {"State", "City", "Order Date", "Sales"}
    if not required_columns.issubset(df.columns):
        raise ValueError("Missing required columns in input file")

    # Convert 'Order Date' to datetime
    df["Order Date"] = pd.to_datetime(df["Order Date"], errors='coerce')
    df.dropna(subset=["Order Date", "City"], inplace=True)  # Ignore missing dates or cities

    # Extract year and quarter
    df["Year"] = df["Order Date"].dt.year
    df["Quarter"] = df["Order Date"].dt.quarter

    # Filter data by state and year
    df_filtered = df[(df["State"] == state) & (df["Year"] == year)]

    # Aggregate sales by state, city, and quarter
    sales_summary = df_filtered.groupby(["State", "City", "Quarter"]).agg({"Sales": "sum"}).reset_index()

    # Save to an Excel file
    sales_summary.to_excel(output_file, index=False)
    print(f"Quarterly sales report saved to: {output_file}")


# Example usage
file_path = r"D:\pandas data\IL_state_sales_report_2021.xlsx"
output_path = r"D:\pandas data\Quarterly_Sales_Report_IL_2021.xlsx"
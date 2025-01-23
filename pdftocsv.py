from tabula import read_pdf
import pandas as pd

# File paths
pdf_path = "path to pdf"
output_excel = "output.xlsx"

try:
    # Read all tables from the PDF
    tables = read_pdf(pdf_path, pages="all", multiple_tables=True, pandas_options={"header": None})
    
    # Combine all tables into one DataFrame
    combined_data = pd.concat(tables, ignore_index=True)

    # Write the combined DataFrame to a single Excel sheet
    combined_data.to_excel(output_excel, index=False, engine="openpyxl")

    print(f"Excel file '{output_excel}' has been created successfully with all pages combined.")
except Exception as e:
    print(f"An error occurred: {e}")


"""
convert_to_parquet.py
---------------
Converts excel data to parquet format.
"""

import pandas as pd
import logging

logging.basicConfig(level=logging.INFO)


class ParquetConverter:
    def __init__(self, excel_file: str, parquet_file: str):
        self.excel_path = f"data/{excel_file}"
        self.parquet_path = f"data/{parquet_file}"

    def convert(self):
        df = pd.read_excel(self.excel_path)
        df.to_parquet(self.parquet_path, engine="pyarrow", index=False)
        logging.info(f"Parquet file saved: {self.parquet_path}")

def main():
    ParquetConverter("employee_data.xlsx", "employee_data.parquet").convert()

if __name__ == "__main__":
    main()

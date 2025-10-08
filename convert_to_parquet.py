import pandas as pd
import logging

logging.basicConfig(level=logging.INFO)


class ParquetConverter:
    def __init__(self, excel_file: str, parquet_file: str):
        self.excel_file = excel_file
        self.parquet_file = parquet_file

    def convert(self):
        df = pd.read_excel(self.excel_file)
        df.to_parquet(self.parquet_file, engine="pyarrow", index=False)
        logging.info(f"Parquet file saved: {self.parquet_file}")

def main():
    ParquetConverter("employee_data.xlsx", "employee_data.parquet").convert()

if __name__ == "__main__":
    main()

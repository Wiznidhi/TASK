import random
from datetime import datetime, timedelta

import pandas as pd
from faker import Faker
import logging

logging.basicConfig(level=logging.INFO)

fake = Faker()


class DataGenerator:
    def __init__(self, num_rows=1_000_000):
        self.num_rows = num_rows

    def generate_data(self) -> pd.DataFrame:
        emp_ids = [f"ZMX{i+1}" for i in range(self.num_rows)]
        names = [fake.name() for _ in range(self.num_rows)]
        salaries = [round(random.uniform(20000, 200000), 2) for _ in range(self.num_rows)]
        start_date = datetime(2020, 1, 1)
        salary_dates = [
            start_date + timedelta(days=random.randint(0, (datetime.today() - start_date).days))
            for _ in range(self.num_rows)
        ]
        df = pd.DataFrame({
            "empid": emp_ids,
            "name": names,
            "salary": salaries,
            "salary_date": salary_dates
        })
        return df


class ExcelHandler:
    def __init__(self, dataframe: pd.DataFrame):
        self.dataframe = dataframe

    def save(self, file_name="employee_data.xlsx") -> None:
        self.dataframe.to_excel(file_name, index=False)
        logging.info(f"Excel file saved: {file_name}")


def main():
    df = DataGenerator().generate_data()
    ExcelHandler(df).save()


if __name__ == "__main__":
    main()

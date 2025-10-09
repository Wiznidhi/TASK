import random
from datetime import datetime, timedelta

import pandas as pd
from faker import Faker
import logging

logging.basicConfig(level=logging.INFO)

fake = Faker("en_IN")

class DataGenerator:

    def __init__(self, num_rows=1_000_000):
        self.num_rows = num_rows

    def generate_id(self) -> list[str]:
        emp_ids = [f"ZMX{i+1}" for i in range(self.num_rows)]
        return emp_ids

    def generate_name(self) -> list[str]:
        names = [fake.name() for _ in range(self.num_rows)]
        return names

    def generate_salary(self) -> list[str]:
        salaries = [round(random.uniform(20000, 200000), 2) for _ in range(self.num_rows)]
        return salaries

    def generate_date(self) -> list[str]:
        start_date = datetime(2020, 1, 1)

        salary_dates = [
            (start_date + timedelta(days=random.randint(0, (datetime.today() - start_date).days))).strftime("%Y-%m-%d") for _ in range(self.num_rows)
        ]
        return salary_dates

    def generate_data(self) -> pd.DataFrame:

        df = pd.DataFrame({
            "empid": self.generate_id(),
            "name": self.generate_name(),
            "salary": self.generate_salary(),
            "salary_date": self.generate_date()
        })
        return df


class ExcelHandler:
    def __init__(self, dataframe: pd.DataFrame):
        self.dataframe = dataframe

    def save(self, file_path="data/employee_data.xlsx") -> None:
        self.dataframe.to_excel(file_path, index=False)
        logging.info(f"Excel file saved: {file_path}")


def main():
    df = DataGenerator().generate_data()
    ExcelHandler(df).save()


if __name__ == "__main__":
    main()

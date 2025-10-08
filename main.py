import generate_data
import convert_to_parquet
import upload_to_S3
import logging

logging.basicConfig(level=logging.INFO)


def main():
    logging.info("Step 1: Generating Excel Data")
    generate_data.main()

    logging.info("Step 2: Converting Excel to Parquet")
    convert_to_parquet.main()

    logging.info("Step 3: Uploading Parquet to AWS S3 bucket")
    upload_to_S3.main()

    logging.info("Pipeline Executed")

if __name__=="__main__":
    main()
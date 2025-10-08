import os
import logging
import boto3
from datetime import datetime
from botocore.exceptions import NoCredentialsError, ClientError

logging.basicConfig(level=logging.INFO)

class S3Uploader:
    def __init__(self, bucket_name: str):
        self.bucket_name = bucket_name
        self.s3_client = boto3.client("s3")

    def upload(self, file_name: str, s3_key: str):

        try:
            self.s3_client.upload_file(file_name, self.bucket_name, s3_key)
            logging.info(f"Uploaded to S3: s3://{self.bucket_name}/{s3_key}")

        except FileNotFoundError:
            logging.error(f"File not found: {file_name}")
        except NoCredentialsError:
            logging.error("AWS credentials not found")
        except ClientError as e:
            logging.error(f"Upload failed: {e}")

def main():
    bucket = "zmx-training-bucketbatch2025"  
    folder = f"Nidhi/{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}"
    file_name = "employee_data.parquet"

    upload_path = f"{folder}/{file_name}"
    S3Uploader(bucket).upload(file_name, upload_path)

if __name__ == "__main__":
    main()

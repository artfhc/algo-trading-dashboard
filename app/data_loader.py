import boto3
import os
import pandas as pd
from io import BytesIO

def load_latest_data():
    try:
        s3 = boto3.client(
            "s3",
            aws_access_key_id=os.environ["AWS_KEY"],
            aws_secret_access_key=os.environ["AWS_SECRET"]
        )
        response = s3.get_object(Bucket=os.environ["S3_BUCKET"], Key="latest.parquet")
        return pd.read_parquet(BytesIO(response['Body'].read()))
    except Exception as e:
        return None

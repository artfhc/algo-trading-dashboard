import os
import boto3
import pandas as pd

def fetch_strategies():
    # TODO: Implement actual Composer API pagination
    return pd.DataFrame({
        'date': pd.date_range(start='2024-01-01', periods=10),
        'PnL': range(10)
    })

def upload_to_s3(df):
    df.to_parquet("latest.parquet", index=False)
    s3 = boto3.client(
        "s3",
        aws_access_key_id=os.environ["AWS_KEY"],
        aws_secret_access_key=os.environ["AWS_SECRET"]
    )
    s3.upload_file("latest.parquet", os.environ["S3_BUCKET"], "latest.parquet")

if __name__ == "__main__":
    df = fetch_strategies()
    upload_to_s3(df)

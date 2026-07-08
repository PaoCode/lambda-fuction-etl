import boto3 

s3 = boto3.client("s3")
bucket = "xideralaws-curso-paoesquivel2026-020635523025-us-west-1-an"
key = "titanic_clean_data.csv"


def create_new_data(data_clean):
    s3.put_object(
        Bucket=bucket,
        Key=key,
        Body=data_clean,
        ContentType="text/csv"
    )
    return 200
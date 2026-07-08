import boto3 

s3 = boto3.client("s3")
bucket = "xideralaws-curso-paoesquivel2026-020635523025-us-west-1-an"
key = "titanic_clean_data.csv" #hola.txt


def create_new_data(data):
    s3.put_object(
        Bucket=bucket,
        Key=key,
        Body=data,
        ContentType="text/csv" # ext/plain
    )
    return 200
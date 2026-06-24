import boto3   # AWS SDK — intentionally NOT declared as a dependency

def make_s3_client():
    return boto3.client("s3")

import boto3
from botocore.exceptions import NoCredentialsError

BUCKET_NAME = "cloudnotes-storage-abhilash"

s3 = boto3.client("s3")


def upload_file_to_s3(file_obj, filename, content_type):
    try:
        s3.upload_fileobj(
            file_obj,
            BUCKET_NAME,
            filename,
            ExtraArgs={"ContentType": content_type}
        )

        file_url = f"https://{BUCKET_NAME}.s3.amazonaws.com/{filename}"
        return file_url

    except NoCredentialsError:
        return None


def delete_file_from_s3(file_url: str):
    try:
        key = file_url.split(".amazonaws.com/")[1]
        s3.delete_object(Bucket=BUCKET_NAME, Key=key)
    except Exception as e:
        print("S3 delete error:", e)

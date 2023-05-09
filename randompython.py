import boto3
import random
import string
# Generate a random string
def random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))
# Set up S3 client
s3 = boto3.client('s3')
# Generate random string
my_string = random_string(10)
# Upload string to S3 bucket
bucket_name = 'sgreen515-s3-demo'
object_name = 'random-string.txt'
s3.put_object(Body=my_string, Bucket=bucket_name, Key=object_name)
print(f"Random string '{my_string}' uploaded to S3 bucket '{bucket_name}' as '{object_name}'.")
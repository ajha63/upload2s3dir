import os
import sys
import boto3
import logging

# get an access token, local (from) directory, and S3 (to) directory
# from the command-line
local_directory, bucket, destination = sys.argv[1:4]

LOG_FILE = '/var/log/upload2s3dir.log'
logging.basicConfig(filename=LOG_FILE, filemode='w', level=logging.INFO)

client = boto3.client('s3')

# get local files recursively
for root, dirs, files in os.walk(local_directory):

  for filename in files:

    # construct the full local path
    local_path = os.path.join(root, filename)

    relative_path = os.path.relpath(local_path, local_directory)
    s3_path = os.path.join(destination, relative_path)


    logging.info("Searching {:s} in {:s}".format(s3_path, bucket))
    try:
        client.head_object(Bucket=bucket, Key=s3_path)
        logging.info("Path found on S3! Skipping {:s}...".format(s3_path))

    except:
        client.upload_file(local_path, bucket, s3_path)
        logging.info("Uploading {:s}...".format(s3_path))

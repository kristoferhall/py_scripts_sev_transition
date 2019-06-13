#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 15:32:32 2019

@author: kris

Test snippet to:
    1. create S3 bucket
    2. create recursive listing of files in directory to upload
    3. recursively upload files/objects to bucket
"""

import boto3
import os
import logging
from botocore.exceptions import ClientError


os.getcwd()
os.chdir('/users/kris/Desktop/')

client = boto3.client('s3')


# create s3 bucket
response = client.create_bucket(
        Bucket='sev-kmh-test-bucket',
        CreateBucketConfiguration={
                'LocationConstraint': 'us-east-2'
                }
        )

print(response)


# get listing of files in directory and subdirectory to upload
fname = []

for root, dirs, files in os.walk('aws_test_dir'):
    for f in files:
        if '.DS_Store' in f:
            continue
        else:
            fname.append(os.path.join(root, f))


for root, dirs, files in os.walk('aws_test_dir'):
    print(root)
    print(dirs)
    print(files)

            
    
print(fname)    


# recursively upload files in fname to bucket
for file in fname:
    client.upload_file(file, 'sev-kmh-test-bucket', file)
    

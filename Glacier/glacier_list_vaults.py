"""
Script lists vaults in Glacier
"""


import boto3


glacier = boto3.client('glacier')

response = glacier.list_vaults(
        accountId='-'
)

print(response)



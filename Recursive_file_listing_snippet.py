"""
KM Hall
20190610

Testing recursively running through files in a list to see whether is is possible
to recursively upload them to S3 via boto3

using the ~/Desktop/aws_test_dir for testing.
Note, this was produced on a Mac and contains .DS_Store files.
We will want to ignore these - see VERSION 2
"""

import os


# VERSION 1 - also captures .DS_Store files

# initialize a list to hold file names
fname = []

for root, dirs, files in os.walk('/users/kris/Desktop/aws_test_dir'):
   for f in files:
       fname.append(os.path.join(root, f))
       
print("fname = %s" %fname)

for n in fname:
     print(n)
     

# VERSION 2 - exlcude .DS_Store files

# reinitialize fname
fname = []

for root, dirs, files in os.walk('/users/kris/Desktop/aws_test_dir'):
    for f in files:
        if '.DS_Store' in f:
            continue
        else:
            fname.append(os.path.join(root, f))
            
for n in fname:
    print(n)
    
    

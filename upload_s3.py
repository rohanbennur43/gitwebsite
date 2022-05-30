import os
import boto3
s3=boto3.resource(service_name='s3',region_name='ap-south-1',aws_access_key_id='AKIAYPEAHG4RYFYBIJ53',aws_secret_access_key='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')


dir='channel_281/priority'
files=os.listdir(dir)

arr=[]
dict={}
for file in files:
    split_files=file.split('_')
    #print(split_files[4])
    dict[int(split_files[4][2:])]=file
    arr.append(int(split_files[4][2:]))
arr.sort()


for i in arr:
  s3.Bucket('amagibucket').upload_file(Filename=os.path.join(dir,dict[i]),Key=dict[i])
  print('uploaded',i)
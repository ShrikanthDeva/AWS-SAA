import boto3
import argparse


# Client: low-level service access
# Resource: higher-level object-oriented service access

s3_client = boto3.client('s3')
s3_resource = boto3.resource('s3')

# Create S3-bucket
def s3_create(namespace):
    session = boto3.session.Session()
    current_region = session.region_name
    try:
        bucket_response = s3_resource.meta.client.create_bucket(Bucket=namespace.bucket)
    except:
        return "Bucket name is not unique !"
    return "Bucket -> "+ namespace.bucket + " was successfully created in -> " + current_region + " region."

# To specify bucket's location use :
#   bucket_response = s3_connection.create_bucket(
#                   Bucket=bucket_name,
#                   CreateBucketConfiguration={'LocationConstraint': current_region} )


# Upload's the given object into s3 bucket
def put_obj(namespace):
    s3_client.upload_file( Filename=namespace.file, Bucket=namespace.bucket,Key=namespace.file )
    return "Successfully uploaded -> " + namespace.file + " on -> " + namespace.bucket

# Download's the given object from s3 bucket
def get_obj(namespace):
    s3_client.download_file( Key=namespace.object, Bucket=namespace.bucket,Filename=namespace.file )
    return "Successfully downloaded -> " + namespace.object + " from -> " + namespace.bucket + " as " + namespace.file

# Delete's the given object from s3 bucket
def del_obj(namespace):
    # s3_client.delete_objects( Bucket=namespace.bucket, Key=namespace.object )
    s3_resource.Object(namespace.bucket, namespace.object).delete()
    return "Successfully deleted -> " + namespace.object + " from -> " + namespace.bucket

# Empty the given s3 bucket
def del_all(namespace):
    s3_bucket = s3_resource.Bucket(namespace.bucket)    
    s3_bucket.objects.all().delete()        
    return "Bucket -> " + namespace.bucket + ' emptied !'

# Lists the object from s3 bucket
def list_obj(namespace):
    objects = s3_client.list_objects( Bucket = namespace.bucket )
    if 'Contents' not in objects:
        print("Bucket -> ",namespace.bucket,'is empty !')
    else :
        for i in objects['Contents']:
            print(i['Key'])   


# creating argument parser object
parser = argparse.ArgumentParser(description='Description: AWS S3 CLI')
subparsers = parser.add_subparsers(help='sub-command help')

# create
mk = subparsers.add_parser('mk', help="Creates a S3 Bucket")
mk.add_argument('--bucket', help="bucket name", required=True)
mk.set_defaults(func=s3_create)

# list-objects
ls = subparsers.add_parser('ls', help='List all objects in S3 Bucket')
ls.add_argument('--bucket', help='bucket name', required=True)
ls.set_defaults(func=list_obj)

# upload
put = subparsers.add_parser('put', help='Upload a file to S3 Bucket')
put.add_argument('--bucket', help="bucket name", required=True)
put.add_argument('--file', help="file to be uploaded", required=True)
put.set_defaults(func=put_obj)

# download
get = subparsers.add_parser('get', help='Download an object from S3 Bucket')
get.add_argument('--bucket', help="bucket name", required=True)
get.add_argument('--object', help="key of the object", required=True)
get.add_argument('--file', help="file to be saved as", required=True)
get.set_defaults(func=get_obj)

# delete
rm = subparsers.add_parser('rm', help="Delete an object from S3 Bucket")
rm.add_argument('--bucket', help="bucket name", required=True)
rm.add_argument('--object', help="key of the object", required=True)
rm.set_defaults(func=del_obj)

# delete all
Del = subparsers.add_parser('clear', help="Delete's all objects in S3 Bucket")
Del.add_argument('--bucket', help="bucket name", required=True)
Del.set_defaults(func=del_all)

# parsing arguments to args
args = parser.parse_args()

try:
    response = args.func(args)
    if response: 
        print(response)
except Exception as Error:
    print("Error :", Error)

# USE:
# python3 python-s3.py mk --bucket=shri2-demo-bucket
# python3 python-s3.py ls --bucket=shri2-demo-bucket
# python3 python-s3.py put --bucket=shri2-demo-bucket --file=obj_from_cli.txt
# python3 python-s3.py get --bucket=shri2-demo-bucket --file=obj_from_aws.txt --object=obj_from_cli
# python3 python-s3.py rm --bucket=shri2-demo-bucket --object=obj_from_cli.txt
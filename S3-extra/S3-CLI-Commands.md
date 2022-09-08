# AWS - CLI - Commands -  S3
+ **Setup profile** - `aws configure`
  + Give access key & secret access key 

+ **View buckets of profile** : `aws s3 ls`
+ **View objects in S3 bucket** : `aws s3 ls s3://<bucket-name>`
+ **Put-object** :   
    1) `aws s3api put-object --bucket <bucket-name> --key <obj-name>  --body <path-of-file>  --content-type <obj-type>`
	+ **Eg** :  aws s3api put-object --bucket shri-demo-bucket --key pic1.png  --body pic1.png --content-type 'image/png'

   2) `aws s3 cp <file-name> s3://<bucket-name>`
    + **Eg** :  aws s3 cp iPadfromcli.png s3://shri-demo-bucket

+ **Get-object** :   
    1) `aws s3api get-object --bucket <bucket-name> --key <obj-name>  <outfile-name>`
	+ **Eg** :  aws s3api get-object --bucket shri-demo-bucket --key iPad.png  iPadfromcli.png

    2) `aws s3 cp s3://<bucket-name> <file-name> `
    + **Eg** :  aws s3 cp s3://shri-demo-bucket iPadfromcli.png



+ **Delete-object** :   
    1) `aws s3api delete-object --bucket <bucket-name> --key <obj-name>`
	+ **Eg** :  aws s3api delete-object --bucket shri-demo-bucket --key pic1.png

    2) `aws s3 rm s3://<bucket-name + file-location>`
    + **Eg** :  aws s3 rm s3://shri-demo-bucket/iPadfromcli.png 


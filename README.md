# Flask Uploader 

This is a small proof of concept getting the [jQuery File Uploader][1] plugin to work with a Flask Backend. By default, this project supports multiple file uploads
for Chrome and Firefox, IE can only do one file at a time. The backend then uploads the file(s) to an S3 bucket of your choosing.


## Installing
Start a virtualenv: virtualenv .

Activate it: source bin/activate

Install the pip requirements: pip install -r requirements.txt

Change api/main.py to reflect your AWS Security Credentials. Also change the value of `bucket_name` in the upload and download handlers

Run the Flask server: python manage.py runserver

## Usage
In your browser, visit http://localhost:5002/, and upload.

You will receive a JSON response with a key to the URL of the upload on S3.

You can download your file by visiting http://localhost:5002/download/<key> (i.e. http://localhost:5002/download/abc123/test.zip).

The download will give you a temporary access key for downloading the file off S3, which expires after 60 seconds.

[1]: http://blueimp.github.com/jQuery-File-Upload/

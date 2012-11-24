import json, re, boto, StringIO, random

from functools import wraps
from flask import Blueprint, request, abort, jsonify, redirect, render_template

main_api = Blueprint('main_api', __name__)
s3conn = boto.connect_s3('access_key', 'secret')

def _handleUpload(files):
    if not files:
        return None

    bucket_name = "bucket_name"
    s3bucket = s3conn.get_bucket(bucket_name, validate=False)
    filenames = []
    
    myhash = random.getrandbits(128)
    hash_str = "%032x" % myhash
    for upload_file in files.getlist('files[]'):
        output = StringIO.StringIO()
        output.write(upload_file.stream.read())
        k = s3bucket.new_key("%s/%s" % (hash_str, upload_file.filename))
        k.set_contents_from_string(output.getvalue())

        filenames.append("%s/%s" % (hash_str, upload_file.filename))

    return filenames

def _handleDownload(hashstr, filename):
    bucket_name = "bucket_name"
    return s3conn.generate_url(60, 'GET', bucket=bucket_name, key='%s/%s' % (hashstr, filename), force_http=True)


@main_api.route('/upload/', methods=['POST'])
def upload():
    try:
        message = request.values['message']
        files = request.files
        print message, files
        
        uploaded_files = _handleUpload(files)

        return jsonify({'files': uploaded_files})
    except:
        raise
        return jsonify({'status': 'error'})

@main_api.route('/download/<hashstr>/<filename>', methods=['GET'])
def download(hashstr, filename):
    try:
        return redirect(_handleDownload(hashstr, filename))
    except:
        return jsonify({'status': 'error'})

@main_api.route('/', methods=['GET'])
def index():
    return render_template('index.html')

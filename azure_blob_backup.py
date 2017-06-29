from azure.storage.blob import BlockBlobService
from azure.storage.blob import ContentSettings
import datetime
import subprocess

NAME = ''
KEY = ''
bbs = BlockBlobService(account_name=NAME, account_key=KEY)
bbs.create_container('webdbbck')

subprocess.call('rm -rf minibezos' ,shell=True)
subprocess.call('mongodump -u usrname -p password -d minibezos -h hostname -o /root' , shell=True)

filename = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M") + '-webdb.tar.gz'
print(filename)
subprocess.call('tar -zcvf ' + filename + ' minibezos',shell=True)

bbs.create_blob_from_path(
        'webdbbck',
        filename,
        filename,
        content_settings=ContentSettings(content_type='application/tar+gzip')
        )

subprocess.call('rm -f ' + filename ,shell=True)
subprocess.call('rm -rf minibezos' ,shell=True)

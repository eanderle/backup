import dropbox
import json
import os
from datetime import datetime

def do_oauth():
    client_secrets = json.load(open('client_secrets.json'))
    app_key = client_secrets['app_key']
    app_secret = client_secrets['secret']

    flow = dropbox.client.DropboxOAuth2FlowNoRedirect(app_key, app_secret)

    # Have the user sign in and authorize this token
    authorize_url = flow.start()
    print '1. Go to: ' + authorize_url
    print '2. Click "Allow" (you might have to log in first)'
    print '3. Copy the authorization code.'
    code = raw_input("Enter the authorization code here: ").strip()

    # This will fail if the user enters an invalid authorization code
    access_token, user_id = flow.finish(code)

    token_file = open('token', 'w')
    token_file.write(access_token)
    token_file.close()

    return access_token

def read_token():
    token_file = open('token', 'r')
    access_token = token_file.readline()
    token_file.close()
    return access_token

def get_datetime(xml_file):
    # Sun, 09 Mar 2014 09:04:54 +0000
    return datetime.strptime(xml_file['modified'][:-6], '%a, %d %b %Y %H:%M:%S')

def get_most_recent(client):
    metadata = client.metadata('/Apps/SMSBackupRestore/')
    xml_files = [x for x in metadata['contents'] if (x['mime_type'] == 'application/xml')]
    return max(xml_files, key=get_datetime)

def save_file(client, path):
    f = open(os.path.expanduser('~/backup/sms/{}'.format(os.path.basename(path))), 'w')
    f.write(client.get_file(path).read())
    f.close()

access_token = read_token() if os.path.isfile('token') else do_oauth()
client = dropbox.client.DropboxClient(access_token)

print 'Finding most recent sms backup...'
most_recent = get_most_recent(client)

path = most_recent['path']
basename = os.path.basename(path)
print 'Found {}.'.format(basename)

print 'Saving into ~/backup/sms/{}...'.format(basename)
save_file(client, path)
print 'Done!'

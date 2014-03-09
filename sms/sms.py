import dropbox
import json
import os

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

access_token = read_token() if os.path.isfile('token') else do_oauth()
client = dropbox.client.DropboxClient(access_token)
print 'linked account: ', client.account_info()

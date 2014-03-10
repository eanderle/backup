import webbrowser
import requests
import facebook
from urlparse import parse_qs

app_id = '273459129487047'
post_login_url = 'https://www.facebook.com/connect/login_success.html'

graph = facebook.GraphAPI()
url = facebook.auth_url(app_id, post_login_url, response_type='token')
print url

webbrowser.open(url)
raw_input('Opening web browser for app permission, press any key when finished...')

data = parse_qs(response)
print data['access_token'][0]

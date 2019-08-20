
import details

from imgurpython import ImgurClient

client_id = details.imgur_id
client_secret = details.imgur_token

client = ImgurClient(client_id, client_secret)

client = ImgurClient(client_id, client_secret)
print(client.get_auth_url('pin'))
credentials = client.authorize(input('Pin: '), 'pin')
print("Authentication successful! Here are the details:")
print("   Access token:  {0}".format(credentials['access_token']))
print("   Refresh token: {0}".format(credentials['refresh_token']))
print("Please paste these in the designated spots in details.py")


#You will only need to do this once per user, store tokens

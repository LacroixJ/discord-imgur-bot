import details

from imgurpython import ImgurClient


client_id = details.imgur_id
client_secret = details.imgur_token
refresh_token = details.refresh_token
access_token = details.access_token

client = ImgurClient(client_id, client_secret, refresh_token)

client.set_user_auth(access_token, refresh_token)


def upload_image(url):
    return 2


def create_album(image_ids): #list of ids
    return 'VR5g2Lg'

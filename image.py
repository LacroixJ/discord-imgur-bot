import details

from imgurpython import ImgurClient


client_id = details.imgur_id
client_secret = details.imgur_token
refresh_token = details.refresh_token
access_token = details.access_token

client = ImgurClient(client_id, client_secret, refresh_token)

client.set_user_auth(access_token, refresh_token)


def upload_image(url):
    image = client.upload_from_url(url, config=None, anon=False)
    image_id = image.get('id')
    return image_id


def create_album(image_ids): #list of ids
    options = {
            'title': 'Your-Album'
            }
    album = client.create_album(options)
    album_id = album.get('id')

    client.album_add_images(album_id, image_ids)

    return album_id

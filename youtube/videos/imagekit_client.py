import os
from imagekitio import ImageKit


def get_streaming_url(url: str):
    return f"{url}/ik-master.m3u8?tr=sr-240_360_480_720_1080"

def get_imagekit_client():
 return ImageKit()
 

def upload_thumbnail(file_data, file_name, folder:str = "thumbnails") :
    public_key = os.environ.get('IMAGEKIT_PUBLIC_KEY')

    import base64

    if file_data.startswith('data'):
        byte64_data = file_data.split(",", 1)[1]
        decoded_data = base64.b64decode(byte64_data)
    else:
        byte64_data = file_data
        decoded_data = base64.b64decode(byte64_data)

     # Upload from file
    client = get_imagekit_client()

    response = client.files.upload(
        file = decoded_data,
        file_name = file_name,
        folder = folder,
        public_key = public_key
    )
    print(f"File ID: {response.file_id}")
    print(f"URL: {response.url}")

    return {
        'file_id': response.file_id,
        'url': response.url
    }

def upload_video(file_data : bytes, file_name : str, folder: str = "videos"):
    public_key = os.environ.get('IMAGEKIT_PUBLIC_KEY')
    # Upload from file
    client = get_imagekit_client()

    response = client.files.upload(
        file = file_data,
        file_name = file_name,
        folder = folder,
        public_key = public_key
    )
    print(f"File ID: {response.file_id}")
    print(f"URL: {response.url}")

    return {
        'file_id': response.file_id,
        'url': response.url
    }

def delete_video(file_id: str) -> bool:
    client = get_imagekit_client()
    client.files.delete(file_id=file_id)
    return True


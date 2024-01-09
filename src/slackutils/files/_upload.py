import imghdr
import io

from pathlibfs import Path
from slack_sdk.web.client import WebClient

SUPPORTED_IMAGES = frozenset({"png", "gif", "bmp", "jpeg"})


def upload_images(token: str, channel: str, filepath: str, description: str):
    client = WebClient(token=token)
    with Path(filepath).open(mode="rb") as f:
        if isinstance(f, io.BytesIO):
            image_type = imghdr.what(f)
        else:
            raise ValueError(f"'{filepath}' is not supported format")
        if image_type not in SUPPORTED_IMAGES:
            raise ValueError(f"'{filepath}' is not supported format")
        client.files_upload(file=f, channels=channel, initial_comment=description)

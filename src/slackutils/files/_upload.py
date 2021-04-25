from contextlib import contextmanager
import io
import imghdr

import s3fs
from slack_sdk.web.client import WebClient

SUPPORTED_IMAGES = {"png", "gif", "bmp", "jpeg"}


@contextmanager
def _open(filepath: str) -> io.IOBase:
    is_s3_path = filepath.startswith("s3://")
    if is_s3_path:
        fs = s3fs.S3FileSystem()
        file = fs.open(filepath)
    else:
        file = open(filepath)
    try:
        yield file
    finally:
        file.close()

def upload_images(token: str, channel: str, filepath: str, description: str):
    client = WebClient(token=token)
    with _open(filepath) as f:
        if not imghdr.what(f) in SUPPORTED_IMAGES:
            raise ValueError(f"'{filepath}' is not supported format")
        client.files_upload(
            file=f, channels=channel, initial_comment=description
        )

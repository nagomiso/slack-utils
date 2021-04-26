import imghdr
import io
from contextlib import contextmanager
from typing import Generator

import s3fs
from slack_sdk.web.client import WebClient

SUPPORTED_IMAGES = {"png", "gif", "bmp", "jpeg"}


@contextmanager
def _open(filepath: str, mode: str = "r") -> Generator[io.IOBase, None, None]:
    is_s3_path = filepath.startswith("s3://")
    if is_s3_path:
        fs = s3fs.S3FileSystem()
        file = fs.open(filepath, mode=mode)
    else:
        file = open(filepath, mode=mode)
    try:
        yield file
    finally:
        file.close()


def upload_images(token: str, channel: str, filepath: str, description: str):
    client = WebClient(token=token)
    with _open(filepath, mode="rb") as f:
        if isinstance(f, io.BytesIO):
            image_type = imghdr.what(f)
        else:
            raise ValueError(f"'{filepath}' is not supported format")
        if image_type not in SUPPORTED_IMAGES:
            raise ValueError(f"'{filepath}' is not supported format")
        client.files_upload(file=f, channels=channel, initial_comment=description)

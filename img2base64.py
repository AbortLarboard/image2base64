from io import BytesIO
from PIL import Image
import base64


def image2base64(img: Image) -> str:
    """returns utf-8 decoded base64 string"""
    buffered = BytesIO()
    img = img.convert('RGBA')
    img.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue())
    buffered.truncate()
    return img_str.decode("utf-8")

"""The Code page."""


import io
import requests
import openai
import PIL.Image

from celestine import load
from celestine.typed import (
    N,
    R,
    H,
    S,
)



def image_data(url):
    """"""
    response = requests.get(url, timeout=5.0)
    content = response.content
    binary = io.BytesIO(content)
    image = PIL.Image.open(binary)
    return image


def image_url(image):
    """"""
    data = image.data
    dictionary = data[0]
    url = dictionary.url
    return url


def generate(hold: H, prompt: str):
    """"""
    client = openai.OpenAI(
        api_key=hold.attribute.key,
        organization=hold.attribute.group,
    )
    image = client.images.generate(
        prompt=prompt,
        model="dall-e-2",
        n=1,
        # quality="hd",
        quality="standard",
        response_format="url",
        # size="1024x1024",
        size="256x256",
        style="vivid",
    )
    return image


def main(*, hold: H, prompt: S, **star: R) -> N:
    """"""
    image = generate(hold, prompt)
    url = image_url(image)
    picture = image_data(url)
    picture.show()
    picture.save("test.png")


# main("A cute baby dragon with a gold bed.")

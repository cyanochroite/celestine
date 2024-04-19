"""Application for generating images with OpenAI."""


import io

import openai
import PIL.Image
import requests

from celestine import language
from celestine.data import (
    code,
    main,
)
from celestine.interface import View
from celestine.session.argument import Optional
from celestine.session.session import (
    AD,
    SuperSession,
)
from celestine.typed import (
    H,
    N,
    R,
    S,
)
from celestine.unicode import NONE

KEY = "key"
GROUP = "group"


class Session(SuperSession):
    """"""

    directory: S

    @classmethod
    def dictionary(cls, core) -> AD:
        """"""
        return {
            KEY: Optional(
                NONE,
                language.TRANSLATOR_SESSION_KEY,
            ),
            GROUP: Optional(
                NONE,
                language.TRANSLATOR_SESSION_REGION,
            ),
        }


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


@code
def draw(hold: H, *, prompt: S, **star: R) -> N:
    """"""
    image = generate(hold, prompt)
    url = image_url(image)
    picture = image_data(url)
    picture.show()
    picture.save("test.png")


@main
def enter(view: View) -> N:
    """"""
    with view.zone("main") as line:
        line.element(
            "main_A",
            text=language.TRANSLATOR_MAIN_BUTTON,
            action="draw",
            prompt="A cute baby dragon with a gold bed.",
        )

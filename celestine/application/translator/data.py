"""Keywords used throughout the translator application."""

from celestine.typed import (
    G,
    TA,
    D,
    N,
    S,
)

INIT = "__init__"
KEY = "key"
LANGUAGE = "language"
LANGUAGE_TAG_AZURE = "LANGUAGE_TAG_AZURE"
LANGUAGE_NAME_ENGLISH = "LANGUAGE_NAME_ENGLISH"
LANGUAGE_TAG_ISO = "LANGUAGE_TAG_ISO"
LANGUAGE_NAME_NATIVE = "LANGUAGE_NAME_NATIVE"
REGION = "region"
SESSION = "session"
TABLE: TA = D[S, S]
TEXT = "text"
TO = "to"
TRANSLATIONS = "translations"
URL = "url"
YIELD_TEXT: TA = G[S, N, N]

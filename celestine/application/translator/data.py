"""Keywords used throughout the translator application."""

from celestine.typed import (
    D,
    G,
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
type TABLE = D[S, S]
TEXT = "text"
TO = "to"
TRANSLATIONS = "translations"
URL = "url"
type YIELD_TEXT = G[S, N, N]

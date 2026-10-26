"""Fonctions partagées du bundle Instagram Skills (version française).

Ce que les skills importent : le parseur d'URL Instagram et le client Apify
(lecture des données publiques d'un hashtag ou d'un profil). Rien ici ne
publie : les skills écrivent, l'utilisatrice publie elle-même dans l'app.
"""
from ._env import load_env

# Charge .env avant que le client Apify lise os.environ.
load_env()

from .url_parser import parse_instagram_url
from .apify_client import ApifyClient, ApifyError, ApifyAuthError

__all__ = [
    "parse_instagram_url",
    "ApifyClient",
    "ApifyError",
    "ApifyAuthError",
]

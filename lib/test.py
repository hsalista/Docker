import requests
import json


def test_get_artists():
    r = requests.get("http://host.docker.internal:8080/artists")
    return print(r.json())

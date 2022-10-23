import requests
from pprint import pprint

spotify_base = "https://api.spotify.com"

if __name__ == "__main__":
    
    req_ret = requests.get(spotify_base)

    pprint(req_ret.status_code)

    pprint(req_ret.json)


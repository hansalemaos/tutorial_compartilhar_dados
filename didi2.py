import codecs

import requests
import pickle

resp = requests.get(
    r"https://github.com/hansalemaos/tutorial_compartilhar_dados/raw/main/futeboltdata.bin"
)

futeboldict = pickle.loads(codecs.decode(resp.content, "base64"))
print(futeboldict)

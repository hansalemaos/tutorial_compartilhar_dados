import codecs
import pickle

futebol = {
    "jogos": {
        1: ("30/09/2012", "Corinthians"),
        2: ("30/11/2012", "Palmeiras (porco do car****o)"),
        3: ("30/12/2012", "Portuguesa"),
    }
}
tostring = codecs.encode(
    pickle.dumps(futebol, protocol=pickle.HIGHEST_PROTOCOL), "base64"
)

with open("c:\\futeboltdata.bin", mode="wb") as f:
    f.write(tostring)

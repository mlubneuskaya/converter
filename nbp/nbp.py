import requests
import gui
import XmlReader as xr
import os

url = "http://api.nbp.pl/api/exchangerates/tables/A/?format=xml"
path = "latest exchange rates.xml"
try:
    response = requests.get(url)
    file = open(path, "wb")
    file.write(response.content)
    file.close()
except requests.ConnectionError:
    if not os.path.isfile(path):
        raise FileNotFoundError
    else:
        pass
currencies = xr.parse_xml(path)
gui.make_gui(currencies)

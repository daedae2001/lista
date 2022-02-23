import requests

url = 'https://i.mjh.nz/PlutoTV/es.xml'

myfile = requests.get(url)

open('es.xml', 'wb').write(myfile.content)

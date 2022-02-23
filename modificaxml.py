
import requests
mylist = [["es.xml", 'https://i.mjh.nz/PlutoTV/es.xml'],
          ["mx.xml", 'https://i.mjh.nz/PlutoTV/mx.xml']]

for x in mylist:
    url = x[1]
    myfile = requests.get(url)
    open(x[0], 'wb').write(myfile.content)

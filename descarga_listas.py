
import requests
mylist = [["es.m3u8", 'https://i.mjh.nz/PlutoTV/es.m3u8', 'es'],
          ["mx.m3u8", 'https://i.mjh.nz/PlutoTV/mx.m3u8', 'mx'],
          ["r1.m3u8", 'https://raw.githubusercontent.com/emiliocuesta/milista/7539e0504f56413d853dcc01ccaf978a531e64a9/lista12', '']]
i = 1
primera = ""
otras = ""

for x in mylist:
    url = x[1]
    myfile = requests.get(url)
    open(x[0], 'wb').write(myfile.content)
    f = open(x[0], 'r')
    primera = f.read()
    f.close()
    print(primera.find('\nhttp://'))
    primera = primera.replace('\nhttp://', '_'+x[2]+'\nhttp://').replace(
        'tvg-id="', 'tvg-id="'+x[2])  # .replace('-id="pluto-', "_"+x[2]+'-id="pluto-')
    f = open(x[0], 'w')
    f.write(primera)
    f.close()

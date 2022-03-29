
import requests
mylist = [["es.m3u8", 'https://i.mjh.nz/PlutoTV/es.m3u8', 'es'],
          ["mx.m3u8", 'https://i.mjh.nz/PlutoTV/mx.m3u8', 'mx'],
          ["r1.m3u8", 'https://raw.githubusercontent.com/emiliocuesta/milista/7539e0504f56413d853dcc01ccaf978a531e64a9/lista12', '']]
primera = ""
otras = ""


def descarga(arch, dir_arch, remplazo=""):
    url = dir_arch
    myfile = requests.get(url)
    open(arch, 'wb').write(myfile.content)
    f = open(arch, 'r')
    primera = f.read()
    f.close()
    # print(primera.find('\nhttp://'))
    # primera = primera.replace('\nhttp://', '_'+remplazo+'\nhttp://').replace(
    #    'tvg-id="', 'tvg-id="'+remplazo)  # .replace('-id="pluto-', "_"+x[2]+'-id="pluto-')
    f = open(arch, 'w')
    f.write(primera)
    f.close()


def descargax(arch, dir_arch, remplazo=""):

    url = dir_arch
    myfile = requests.get(url)
    open(arch, 'wb').write(myfile.content)
    f = open(arch, 'r')
    primera = f.read()
    f.close()
    print(primera.find('\nhttp://'))
    primera = primera.replace('\nhttp://', '_'+remplazo+'\nhttp://').replace(
        'tvg-id="', 'tvg-id="'+remplazo)  # .replace('-id="pluto-', "_"+x[2]+'-id="pluto-')
    f = open(arch, 'w')
    f.write(primera)
    f.close()

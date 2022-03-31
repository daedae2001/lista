
import requests
import gzip

mylist = [["es.xml", 'https://raw.githubusercontent.com/matthuisman/i.mjh.nz/master/PlutoTV/es.xml', 'es'],
          ["mx.xml", 'https://raw.githubusercontent.com/matthuisman/i.mjh.nz/master/PlutoTV/mx.xml', 'mx'],
          ["smes.xml", 'https://i.mjh.nz/SamsungTVPlus/es.xml', ''],
          ["mv.xml", 'http://tropical.jungle-team.online/epg/koala3.xml', '']]
mylist_locales = [["aizzi.xml", 'aizzi.xml', '']]

i = 1
primera = ""
otras = ""


def insertar_texto(cadena, texto):
    posicion = cadena.find('<programme channel="')
    if posicion <= len(cadena):
        izquierda = cadena[:posicion]
        derecha = cadena[posicion:]

        return '{} {} {}'.format(izquierda, texto, derecha)
    else:
        raise ValueError(
            'La posición donde se quiere insertar el texto no existe.')


for x in mylist:
    url = x[1]
    myfile = requests.get(url)
    open(x[0], 'wb').write(myfile.content)
    f = open(x[0], 'r', encoding="utf8")

    if i == 1:
        primera = f.read()
        f.close()
        primera = primera.replace('<channel id="', '<channel id="' +
                                  x[2]).replace('<programme channel="', '<programme channel="'+x[2]).replace("</display-name>", "_"+x[2]+"</display-name>")
    else:
        otras = f.read()
        f.close()
        otras = otras[otras.find('<channel id="'):]
        otras = otras.replace('<channel id="', '<channel id="' +
                              x[2]).replace('<programme channel="', '<programme channel="'+x[2]).replace("</display-name>", "_"+x[2]+"</display-name>")
        otras = otras.replace("</tv>", "")
        primera = insertar_texto(primera, otras)
        #p1 = otras[0: otras.find('<programme channel="')]
        #p2 = otras[otras.find('<programme channel="'):len(otras)]
        #primera = primera[otras.find('<channel id="'):len(otras)]

    i = i+1
locales = open(mylist_locales[0][1], "r")
otras = locales.read()
locales.close
primera = insertar_texto(primera, otras)

f = open('todo.xml', 'w', encoding="utf8")
f.write(primera)
f.close()


try:
    f = open('todo.xml', "rb")
except IOError as e:
    print(e.errno, e.message)
else:
    data = f.read()
    f.close()

if data is not None:
    f = gzip.open('todo.xml' + ".gz", "wb")
    f.write(data)
    f.close()


import requests
mylist = [["es.xml", 'https://i.mjh.nz/PlutoTV/es.xml', 'es'],
          ["mx.xml", 'https://i.mjh.nz/PlutoTV/mx.xml', 'mx']]
i = 1
primera = ""
otras = ""

for x in mylist:
    url = x[1]
    myfile = requests.get(url)
    open(x[0], 'wb').write(myfile.content)
    f = open(x[0], 'r')

    if i == 1:
        primera = f.read()
        f.close()
        primera = primera.replace('<channel id="', '<channel id="' +
                                  x[2]).replace('<programme channel="', '<programme channel="'+x[2]).replace("<display-name>", "<display-name>"+x[2])
    else:
        otras = f.read()
        f.close()

        otras = otras.replace('<channel id="', '<channel id="' +
                              x[2]).replace('<programme channel="', '<programme channel="'+x[2]).replace("<display-name>", "<display-name>"+x[2])
        p1 = otras[0: otras.find('<programme channel="')]
        p2 = otras[otras.find('<programme channel="')+10:len(otras)]
        primera = primera[otras.find('<channel id="'):len(otras)]
        primera = (p1 + primera.replace("</tv>", "") + p2)
    i = i+1
f = open('todo.xml', 'w')
f.write(primera)
f.close()

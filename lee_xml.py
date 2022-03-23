
import requests
mylist = [["movistar.xml", 'http://tropical.jungle-team.online/epg/koala3.xml', '']]
i = 1
primera = ""
otras = ""

for x in mylist:
    url = x[1]
    myfile = requests.get(url)
    open(x[0], 'wb').write(myfile.content)
    f = open(x[0], 'r', encoding="utf8")

    if i == 1:
        primera = f.read()
        f.close()
        #primera = primera.replace('<channel id="', '<channel id="' + x[2]).replace('<programme channel="', '<programme channel="'+x[2]).replace("</display-name>", "_"+x[2]+"</display-name>")
        
    else:
        pass
f = open('movistar.xml', 'w', encoding="utf8")
f.write(primera)
f.close()
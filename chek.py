import requests

#ht = requests.get("https://piratilla.com/836015/ek?ch=tnt",  timeout=0.5)

f = open("tv20.m3u", 'r', encoding="utf8")
linea=f.read()

linea=linea.replace(',http','\nhttp')


f.close
f=open('tv201.m3u','w')
f.write(linea)
f.close
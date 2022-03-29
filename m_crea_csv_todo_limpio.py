# id	estatus	url	Channel-id	nombre	url2	tvg-id	tvg-chno	tvg-logo	group-title
import requests
import sys
import pandas as pd
titulos = ['channel-id', 'tvg-id', 'tvg-logo', 'group-title', 'nombre', 'url']

id = 0


def extrae(t, b):
    i = b
    f = ","
    try:
        esta = t.find(i)

        if esta >= 0:
            inicio = t.find(i)+len(i)+1
            fin = t.find(f, inicio)
            r = t[inicio: fin]
            return r
        else:
            r = '"x"'
            return r
    except:
        r = '"x"'
        return r


def crea_csv_todo_limpio(arch):
    texto_com = ''
    f = open(arch, 'r', encoding="utf8")
    for linea in f:
        i = 0
        texto = ''
        ix = 'ix='+str(++id)+',0,'
        for t in titulos:
            #rr = titulos[i]+'='+extrae(linea, t)
            rr = extrae(linea, t)
            i = i+1
            texto = texto+rr+','
        #texto.replace('http', '\nhttp')
        texto_com = texto_com+ix+texto+'\n'

    f.close()
    f = open(arch, 'w', encoding="utf8")
    f.write(texto_com)
    f.close()
# -----------------------------------------

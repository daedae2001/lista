from cmath import nan
import requests
import sys
import pandas as pd


def crea_m3u(arch):
    df = pd.read_csv(arch)

    # #EXTM3U  #EXTINF:-1 "id,estatus,Channel-id,tvg-id, tvg-logo,group-title,nombre,url"
    #df['estatus'] = df['estatus'].replace({0: 1})
    w = 0
    txt = "#EXTM3U\n"
    for i, row in df.iterrows():
        try:
            if row["estatus"] < 300:
                txt = txt+"#EXTINF:-1 "
                if row['channel-id'] == nan:
                    row['channel-id'] = "x"
                if row['tvg-id'] == nan:
                    row['tvg-id'] = "x"
                if row['tvg-logo'] == nan:
                    row['tvg-logo'] = "http://n"
                if row['group-title'] == nan:
                    row['group-title'] = "otros"
                if row['nombre'] == nan:
                    row['nombre'] = "sin nombre"
                if row['url'] == nan:
                    row['url'] = "http://n"

                txt = txt+'channel-id='+row['channel-id']+" "
                txt = txt+'tvg-id='+row['tvg-id']+" "
                txt = txt+'tvg-logo='+row['tvg-logo']+" "
                txt = txt+'group-title=' + row['group-title'] + ","
                txt = txt+row['nombre']+"\n"
                txt = txt+row['url']+"\n"

            else:
                pass
        except:
            pass
    f = open("l1.m3u", 'w', encoding="utf8")
    f.write(txt)
    f.close()

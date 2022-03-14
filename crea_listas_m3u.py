import requests
import sys
import pandas as pd
df = pd.read_csv("base_lista_canalesx.csv", index_col=0)

# #EXTM3U  #EXTINF:-1 "id,estatus,url,Channel-id, nombre,url2, tvg-id, tvg-chno, tvg-logo,group-title"
#df['estatus'] = df['estatus'].replace({0: 1})
w = 0
txt = "#EXTM3U\n"
for index, row in df.iterrows():
    try:
        if row["estatus"] < 300:
            txt = txt+"#EXTINF:-1 "
            txt = txt+row['Channel-id']+" "
            txt = txt+row['tvg-id']+" "
            txt = txt+row['tvg-logo']+" "
            txt = txt+row['group-title'] + ","
            txt = txt+row['nombre']+"\n"
            txt = txt+row['url']+"\n"

        else:
            pass
    except:
        pass
f = open("lista1.m3u", 'w', encoding="utf8")
f.write(txt)
f.close()

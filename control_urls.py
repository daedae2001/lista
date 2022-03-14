import requests
import sys
import pandas as pd

df = pd.read_csv("base_lista_canales.csv")

df['estatus'] = df['estatus'].replace({0: 1})

df.to_csv("base_lista_canales.csv", index=False)

print(df)
destFile = r"resultado.txt"
res = open(destFile, "w")
urls = open("urls.txt", "r")
for url in urls:
    try:
        resultado = requests.get(url.replace("\n", ""))
        res.write(str(resultado.status_code) + ", " + url.replace("\n", "") +
                  "\n")
        #print(url.replace("\n", "") + ", " + resultado.text + "\n")
    except:
        res.write("error" + ", " + url.replace("\n", "") + "\n")

res.close()
urls.close()

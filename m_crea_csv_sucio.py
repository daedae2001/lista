import numpy as np
import requests


def crea_csv_sucio(arch):
    i = 1
    primera = ""
    otras = ""
    registro = []
    registro_nuevo1 = []

    f = open(arch, 'r', encoding="utf8")
    if i == 1:
        j = 0
        for linea in f:
            linea = linea.replace("#EXTINF:0", "#EXTINF:0").replace("  # EXTINF:1", "#EXTINF:0").replace("  # EXTINF:-1", "#EXTINF:0").lower().replace("  ", " ").replace("  ", " ").replace(": 0 ", "=0").replace(
                ":1 ", "=1;").replace('" ', '";').replace(", ", ",").replace(" ,", ",")
            j = j+1

            if linea[0:7] == "#extm3u":
                pass
            elif linea[0:4] == "http":
                registro_nuevo1.append(["url", linea.replace('\n', '')])
            # print(registro_nuevo)
                try:
                    registro.append(registro_nuevo1)
                    registro_nuevo1 = []
                except:
                    pass
            else:
                #print(str(j) + " " + linea)
                l1 = linea.replace(":", "=").replace("=//", "://").split(",")
                l1[0] = l1[0]+";nombre=" + \
                    l1[1].replace('\n', '')
                l2 = l1[0].split(";")
                l3 = l1[0].split(' ')
                for a in l2:
                    try:
                        registro_nuevo1.append(a.split("="))
                    except:
                        pass
                # print("nuevo")

        f.close()
        # print(registro)
    f = open(arch.replace("m3u8", "py").replace(
        "m3u", "py"), 'w', encoding="utf8")
    f.write("canales=" +
            str(registro))
    f.close()
    f = open(arch.replace("m3u8", "csv").replace(
        "m3u", "csv"), 'w', encoding="utf8")
    txt = str(registro).replace("]], [[", "\n").replace("', '", "=").replace(
        "['", "").replace("']", "").replace("[[", "").replace("]]", "").replace("'", "").replace(', logo ="', ',tvg-logo="').replace('", group="', '", group-title="')
    txt = txt.replace(', type="stream",', ',')
    txt = txt.replace(', channelid="', ', channel-id="')
    txt = txt.replace(', type="favorites",', '')
    txt = txt.replace(', logo="', ',tvg-logo="')
    txt = txt.replace('#extinf=0, ', '')
    txt = txt.replace('nombre, "mtv spankin new"]',
                      'nombre="mtv spankin new"')
    txt = txt.replace('#extinf=0 ', '')
    txt = txt.replace(', type="stream",', ',')
    txt = txt.replace(', group-title=', ',group-title=')
    txt = txt.replace(', nombre=', ',nombre=')
    txt = txt.replace(', url=', ',url=')
    txt = txt.replace(', name="la_sd=axn"', '')

    f.write(txt)
    f.close()

def procesa_linea_m3u_sucia(linea):
    registro = []
    registro_nuevo1 = []
    j = 0
    print('')
    linea = linea.replace("#EXTINF:1", "#EXTINF:0").replace("#EXTINF:-1", "#EXTINF:0").lower().replace("  ", " ").replace("  ", " ").replace(":0 ", "=0;").replace(
        ":1 ", "=1;").replace('" ', '";').replace(", ", ",")
    print(linea+'\n')
    j = j+1
    print(linea[0:7]+'\n')
    if linea[0:7] == "#extinf":
        #print(str(j) + " " + linea)
        l1 = linea.replace(":", "=").replace("=//", "://").split(",")
        print(l1[0]+'\n')
        print(l1[1]+'\n')
        l1[0] = l1[0]+";nombre=" + \
            l1[1].replace('\n', '')
        print(l1[0]+'\n')
        l2 = l1[0].split(";")
        print(l2)
        for a in l2:
            try:
                registro_nuevo1.append(a.split("="))
            except:
                pass
        # print("nuevo")
    elif linea[0:7] == "#extm3u":
        pass
    elif linea[0:4] == "http":
        registro_nuevo1.append(["url", linea.replace('\n', '')])
    # print(registro_nuevo)
        try:
            registro.append(registro_nuevo1)
            registro_nuevo1 = []
        except:
            pass
    return registro


l = '#EXTINF:0 type="stream" channelId="-1" name="Planetatv Kidss" logo="https://www.m3u.cl/logo/1015_Planetatv_Kids.png", Planetatv Kids * | CL\nhttps: // mediacpstreamchile.com: 1936/8152/8152/playlist.m3u8'
procesa_linea_m3u_sucia(l)

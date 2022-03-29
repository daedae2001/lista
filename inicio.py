import pandas as pd
import xml.etree.ElementTree as Xet
lista_canales = ["24 HORAS", "307SonyComedias", "74 tv", "7NNNOTICIAS", "ae 2", "alf", "ARAGONTV", "buin somos todos cl", "butaca tv 2", "canal visión dorada sd caldas", "CANAL10", "CANAL26", "canl nn", "Cartelera lavozdetucuman", "central comedy", "cine life", "CINE.AR", "CINE", "cinema+", "CINEMAX", "cosmos tv", "CRONICA", "cultura 24 tv", "DARK", "Discovery Science", "DISTRITOTV", "EL TRECE ARG", "EL TRECE", "EL12TV", "ELCHAVODEL8", "ELTOROTV", "ENCUENTRO", "es5f1abce155a03d0007718834", "es5f1ac1f1b66c76000790ef27", "es5f1ac2591dd8880007bb7d6d", "es5f1ac8099c49f600076579b2", "es5f1ac8a87cd38d000745d7cf", "es5f1ac947dcd00d0007937c08", "es5f1ac9a2d3611d0007a844bb", "es5f1aca8310a30e00074fab92", "es5f1acb4eebe0f0000767b40f", "es5f1acba0d1f6340007db8843", "es5f1acbed25948a0007ffbe65", "es5f1acc3e061597000768d4ea", "es5f1acc3e061597000768d4ea", "es5f1acc91cc9e1b000711ff21", "es5f1acdaa8ba90f0007d5e760", "es5f6a38eaa5b68b0007a00e7a", "es5f984c1dc54853000797a5e8", "es5f984f4a09e92d0007d74647", "es5f9853138d19af0007104a8d", "es60218baa464ef900073168c1", "es602ba1cfb386d30007aecbbe", "es6086d3f420fc8500075f8dbf", "es60c343007bcabe0007242aa6", "es60c343ad476ec00007c2ec1a", "es60c8a24e17da110007eed4fd", "es60cc807324d60a0007708dc8", "es60d3574e97f10800078455de", "es60dafb9a0df1ba000758d37b", "es60dd6b1da79e4d0007309455", "es60e45687313c5f0007bc8e94", "es60e4573c9f963e00077ecf25", "es60ed5fb9c4716d0007d180c5", "es612ce5214bb5790007ad3016", "es61373bb45168fe000773eecd", "es61922be835f3910007fc58f6", "es6193963c5a960200074ce816", "es61cd78920b90cb0007e28231", "ESAJ3800001KT", "ESAJ3800005C5", "ESAJ3800007PC", "ESAJ3800008ZD", "ESAJ4500016BH", "ESAJ45000181E", "ESAJ4500019AM", "ESAJ4500020V7", "ESAJ4500021HQ", "ESAJ4500023Y5", "ESAJ49000017H", "ESBA1400001OG", "ESBA1400006NP", "ESBA1400008NE", "ESBA2200004G5", "ESBA2200005D6", "ESBA2200006B4", "ESBA2200008NQ", "ESBA22000094V", "ESBA22000102A", "ESBA3300017FA", "ESBA3300019NX", "ESBA3300021PZ", "ESBA3300022SL", "ESBA3300024AJ", "ESBA3300025WZ", "ESBA3300027H5", "ESBA3300036W1", "ESBA3300039ZX", "ESBA330004121", "ESBC400001QQ", "ESBC40000248", "EvaRetro", "EvaStream", "EXTREMATV", "feel good verdi hd españa", "frecuencia musical tv", "FX", "GOLDEN PLUS", "gourmet tv", "HISTORY", "HMTV", "ivestigacion", "LA 1", "LA 2", "LA SEXTA", "LATINO DE PELICULA", "LOS SIMSONS", "LOVE NATURE EN ESPAÑOL", "m+", "miami tv internacional hd estados unidos", "miami tv jenny for you hd estados unidos",
                 "miami tv méxico hd méxico", "MiTVTelevisiónClásica", "MTMAD24H", "mx5dcb62e63d4d8f0009f36881", "mx5dcdde78f080d900098550e4", "mx5dcddf1ed95e740009fef7ab", "mx5dcddfbdb7cf0e0009ae09ea", "mx5dcddfcb229eff00091b6bdf", "mx5dcde0657444a40009cd2422", "mx5dcde197f6591d0009839e04", "mx5dcde27ffae9520009c0c75a", "mx5dcde2f53449c50009b2b4dc", "mx5dcde437229eff00091b6c30", "mx5dd6ab8056beb000091fc6b6", "mx5dd6ddb30a1d8a000908ed4c", "mx5dd7ea2aeab5230009986735", "mx5dd834c66fe2ca0009303b8d", "mx5dd8364ea1d6780009929902", "mx5dd837642c6e9300098ad484", "mx5dd837642c6e9300098ad484", "mx5dd85eac039bba0009e86d1d", "mx5ddc266f80e3550009136843", "mx5ddc4e8bcbb9010009b4e84f", "mx5de5758e1a30dc00094fcd6c", "mx5de802659167b10009e7deba", "mx5de802659167b10009e7deba", "mx5defde6d6c07b50009cf0757", "mx5df265697ec3510009df1ef0", "mx5e3ddbd27091820009f86dd9", "mx5e67d41b93312100076f3fca", "mx5e8397936791b30007ebb5a7", "mx5e972a21ad709d00074195ba", "mx5ebaccf1734aaf0007142c86", "mx5efb8c19b2678b000780d032", "mx5f230e416b68ff00075b0139", "mx5f23102d5e239d00074b092a", "mx5f2817d3d7573a00080f9175", "mx5f610042272f68000867685b", "mx5f9992c685a2a80007fa414a", "mx5f9afb01816137000737f799", "mx5fcea359e533cb0007215c71", "mx5ffcc21a432945000762d06b", "mx609059dc63be6e0007b4eca6", "mx609062295c2b8f0007199e7a", "mx6095ad97351eb0000754c1e6", "mx609ae5cd48d3200007b0a98e", "mx61099f2b40d0640007fc5aa2", "mx6109a9f5531b840007a4a187", "mx6109ab25b84d6a0007504886", "mx615b9855c6b58b000724477f", "mx619d59b7cbef25000728221c", "my time movies 1", "my time movies 2", "NETTV", "Peliculas 01", "Peliculas 02", "Peliculas 03", "Peliculas 04", "Peliculas 05", "Peliculas 06", "Peliculas 07", "Peliculas 08", "Peliculas 09", "Peliculas 10", "Peliculas 11", "Peliculas 12", "Peliculas 13", "Peliculas 14", "Peliculas 15", "Peliculas 16", "Peliculas 17", "Peliculas 18", "Peliculas 19", "Peliculas 20", "Peliculas 21", "Peliculas 22", "Peliculas 23", "Peliculas 24", "Peliculas 25", "Peliculas 26", "Peliculas 27", "Peliculas 28", "Peliculas 29", "Peliculas 30", "Peliculas 31", "Peliculas 32", "PELICULAS CB", "peliculas pluto", "planeta tv", "rakuten tv acción hd españa", "rakuten tv comedias hd españa", "rakuten tv drama hd españa", "retro plus tv señal 3 cl", "runtime-espanol-roku", "SaberMas", "samsung1", "SONY CHANELS", "STUDIO UNIVERSAL", "TCM", "TELECANAL12HD", "TELEFERO", "The Walking Dead en español", "TNT", "topcine", "Viaje a las estrellas", "WARNER", "wow"]
start = ""
stop = ""
channel = ""
desc = ""
title = ""
icon = ""
url = ""
country = ""
episodenum = ""
starrating = ""
subtitle = ""
category = ""
id = ""
displayname = ""

cols_channels = ["id", "display-name", "url", "icon"]
rows_channels = []
cols_programmes = ["start", "stop", "channel",
                   "desc", "title", "icon", "url",
                   "country", "episode-num", "star-rating",
                   "sub-title", "category"]
rows_programmes = []
lin = '<?xml version="1.0" encoding="UTF-8"?><tv>\n'
linp = ''
try:
    xmlparse = Xet.parse('todo.xml')
    root = xmlparse.getroot()
    print(root)
    i = 0
    for hijo in root:
        if hijo.tag == 'channel':
            i = i+1
            print(str(i))
            id = hijo.attrib["id"]
            for nieto in hijo:
                if nieto.tag == 'display-name':
                    displayname = nieto.text
                elif nieto.tag == 'url':
                    url = (nieto.text)
                elif nieto.tag == 'icon':
                    icon = (nieto.attrib["src"])
            if id in lista_canales:
                lin = lin+'<channel id="'+id+'">\n'
                lin = lin+'<display-name>'+displayname+'</display-name>\n'
                lin = lin+'</channel>\n'
                rows_channels.append({"id": id,
                                      "display-name": displayname,
                                      "url": url,
                                      "icon": icon})
                id = ""
                displayname = ""
                url = ""
                icon = ""

        elif hijo.tag == 'programme':

            i = i+1
            print(str(i))
            start = (hijo.attrib["start"])
            stop = (hijo.attrib["stop"])
            channel = (hijo.attrib["channel"])

            for nieto in hijo:
                if nieto.tag == 'desc':
                    desc = (nieto.text.replace('&amp;', '').replace(
                        '\n\n', '\n').replace('\n\n', '\n').replace('\n\n', '\n').replace(';', '.\n'))
                    print(desc)
                elif nieto.tag == 'title':
                    title = (nieto.text.replace(
                        '&amp;', ' ').replace(';', ' '))
                elif nieto.tag == 'icon':
                    icon = (nieto.attrib["src"])
                elif nieto.tag == 'url':
                    url = (nieto.text)
                elif nieto.tag == 'country':
                    country = (nieto.text)
                elif nieto.tag == 'episode-num':
                    episodenum = (nieto.text)
                elif nieto.tag == 'star-rating':
                    starrating = (nieto[0].text)
                elif nieto.tag == 'sub-title':
                    subtitle = (nieto.text.replace(
                        '&amp;', ' ').replace(';', ' '))
                elif nieto.tag == 'category':
                    category = (nieto.text.replace(
                        '&amp;', ' ').replace(';', ' '))
            if channel in lista_canales:
                linp = linp+'<programme channel="'+channel + \
                    '" start="'+start+'" stop="'+stop+'">\n'
                linp = linp+'<title>'+title+'</title>\n'
                linp = linp+'<desc>'+desc+'</desc>\n'
                linp = linp+'</programme>\n'
                rows_programmes.append({"start": start,
                                        "stop": stop,
                                        "channel": channel,
                                        "desc": desc,
                                        "title": title,
                                        "icon": icon,
                                        "url": url,
                                        "country": country,
                                        "episode-num": episodenum,
                                        "star-rating": starrating,
                                        "sub-title": subtitle,
                                        "category": category})
                start = ""
                stop = ""
                channel = ""
                desc = ""
                title = ""
                icon = ""
                url = ""
                country = ""
                episodenum = ""
                starrating = ""
                subtitle = ""
                category = ""


except Exception as err:
    print("Error:", err)
finally:
    pass

f = open('todon.xml', 'w')
f.write(lin+linp+'</tv>')
f.close()
df_channels = pd.DataFrame(rows_channels, columns=cols_channels)
df_programmes = pd.DataFrame(rows_programmes, columns=cols_programmes)
# Writing dataframe to csv
df_channels.to_csv('channels.csv', sep=';')
df_programmes.to_csv('programmes.csv', sep=';')

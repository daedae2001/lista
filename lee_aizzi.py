import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import datetime
import sys
from datetime import datetime, date, timedelta
canales = []
canal = []
horarios = []
horario = []
linea = 1
texto = ''
anterior = ''


def cambio_hora(fecha, hora_texto, modif_horaria):
    global anterior
    partes = (hora_texto.split('-'))
    parte0 = partes[0].strip()
    pp1 = parte0.split(' ')[0]
    p1 = parte0.split(' ')[1]
    h1 = int(pp1.split(':')[0].replace('24', '00'))
    m1 = int(pp1.split(':')[1].replace(' ', '0'))
    parte1 = partes[1].strip()
    pp2 = parte1.split(' ')[0]
    p2 = parte1.split(' ')[1]
    h2 = int(pp2.split(':')[0].replace('24', '00'))
    m2 = int(pp2.split(':')[1].replace(' ', '0'))
    if p1 == 'P.M.':
        h1 = h1+12
    if p2 == 'P.M.':
        h2 = h2+12
    dia = fecha.day
    mes = fecha.month
    año = fecha.year
    ahora = datetime.now()
    dia2 = dia
    mes2 = mes
    año2 = año
    if p1 == 'A.M.' and anterior == 'P.M.':
        fecha2 = (fecha+timedelta(days=1))
        dia2 = (fecha2).day
        mes2 = (fecha2).month
        año2 = (fecha2).year
        pass

    res = ' start ="' + str(año*10000000000+mes*100000000+dia *
                            1000000+h1*10000+m1*100)+' '+modif_horaria+'" stop="'+str(año2*10000000000+mes2*100000000+dia2 *
                                                                                      1000000+h2*10000+m2*100)+' '+modif_horaria+'">\n'

    anterior = p2
    return res


def extrae(texto_origen, texto_buscado, texto_fin):
    i = texto_buscado
    f = texto_fin
    try:
        esta = texto_origen.find(i)

        if esta >= 0:
            inicio = texto_origen.find(i)+len(i)
            fin = texto_origen.find(f, inicio)
            r = texto_origen[inicio: fin]
            return [r, fin]
        else:
            r = ['', fin]
            return r
    except:
        r = ['', 0]
        return r


x = datetime.now()
fecha = "%s/%s/%s" % (x.day, x.month, x.year)

driver = webdriver.Chrome(executable_path="./chromedriver")
driver.get("https://www.izzi.mx/webApps/entretenimiento/guia")
time.sleep(2)


def lee_horarios(canal):
    global texto
    global linea
    try:
        xpath = f"/html/body/main/section/div/div/div[2]/div[2]/div/div/div[2]/div[2]/ul/li[{linea}]"
        lista_horarios = driver.find_element(
            by=By.XPATH, value=xpath).get_attribute('outerHTML')
        linea = linea+1
        salida = 1

        while(salida > 0):
            texto = texto+'<programme channel="' + \
                canal.replace('&amp;', ' y ')+'_la"'
            resultado = extrae(lista_horarios, 'data-duracion="', '"')
            lista_horarios = lista_horarios[resultado[1]:]
            horarios.append(resultado[0])
            if resultado[1] > 0:
                resultado = extrae(
                    lista_horarios, '"hora-inicial">', '</span>')
                lista_horarios = lista_horarios[resultado[1]:]
                title = extrae(lista_horarios, 'alt="', '"')[0]
                lista_horarios = lista_horarios[resultado[1]:]
                #texto = texto+'<channel id ="'+resultado[0]+'">\n'
                horarios.append(resultado[0])
                resultado = extrae(
                    lista_horarios, '<p class="fw-medium">', '</p>')
                lista_horarios = lista_horarios[resultado[1]:]
                start_stop = cambio_hora(datetime.now(), resultado[0], '+0500')
                img = extrae(lista_horarios, '<img data-src="', '"')
                lista_horarios = lista_horarios[resultado[1]:]
                horarios.append(resultado[0])
                desc = extrae(
                    lista_horarios, '<p>', '</p>')[0].replace('<span class="bold program-label">', '').replace('<span class="bold program-label">Actores:</span> ', '').replace('<span class="program-content">', '').replace('</span>', '')
                lista_horarios = lista_horarios[resultado[1]:]
                horarios.append(resultado[0])
                resultado = extrae(lista_horarios, 'program-langs', '">')
                lista_horarios = lista_horarios[resultado[1]:]
                pass

            texto = texto+start_stop+'<title>'+title + \
                '</title>\n'+'<desc>'+desc+'</desc>\n</programme>\n'

            if len(lista_horarios) > 150:
                salida = 1
            else:
                salida = 0

        pass

    except:
        print("Error inesperado:", sys.exc_info()[0])


# d0.click()
# time.sleep(1)
xpath = "/html/body/main/section/div/div/div[2]/div[2]/div/div/div[2]/div[1]/ul"
lista_canales = driver.find_element(
    by=By.XPATH, value=xpath).get_attribute('outerHTML')
salida = 1
while(salida > 0):
    resultado = extrae(lista_canales, '<img src="', '"')
    lista_canales = lista_canales[resultado[1]:]
    logo = 'https://www.izzi.mx'+resultado[0]
    #texto = texto+'<channel id ="'+canal_id+'">\n'
    #canal.append(resultado[0].replace('"', ''))
    if resultado[1] > 0:
        resultado = extrae(lista_canales, 'alt="', '"')
        canal_id = resultado[0]
        canal.append(canal_id)
        texto = texto+'<channel id = "'+canal_id.replace('&amp;', ' y ')+'_la">\n<display-name>' + \
            canal_id.replace('&amp;', ' y ')+'_la' + \
            ' </display-name>\n </channel>\n'
        lista_canales = lista_canales[resultado[1]:]

        resultado = extrae(lista_canales, '</l', '>')
        lista_canales = lista_canales[resultado[1]:]

    if len(lista_canales) > 8:
        salida = 1
    else:
        salida = 0
    #texto = texto+'<channel id ="'+canal_id+'">\n'
    #texto = texto+'<display-name>' + resultado[0]+'</display-name>\n</channel>\n'
    #texto = texto+'<programme channel="'+resultado[0]+'_la"'
    canales.append(canal)
    canal = []

# lee_horarios()
for can in canales:

    lee_horarios(can[0])


driver.close()
f = open('aizzi.xml', 'w')
f.write(texto.replace('<desc></desc>', '<desc>nn</desc>'))
f.close

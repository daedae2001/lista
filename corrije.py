f = open('tv21.m3u', 'r')
texto = f.read()
texto = texto.replace(',http', '\nhttp')
f.close()
f = open('tv21.m3u', 'w')
f.write(texto)
f.close()

from datetime import datetime

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
    if p1 == 'A.M.' and anterior == 'P.M.':
        dia2 = fecha.timedelta(days=1).day
        ' start="20220330000000 +0200" stop="20220330003000 +0200">'
    res = ' start ="' + str(año*10000000000+mes*100000000+dia *
                            1000000+h1*10000+m1*100)+' '+modif_horaria+'" stop="'+str(año*10000000000+mes*100000000+dia2 *
                                                                                      1000000+h2*10000+m2*100)+' '+modif_horaria+'">'

    anterior = p2
    return res


a = datetime.now()
print(a)
cambio_hora(a, '24:30 A.M. - 1:30 A.M.', '+0500')

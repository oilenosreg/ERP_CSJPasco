import re

def caracteres_alfabeticos(texto):
    '''
    Evalua si la cadena contiene, solo caracteres alfabéticos, 
    incluyendo el espacio en blanco y los acentos y tíldes del 
    idioma español.
    '''
    patron = '^[ a-zA-ZÑñÁáÉéÍíÓóÚúÜü]+$'
    #evaluar = re.compile(patron, re.UNICODE)
    # resultado = evaluar.match(texto)
    
    resultado = re.match(patron, texto)

    if resultado:
        # print(f'resultado: {resultado}')
        return True
    else:
        return False 


def caracteres_numericos(texto):
    '''
    Evalua si la cadena contiene, solo caracteres numéricos.
    '''
    patron = '^[0-9]+$'
    resultado = re.match(patron, texto)

    if resultado:
        return True
    else:
        return False

# print(caracteres_alfabeticos('elio clímaco Núñez'))
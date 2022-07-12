import os, time
from uuid import uuid4


def renombrar_imagen(persona, archivo):
    carpeta = 'personas'
    extension = archivo.split('.')[-1]
    print(extension)
    fecha_hora = time.strftime('%Y%m%d%H%M%S')
    if persona.dni:
        archivo = f'{persona.dni}-{persona.apellido_paterno}_{persona.apellido_materno}-{persona.nombres}_{fecha_hora}.{extension}'
    else:
        archivo = f'{uuid4().hex}.{extension}'
    imagen = os.path.join(carpeta, archivo).upper()
    return imagen
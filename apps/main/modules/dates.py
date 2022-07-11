from datetime import date


def calcular_edad(fecha_nacimiento):
    '''
    Función que calcula la edad al día de hoy a partir de la fecha de
    nacimiento; parámetro <date:fecha_nacimiento>
    '''
    hoy = date.today()

    try:
        anio = fecha_nacimiento.replace(year = hoy.year)
    except ValueError:
        anio = fecha_nacimiento.replace(
            year = hoy.year,
            month = fecha_nacimiento.month + 1,
            day = 1
        )
    
    if fecha_nacimiento > hoy:
        return hoy.year - fecha_nacimiento.year - 1
    else:
        return hoy.year - fecha_nacimiento.year


def menor_edad(edad):
    if edad < 18:
        return True
    else:
        return False


edad = calcular_edad(date(2021,12,31))
menor_edad(edad)
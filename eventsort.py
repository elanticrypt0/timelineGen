from datetime import datetime

def sortEventsByDate(eventos, ordenAsc=True):
    # Convertir las fechas de string a datetime
    for evento in eventos:
        evento.date = datetime.strptime(evento.date, '%Y-%m-%d %H:%M')

    # Ordenar los eventos según la fecha
    eventos_ordenados = sorted(eventos, key=lambda x: x.date, reverse=ordenAsc)

    # Convertir las fechas de datetime de vuelta a string
    for evento in eventos_ordenados:
        evento.date = evento.date.strftime('%Y-%m-%d %H:%M')

    return eventos_ordenados
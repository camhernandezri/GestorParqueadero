from datetime import datetime
from models import db, Registro

PRECIO_HORA = 2000  # pesos por hora

def registrar_entrada(placa):
    nuevo = Registro(placa=placa)
    db.session.add(nuevo)
    db.session.commit()
    return nuevo

def registrar_salida(placa):
    registro = Registro.query.filter_by(placa=placa, hora_salida=None).first()
    if not registro:
        return None

    registro.hora_salida = datetime.now()
    horas = (registro.hora_salida - registro.hora_entrada).total_seconds() / 3600
    registro.costo = round(horas * PRECIO_HORA, 2)

    db.session.commit()
    return registro

def obtener_total_dia():
    hoy = datetime.now().date()
    registros = Registro.query.filter(
        Registro.hora_salida != None,
        Registro.hora_salida >= datetime.combine(hoy, datetime.min.time()),
        Registro.hora_salida <= datetime.combine(hoy, datetime.max.time())
    ).all()

    total = sum(r.costo for r in registros if r.costo)
    return total, registros

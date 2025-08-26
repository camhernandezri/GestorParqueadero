from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Registro(db.Model):
    __tablename__ = 'registros'
    id = db.Column(db.Integer, primary_key=True)
    placa = db.Column(db.String(10), nullable=False)
    hora_entrada = db.Column(db.DateTime, default=datetime.now)
    hora_salida = db.Column(db.DateTime, nullable=True)
    costo = db.Column(db.Float, nullable=True)

    def __repr__(self):
        return f"<Registro {self.placa}>"

from flask import Flask, render_template
from config import SQLALCHEMY_DATABASE_URI, SQLALCHEMY_TRACK_MODIFICATIONS
from models import db
from routes import routes
from controllers import PRECIO_HORA
from datetime import datetime

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = SQLALCHEMY_TRACK_MODIFICATIONS

db.init_app(app)
app.register_blueprint(routes)

@app.route("/")
def home():
    # Fecha actual en formato DD/MM/YYYY
    fecha_actual = datetime.now().strftime("%d/%m/%Y")
    return render_template("index.html", precio=PRECIO_HORA, fecha=fecha_actual)

@app.route("/reporte-view")
def reporte_view():
    return render_template("reporte.html")

@app.route("/reporte")
def reporte():
    registros = Registro.query.all()
    data = []
    for r in registros:
        data.append({
            "id": r.id,
            "placa": r.placa,
            "hora_entrada": r.hora_entrada.strftime("%Y-%m-%d %H:%M:%S"),
            "hora_salida": r.hora_salida.strftime("%Y-%m-%d %H:%M:%S") if r.hora_salida else "",
            "costo": r.costo if r.costo else 0
        })
    return jsonify(data)


if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # Crea la tabla si no existe
    app.run(debug=True)

    

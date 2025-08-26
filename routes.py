from flask import Blueprint, request, jsonify
from controllers import registrar_entrada, registrar_salida, obtener_total_dia

routes = Blueprint("routes", __name__)

@routes.route("/entrada", methods=["POST"])
def entrada():
    data = request.json
    registro = registrar_entrada(data["placa"])
    return jsonify({"mensaje": "Entrada registrada", "placa": registro.placa})

@routes.route("/salida", methods=["POST"])
def salida():
    data = request.json
    registro = registrar_salida(data["placa"])
    if not registro:
        return jsonify({"error": "Vehículo no encontrado"}), 404
    return jsonify({
        "mensaje": "Salida registrada",
        "placa": registro.placa,
        "costo": registro.costo
    })

@routes.route("/reporte", methods=["GET"])
def reporte():
    total, registros = obtener_total_dia()
    return jsonify({
        "total_dia": total,
        "registros": [
            {"placa": r.placa, "entrada": r.hora_entrada, "salida": r.hora_salida, "costo": r.costo}
            for r in registros
        ]
    })

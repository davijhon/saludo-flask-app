from flask import Flask, request, jsonify, make_response, current_app
from flask_sqlalchemy import SQLAlchemy
from decouple import config


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = (
    "postgresql://{user}:{passwd}@{host}:{port}/{db}".format(
        user=config("POSTGRES_USER"),
        passwd=config("POSTGRES_PASSWORD"),
        host=config("DB_HOST"),
        port=config("DB_PORT"),
        db=config("POSTGRES_DB"),
    )
)
db = SQLAlchemy()
db.init_app(app)
app.app_context().push()


class Saludo(db.Model):
    __tablename__ = "saludos"

    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String(120), nullable=False)

    def json(self):
        return {"id": self.id, "message": self.message}


db.create_all()


# Crear saludos
@app.route("/saludos", methods=["POST"])
def create_saludo():
    try:
        data = request.get_json()
        new_saludo = Saludo(message=data["message"])
        db.session.add(new_saludo)
        db.session.commit()
        return make_response(jsonify({"message": "Saludo creado exitosamente"}), 201)
    except Exception as e:
        return make_response(
            jsonify({"message": "Error al crear el saludo", "error": str(e)}), 500
        )


# Listar saludos
@app.route("/saludos", methods=["GET"])
def get_saludos():
    try:
        saludos = Saludo.query.all()
        return make_response(jsonify([saludo.json() for saludo in saludos]), 200)
    except Exception as e:
        return make_response(
            jsonify({"message": "Error al obtener los saludos", "error": str(e)}), 500
        )


# Traer un "saludo" por id
@app.route("/saludos/<int:id>", methods=["GET"])
def get_saludo(id):
    try:
        saludo = Saludo.query.filter_by(id=id).first()
        if saludo:
            return make_response(jsonify({"greeting": saludo.json()}), 200)
        return make_response(jsonify({"message": "Saludo no encontrado."}), 404)
    except Exception as e:
        return make_response(
            jsonify({"message": "Error al obtener el saludo", "error": str(e)}), 500
        )

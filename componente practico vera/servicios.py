import json
import os

from app.models import Estudiante


class GestorEstudiantes:
    def __init__(self, ruta_archivo):
        self.ruta = ruta_archivo
        os.makedirs(os.path.dirname(ruta_archivo), exist_ok=True)
        if not os.path.exists(ruta_archivo):
            with open(ruta_archivo, "w", encoding="utf-8") as archivo:
                json.dump([], archivo, ensure_ascii=False, indent=2)

    def cargar(self):
        with open(self.ruta, "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)
        return datos

    def guardar(self, estudiantes):
        with open(self.ruta, "w", encoding="utf-8") as archivo:
            json.dump(estudiantes, archivo, ensure_ascii=False, indent=2)

    def crear(self, nombre, carnet, email):
        datos = self.cargar()

        if not nombre or not carnet or not email:
            return False, "Todos los campos son obligatorios."

        for estudiante in datos:
            if estudiante["carnet"] == carnet:
                return False, "Ese carnet ya existe."

        ultimo_id = max((e["id"] for e in datos), default=0)
        nuevo = Estudiante(ultimo_id + 1, nombre, carnet, email)
        datos.append({
            "id": nuevo.id,
            "nombre": nuevo.nombre,
            "carnet": nuevo.carnet,
            "email": nuevo.email,
        })
        self.guardar(datos)
        return True, "Estudiante creado."

    def listar(self):
        datos = self.cargar()
        return [Estudiante(d["id"], d["nombre"], d["carnet"], d["email"]) for d in datos]

    def buscar(self, texto):
        texto = texto.lower()
        datos = self.cargar()
        resultado = []

        for d in datos:
            if texto in d["nombre"].lower() or texto in d["carnet"].lower() or texto in d["email"].lower():
                resultado.append(Estudiante(d["id"], d["nombre"], d["carnet"], d["email"]))

        return resultado

    def actualizar(self, id, nombre=None, carnet=None, email=None):
        datos = self.cargar()
        for d in datos:
            if d["id"] == id:
                if nombre:
                    d["nombre"] = nombre
                if carnet:
                    d["carnet"] = carnet
                if email:
                    d["email"] = email
                self.guardar(datos)
                return True, "Estudiante actualizado."
        return False, "No existe ese estudiante."

    def eliminar(self, id):
        datos = self.cargar()
        lista_nueva = [d for d in datos if d["id"] != id]

        if len(lista_nueva) == len(datos):
            return False, "No existe ese estudiante."

        self.guardar(lista_nueva)
        return True, "Estudiante eliminado."

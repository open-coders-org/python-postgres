from hospital import Hospital as h
from db.db import db

from Crud import Crud


class CrudHospital(Crud):
    connection = db()
    cursor = connection.cursor()

    def crear(self, **kwargs):
        super().crear(**kwargs)
        hospital_name = kwargs.get("hospital_name")
        self.cursor.execute(
            "INSERT INTO hospital (hospital_name) values(%s)", (hospital_name,)
        )
        self.connection.commit()

    def mostrar(self, **kwargs):
        super().mostrar(**kwargs)
        self.cursor.execute("SELECT * FROM hospital")
        rows = self.cursor.fetchall()
        return rows

    def eliminar(self, **kwargs):
        pass

    def mostrarId(self, **kwargs):
        super().mostrar(**kwargs)
        hospital_id = kwargs.get("hospital_id")
        self.cursor.execute(
            "SELECT hospital_name FROM hospital where hospital_id = %s ", (hospital_id)
        )
        rows = self.cursor.fetchone()
        return rows

    def editar(self, **kwargs):
        super().editar(**kwargs)
        hospital_id = kwargs.get("hospital_id")
        hospital_name = kwargs.get("hospital_name")
        self.cursor.execute(
            "UPDATE hospital SET hospital_name = %s WHERE hospital_id = %s",
            (hospital_name, hospital_id),
        )
        self.connection.commit()

    def eliminar(self, **kwargs):
        super().eliminar(**kwargs)
        hospital_id = kwargs.get("hospital_id")
        self.cursor.execute(
            "DELETE FROM hospital WHERE hospital_id = %s", (hospital_id)
        )
        self.connection.commit()

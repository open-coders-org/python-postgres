from hospital import Hospital as h
from db.db import db

from Crud import Crud


class CrudDoctor(Crud):
    connection = db()
    cursor = connection.cursor()

    def crear(self, **kwargs):
        super().crear(**kwargs)
        doctor_name = kwargs.get("doctor_name")
        e_doctor = kwargs.get("speciality")
        hospital_id = kwargs.get("hospital_id")
        self.cursor.execute(
            "INSERT INTO doctor (doctor_name , speciality , hospital_id) values(%s,%s,%s)",
            (doctor_name, e_doctor, hospital_id),
        )
        self.connection.commit()

    def mostrar(self, **kwargs):
        super().mostrar(**kwargs)
        self.cursor.execute(
            "SELECT doctor.doctor_name, doctor.speciality, hospital.hospital_name FROM hospital INNER JOIN doctor ON hospital.hospital_id = doctor.hospital_id"
        )
        rows = self.cursor.fetchall()
        return rows

    def eliminar(self, **kwargs):
        pass

    def mostrarId(self, **kwargs):
        pass

    def editar(self, **kwargs):
        super().editar(**kwargs)
        doctor_name = kwargs.get("doctor_name")
        e_doctor = kwargs.get("speciality")
        hospital_id = kwargs.get("hospital_id")
        id_doctor = kwargs.get("id_doctor")
        self.cursor.execute(
            "UPDATE doctor SET doctor_name = %s, speciality = %s , hospital_id = %s WHERE doctor_id = %s",
            (doctor_name, e_doctor, hospital_id, id_doctor),
        )
        self.connection.commit()

    def eliminar(self, **kwargs):
        super().eliminar(**kwargs)
        id_doctor = kwargs.get("id_doctor")
        self.cursor.execute("DELETE FROM doctor WHERE doctor_id = %s", (id_doctor))
        self.connection.commit()

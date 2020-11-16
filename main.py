from CrudHospital import CrudHospital
from CrudDoctor import CrudDoctor

import argparse

parser = argparse.ArgumentParser("CRUD")

parser.add_argument("-c", "--comando", help="Is a command for create doctor")
parser.add_argument("-nh", "--nombrehospital", help="Name hospital")
parser.add_argument("-esp", "--especial", help="Especializacion del doctor")
parser.add_argument("-ho", "--hospital", help="Hospital al que pertenece el doctor")
parser.add_argument("-nd", "--nombredoctor", help="Name doctor")
parser.add_argument("-id", "--idoctor", help="Id doctor")
parser.add_argument("-ih", "--ihospital", help="Id hospital")

args = parser.parse_args()
name_hospital = args.nombrehospital
command = args.comando
name_doctor = args.nombredoctor
hospital = args.hospital
especial = args.especial
idoctor = args.idoctor
ihospital = args.ihospital

if __name__ == "__main__":
    crudhospital = CrudHospital()
    cruddoctor = CrudDoctor()
    if command == "crearh":
        if name_hospital:
            print(name_hospital)
            crudhospital.crear(hospital_name=name_hospital)
        else:
            print("No ha ingresado el nombre, verifique por favor")
    elif command == "mostrarh":
        rows = crudhospital.mostrar()
        for row in rows:
            print(row)
    elif command == "editarh":
        if ihospital and name_hospital:
            crudhospital.editar(hospital_id=ihospital, hospital_name=name_hospital)
        else:
            print("Faltan datos por favor ingresarlos")

    elif command == "eliminarh":
        if ihospital:
            crudhospital.eliminar(hospital_id=ihospital)
        else:
            print("Faltan datos por favor ingresarlos")
    elif command == "creard":
        if name_doctor and hospital and especial:
            cruddoctor.crear(
                doctor_name=name_doctor, speciality=especial, hospital_id=hospital
            )
        else:
            print("Faltan campos por llenar")
    elif command == "mostrard":
        rows = cruddoctor.mostrar()
        for row in rows:
            print(f"Nombre: {row[0]}")
            print(f"Especializacion: {row[1]}")
            print(f"Hospital al que pertenece: {row[2]}")
    elif command == "editard":
        if name_doctor and hospital and especial and idoctor:
            cruddoctor.editar(
                doctor_name=name_doctor,
                spectiality=especial,
                hospital_id=hospital,
                id_doctor=idoctor,
            )
        else:
            print("Debe ingresar todos los campos: ")
    elif command == "eliminard":
        if idoctor:
            cruddoctor.eliminar(id_doctor=idoctor)
        else:
            print("Faltan datos todavía, por favor ingresar bien el id")

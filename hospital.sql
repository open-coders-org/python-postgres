create database H;

create table hospital(

	hospital_id SERIAL PRIMARY KEY,
	hospital_name VARCHAR(100)


);

create table doctor(

	doctor_id  SERIAL PRIMARY KEY,
	doctor_name VARCHAR(100),
	speciality VARCHAR(100)

);

-- relaciones
alter table doctor
add hospital_id integer not null;
alter table doctor
add foreign key (hospital_id) references hospital(hospital_id)

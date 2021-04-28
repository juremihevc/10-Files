import json

with open("DNA_characteristics.json", "r") as DNA_car_file:
    DNA_car_list = json.loads(DNA_car_file.read())

with open("Suspects_characteristics.json", "r") as Suspects_car_file:
    Suspects_car_list = json.loads(Suspects_car_file.read())

with open("dna.txt", "r") as dna_file:
    dna_link = dna_file.read()

suspect_car = []

gender = DNA_car_list["Gender"]
for i in gender:
    if gender[i] in dna_link:
        suspect_car.append(i)

race = DNA_car_list["Race"]
for i in race:
    if race[i] in dna_link:
        suspect_car.append(i)

hair = DNA_car_list["Hair_color"]
for i in hair:
    if hair[i] in dna_link:
        suspect_car.append(i)

eye = DNA_car_list["Eye_color"]
for i in eye:
    if eye[i] in dna_link:
        suspect_car.append(i)

face = DNA_car_list["Facial_shape"]
for i in face:
    if face[i] in dna_link:
        suspect_car.append(i)

Names = {}

Eva = list(Suspects_car_list["Eva"].values())
Names["Eva"] = Eva

Larisa = list(Suspects_car_list["Larisa"].values())
Names["Larisa"] = Larisa

Matej = list(Suspects_car_list["Matej"].values())
Names["Matej"] = Matej

Miha = list(Suspects_car_list["Miha"].values())
Names["Miha"] = Miha

for name in Names:
    if Names[name] == suspect_car:
        print(f"{name} ate the icecream!")
        break



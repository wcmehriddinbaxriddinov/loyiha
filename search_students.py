
with open("students.txt", "r") as f:
    id = input("ID kiriting: ")

    for qator in f:
        malumot = qator.split()

        if malumot[0] == id:
            print(qator)
        else:
            print("bunday id mavjud emas!")

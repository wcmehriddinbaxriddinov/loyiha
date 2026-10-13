id = input("Student ID: ")
ism = input("Student ismi: ")

with open("students.txt", "a") as file:
    file.write(f"{id} {ism}\n")

print("Student muvaffaqiyatli qo'shildi!")

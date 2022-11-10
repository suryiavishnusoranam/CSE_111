student1 = {
    "age":20,
    "name": "Fred",
    "phone_number": "3333333",
}
student2 = {
    "age":30,
    "name": "Jenny",
    "phone_number": "777777",
}

print("The namne of student is " + student1['name'])

student_list = [
    student1, student2
]
print(student_list)

total_age = 0
# while (i <  len(student_list)): #same
#     print(student_list[i])
#     i += 1

# for student in student_list: #same
#     total_age += student['age']

average_age = total_age / len(student_list)
#print(average_age)

student_names = ["Jed", "Jen", "Sandy"]

# print(student_names[0],student_names[1])

i = len(student_names) - 1
while (i >= 0):
    print(student_names[i])
    i -= 1
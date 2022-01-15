f=open('classbook.txt','r')
content=f.read()
f.close()

content = content.split("\n")
pupils=[]

for line in content:
    line = line.split(" ")
    pupils.append([line[0], line[1], int(line[2])])
    srednia=0

print("Ниже трех баллов:")

for p in pupils:
    srednia+=int(p[2])

    if p[2] < 3:
        print(f"{p[0]} {p[1]}: {p[2]}")
        srednia /= len(pupils)

        print(f"Средняя оценка по классу: {srednia}")


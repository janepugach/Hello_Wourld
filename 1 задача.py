from random import randint

a = []
for i in range(10):
   a.append(randint(0, 10))
print(a)

for i in range(len(a)):
   for j in range(len(a)):
       if i != j and a[i] == a[j]:
           break
   else:
       print(a[i], end=' ')
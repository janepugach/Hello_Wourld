# a = [int(s) for s in input().split()]
# counter = 0
# for i in range(len(a)):
#     for j in range(i + 1, len(a)):
#         if a[i] == a[j]:
#             counter += 1
# print(counter)

L = map(int, input().split())

obj = { }
for k in L:
    obj[k] = obj.get(k, 0) + 1

count = 0
for n in obj.values():
    count += (n - 1) * n / 2

print( int(count) )
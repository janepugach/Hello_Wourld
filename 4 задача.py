my_string = 'An apple a day keeps the doctor away'
my_dict = {i: my_string.count(i) for i in my_string}
print(my_dict)
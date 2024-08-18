def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params(b=25)
print_params(c = [1,2,3])
print_params()
print_params(65, {3, 4}, (),)
print_params(65, {3})
print_params(65)

value_list = [3.14, 1 + 1j, 0]
value_dict = {'a': 4, 'b': False, 'c': '\\'}

print_params(*value_list)
print_params(**value_dict)

value_list_2 = [1j, 2.7]
print_params(*value_list_2, 42)
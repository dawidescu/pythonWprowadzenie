eng2esp = dict()
print(eng2esp)

eng2esp ["one"] = "uno"
print(eng2esp)

eng2esp = {'one' : 'uno', 'two' : 'dos', 'three' : 'tres'}
print(eng2esp)

print(eng2esp['two'])

print(len(eng2esp))

hello ='one' in eng2esp
print(hello)

"""Aby sprawdzić, czy coś pojawia się w słowniku jako wartość, możesz użyć metody values(), zwracającą
wartości jako typ, który może być skonwertowany na listę, a następnie użyć operatora in:"""
vals = list(eng2esp.values())
print('uno' in vals)


"""
Ćwiczenie 1. Napisz funkcję o nazwie chop(), która przyjmuje listę i modyfikuje ją, usuwając z niej
pierwszy i ostatni element; funkcja ma zwracać None. Następnie napisz funkcję o nazwie middle(), która
przyjmuje listę i zwraca nową listę, która zawiera wszystkie elementy wejściowej listy za wyjątkiem
pierwszego i ostatniego elementu.
"""

def chop(t):
    t.pop(0)
    t.pop(-1)



my_list = [1, 2, 3, 4, 5]
#chop(my_list)   --- 1 part of assignment
#print(my_list)


def middle(t):
    return t[1:-1]

my_new_list = middle(my_list)
print(my_new_list)

"""More info: 
https://docs.python.org/3/library/stdtypes.html#common-sequence-operations
https://docs.python.org/library/stdtypes.html#mutable-sequence-types
"""


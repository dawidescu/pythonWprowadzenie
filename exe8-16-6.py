"""
Ćwiczenie 6. Napisz ponownie program, który poprosi użytkownika o listę liczb, natomiast gdy
użytkownik wpisze “gotowe”, wypisze na końcu największą i najmniejszą z nich. Napisz program w ten
sposób, że zapisze on wprowadzone przez użytkownika liczby na liście i użyje funkcji max() oraz min() do
znalezienia największej i najmniejszej liczby po zakończeniu pętli.
Wprowad ź liczb ę : 6
Wprowad ź liczb ę : 2
Wprowad ź liczb ę : 9
Wprowad ź liczb ę : 3
Wprowad ź liczb ę : 5
Wprowad ź liczb ę : gotowe
Najwi ę ksza : 9.0
Najmniejsza : 2.0
"""

"""users_number = input("Wpisz pan liczbę: \n")
users_list = []
while True:
    line = users_number.append
    #print(line)
    #users_list.append(line)
    if users_number == "gotowe":
        break

print("Wykonało sie!")"""


def mini_maxi():
    users_list = []

    while True:
        users_number = input("Wpisz pan liczbę!: \n")
        if users_number == "gotowe":
            break

        try:
            users_list.append(float(users_number))
        except ValueError:
            print("Liczbę, bracie, liczbę! ")


    print("Najwieksza: ", max(users_list))
    print("Najmniejsza: ", min(users_list))

mini_maxi()


"""Ćwiczenie 1. Pobierz kopię pliku https://py4e.pl/code3/words.txt
Napisz program, który odczytuje słowa z words.txt i przechowuje je jako klucze w słowniku. Nie ma
znaczenia, jakie będą wartości w słowniku. Następnie możesz użyć operatora in jako szybkiego sposobu
na sprawdzenie, czy dany wyraz znajduje się w słowniku"""



with open('words.txt') as words:
    words = {k: 1 for line in words for(k) in line.strip().split(None, 1)}

print('Pisanie' in words)
print(words)

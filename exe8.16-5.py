"""
Ćwiczenie 5. Napisz program, który czyta dane mailowe z pliku w formacie Mbox, a gdy znajdzie
wiersz zaczynający się od “From”, niech podzieli go na słowa, korzystając z metody split(). Interesuje
nas, kto wysłał wiadomość – informacja ta jest drugim słowem w wierszu zawierającym “From”.
From stephen . marquard@uct . ac . za Sat Jan 5 09:14:16 2008
Musisz przeparsować linię zawierającą “From” i wyświetlić drugie słowo dla każdej takiej linii. Następnie
musisz zliczyć liczbę wierszy “From” (nie “From:”) i na końcu wyświetlić tę liczbę. Poniżej znajduje się
przykładowe poprawne wyjście (część linii wyjścia została usunięta):
Podaj nazw ę pliku : mbox - short . txt
stephen . marquard@uct . ac . za
louis@media . berkeley . edu
zqian@umich . edu
[... cz ę ś ć linii wyj ś cia usuni ę ta ...]
ray@media . berkeley . edu
cwen@iupui . edu
cwen@iupui . edu
cwen@iupui . edu
Mamy 27 linii , w kt ó rych From jest pierwszym wyrazem
"""


my_file = open("mbox-short.txt")
count = 0
for line in my_file:
    line = line.rstrip()
    if line.startswith("From "):
        name = line.split()
        print(name[1])
        count += 1
print(f"There is {count} names where the line strats from From from from From from...")


"""rows = len(name)
print(rows)"""


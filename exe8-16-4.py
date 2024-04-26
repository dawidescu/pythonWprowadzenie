"""
Ćwiczenie 4. Pobierz kopię pliku https://py4e.pl/code3/romeo.txt. Napisz program, który będzie
przechowywał listę wyrazów występujących w pliku. Na początku otwórz plik romeo.txt i czytaj go linia
po linii. Każdą z nich podziel na listę słów za pomocą metody split(). Dla każdego słowa sprawdź, czy
znajduje się ono już na liście. Jeśli go nie ma, to dodaj je do listy. Gdy program zakończy pracę, posortuj
i wypisz wynikowe słowa w kolejności alfabetycznej.
Podaj nazw ę pliku : romeo . txt
['Arise ', 'But ', 'It ', 'Juliet ', 'Who ', 'already ',
"""
romek = open("romeo.txt")
#plik = romek.read()
romek_full = []

for line in romek:
    words = line.split()
    romek_full.extend(words)
    # trzeba zrobic, zeby to byla nowa lista i return

romek_sorted = sorted(romek_full, key=str.lower)
print(romek_sorted)


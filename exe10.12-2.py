"""Ćwiczenie 2. Napisz program, który zlicza rozkład godzin dla wszystkich wiadomości mailowych.
Możesz wyodrębnić godzinę z linii zaczynających się od “From” (są to napisy związane z czasem do
przeanalizowania), a następnie dzieląc tę linię na części za pomocą znaku dwukropka. Gdy już zgromadzisz
wartości dla każdej godziny, wypisz zliczenia, po jednym na wiersz, posortowane według godzin, tak jak
pokazano poniżej.
Podaj nazw ę pliku : mbox - short . txt
04 3
06 1
07 1
09 2
10 3
11 6
14 1
15 2
16 4
17 2
18 1
19 1"""
import string

fname = input('Podaj nazwę pliku :')
try:
    fhand = open(fname)
except :
    print('Nie można otworzyć pliku :', fname)
    exit()
counts = dict()
for line in fhand:
    line = line.lower()
    # line = line.translate(str.maketrans('', '', string.punctuation))
    words = line.split()
    if line.startswith('from '):
        if len(words) >=3:
            hour = words[5]
            full_hour = hour.split(':')[0]
            counts[full_hour] = counts.get(full_hour, 0) + 1
        else:
            print("Buuuu!")

# filename : mbox-short.txt

hour_disposition = list()

for val, key in counts.items():
    hour_disposition.append((val, key))

hour_disposition.sort()

for key, val in hour_disposition:
    print(key, val)


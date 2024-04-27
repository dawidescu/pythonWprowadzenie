"""
Ćwiczenie 2. Napisz program, który każdą wiadomość mailową (zapisaną w pliku w formacie Mbox)
skategoryzowałby według dni tygodnia. Aby to zrobić, poszukaj wierszy rozpoczynających się od “From”,
a następnie poszukaj trzeciego słowa i zachowaj bieżące zliczenia dla każdego dnia. Na koniec programu
wyświetl zawartość swojego słownika (kolejność nie ma znaczenia).
Przykładowa linia:
From stephen . marquard@uct . ac . za Sat Jan 5 09:14:16 2008
Przykładowe uruchomienie:
Podaj nazw ę pliku : mbox - short . txt
{'Sat ': 1 , 'Fri ': 20 , 'Thu ': 6}
"""
# c

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
    words = line.split()
    if line.startswith('from '):
        if len(words) >= 3:
            counts[words[2]] = counts.get(words[2], 0) + 1
        else:
            print("Buuuu!")
    #print(counts)



print(counts)

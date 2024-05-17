"""
Ćwiczenie 1. Przepisz swój poprzedni program zliczający wysłane wiadomości mailowe w następujący
sposób. Wczytaj i przetwórz linie zaczynające się od “From” oraz wyodrębnij z nich adresy mailowe. Za
pomocą słownika, dla każdej osoby zapisz liczbę wysłanych przez nią wiadomości.
Po przeczytaniu wszystkich danych utwórz ze słownika listę krotek w postaci (liczba, adres e-mail).
Następnie posortuj listę w odwrotnej kolejności i wypisz osobę, która wysłała najwięcej wiadomości.
Przykładowa linia:
From stephen . marquard@uct . ac . za Sat Jan 5 09:14:16 2008
10.12. Ćwiczenia 105
Przykładowe uruchomienia:
Podaj nazw ę pliku : mbox - short . txt
cwen@iupui . edu 5
Podaj nazw ę pliku : mbox . txt
zqian@umich . edu 195

"""

# filename : mbox-short.txt

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
            counts[words[1]] = counts.get(words[1], 0) + 1
        else:
            print("Buuuu!")
# filename : mbox-short.txt
num_of_mails = list()
for key, val in counts.items():
    num_of_mails.append((val, key))
num_of_mails.sort(reverse=True)

for key, val in num_of_mails[:1]:
    print(key, val)

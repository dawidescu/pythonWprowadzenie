"""
Ćwiczenie 4. Do powyższego programu dodaj kod, tak by dowiedzieć się, kto wysłał najwięcej e￾maili. Po przeczytaniu wszystkich danych i utworzeniu słownika, przeszukaj tej osoby za pomocą pętli
wyszukującej największą wartość (patrz: rozdział 5, sekcja “Pętle typu maksimum i minimum”). Na
koniec programu wyświetl informację dotyczącą adresu mailowego i liczbie wysłanych wiadomości.
Podaj nazw ę pliku : mbox - short . txt
cwen@iupui . edu 5
Podaj nazw ę pliku : mbox . txt
zqian@umich . edu 195
"""

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

most_msg = max(counts.values())
most_key = [key for key, value in counts.items() if value == most_msg]
print(f"The most messages comes from: {most_key}: {most_msg}")
least_msg = min(counts.values())
least_key = [key for key, value in counts.items() if value == least_msg]
print(f"The least messages comes from: {least_key}: {least_msg}")
# file-name: mbox-short.txt


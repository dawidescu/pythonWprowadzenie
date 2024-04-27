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

word = ' brontosaurus '
d = dict()
for c in word :
    if c not in d :
        d[c] = 1
    else:
        d[c] = d[c] + 1
print(d)

### --- Powyższą pętlę możemy napisać w sposób bardziej zwięzły.
### --- Użyjemy do tego metody .get()

"""Słowniki posiadają metodę get(), która przyjmuje klucz i domyślną wartość. Jeśli klucz pojawia się w
słowniku, get() zwraca odpowiednią wartość; w przeciwnym razie zwraca wartość domyślną"""

word = ' brontosaurus '
d = dict()
for c in word:
    d[c] = d.get(c, 0) + 1
print(d)

# zwróć uwagę na spacje

""" Napiszemy program, który odczyta wiersze pliku, rozbijemy każdy wiersz na listę słów,
a następnie przejdziemy w pętli przez każde słowo zawarte w linii i za pomocą słownika policzymy
wystąpienia każdego słowa."""

import string

fname = input('Podaj nazwę pliku :')
try:
    fhand = open(fname)
except :
    print('Nie można otworzyć pliku :', fname)
    exit()
counts = dict()
for line in fhand:
    # tutaj dodaje metody na pozbycie sie znaków interpunkcyjnych
    line = line.translate(str.maketrans('', '', string.punctuation))
    line = line.lower()
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1
print(counts)


"""
Ćwiczenie 3. Napisz program, który wczytuje plik i wypisuje litery malejąco po częstości ich wy￾stępowania. Twój program powinien przekonwertować wszystkie dane wejściowe na małe litery i zli￾czać tylko litery a-z. Program nie powinien uwzględniać spacji, cyfr, interpunkcji ani niczego innego
poza literami a-z. Znajdź próbki tekstów z kilku różnych języków i sprawdź, jak bardzo częstość wy￾stępowania liter różni się w zależności od języka. Porównaj swoje wyniki z tabelami pod adresem
https://en.wikipedia.org/wiki/Letter_frequency.
"""
import string

fname = input('Podaj nazwę pliku : ')
try:
    fhand = open(fname)
except :
    print('Nie można otworzyć pliku :', fname)
    exit()
counts = dict()
for line in fhand:
    line = line.lower()
    line = line.strip()
    line = line.translate(str.maketrans('', '', string.punctuation))
    line_no_dig = line.translate(str.maketrans('', '', string.digits))
    words = line_no_dig.split()
    # print(type(words)) #list
    # print(type(line))  #string
    words[:] = line_no_dig

    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1


characters = [ (v, k) for k, v in counts.items()]

characters.sort()

for key, val in characters:
    print(val, key)


# filename : mbox-short.txt




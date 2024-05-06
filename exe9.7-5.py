"""
Ćwiczenie 5. Napisz program zapamiętujący nazwę domeny, z której została wysłana wiadomość
(zamiast informacji, od kogo pochodziła wiadomość, tzn. całego adresu e-mail). Na koniec programu
wyświetl zawartość słownika.
Podaj nazw ę pliku : mbox - short . txt
{' uct . ac . za ': 6 , 'media . berkeley . edu ': 4 , 'umich . edu ': 7 ,
'iupui . edu ': 8 , 'caret . cam . ac . uk ': 1 , 'gmail . com ': 1}
"""
import string

    # filename : mbox-short.txt

"""def make_trans(counts):
    x = "@"
    y = " "
    email = str.maketrans(x, y)
    return counts.maketrans(email)"""

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
        if len(words) >= 3:
            email = words[1]
            domain = email.split('@')[1]
            counts[domain] = counts.get(domain, 0) + 1
        else:
            print("Buuuu!")

print(counts)

"""
Ćwiczenie 3. Napisz program, który odczytuje dane z pliku w formacie Mbox i przy pomocy słownika
tworzy histogram. Chcemy zliczyć, ile wiadomości przyszło z każdego adresu e-mail. Jako wynik działania
programu ma zostać wyświetlony utworzony słownik.
Podaj nazw ę pliku : mbox - short . txt
{' stephen . marquard@uct . ac . za ': 2 , 'louis@media . berkeley . edu ': 3 ,
' zqian@umich . edu ': 4 , ' rjlowe@iupui . edu ': 2 , 'cwen@iupui . edu ': 5 ,
' gsilver@umich . edu ': 3 , ' wagnermr@iupui . edu ': 1 ,
' antranig@caret . cam . ac . uk ': 1 , 'gopal . ramasammycook@gmail . com ': 1 ,
'david . horwitz@uct . ac . za ': 4 , 'ray@media . berkeley . edu ': 1}
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
    words = line.split()  # w odróżnieniu od poprzedniego (972) tutaj mamy split() a nie strip().


    if line.startswith('from '):
        if len(words) >= 3:
            counts[words[1]] = counts.get(words[1], 0) + 1
        else:
            print("Buuuu!")


# file-name: mbox-short.txt
print(counts)


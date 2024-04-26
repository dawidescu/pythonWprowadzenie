"""Ćwiczenie 2. Sprawdź, która linia powyższego programu nie jest jeszcze właściwie zabezpieczona.
Skonstruuj taki plik tekstowy, który wysypie program, a następnie zmodyfikuj program tak, by był on
odpowiednio zabezpieczony. Przetestuj poprawiony program, by upewnić się, że obsługuje Twój nowy
plik tekstowy."""

fhand = open('mbox-short.txt')
for line in fhand:
    words = line.split()
    #print('Debug:', words)
    #if len(words) == 0: continue
    #if words[0] != 'From': continue
    if len(words) == 0 and words[0] != "From": continue
    print(words[2])

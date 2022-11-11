import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())

d = {'e' : 1, 'a' : 1, 'i' : 1, 'o' : 1, 'n' : 1, 'r' : 1, 't' : 1, 'l' : 1,\
's' : 1, 'u' : 1, 'd' : 2, 'g' : 2, 'b' : 3, 'c' : 3, 'm' : 3, 'p' : 3,\
'f' : 4, 'h' : 4, 'v' : 4, 'w' : 4, 'y' : 4, 'k' : 5, 'j' : 8, 'x' : 8,\
'q' : 10, 'z' : 10}

mots = []
for i in range(n):
    w = input()
    w = list(w.strip())
    mots.append(w)

letters = input()
letters = list(letters.strip())

tirage = ""
motFinal = ""
somme = 0
sommeMax = 0

for mot in mots:
    tirage = list(letters)

    cpt = 0
    for i in range(len(mot)):
        if mot[i] in tirage:
            tirage.remove(mot[i])
            cpt+=1
        else:
            break

    if len(mot) == cpt:
        for i in mot:
            somme = somme + d[i]
        if somme > sommeMax:
            sommeMax = somme
            motFinal = mot
    somme = 0

print("".join(motFinal))

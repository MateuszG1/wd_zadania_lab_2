import sys as system
import math
#zad1

sporty = ['plywanie', 'pilka nozna', 'siatkowka']
sporty.reverse()
sporty.append('koszykowa')
sporty.append('hokej')
print(sporty)



#zad2
slownik = {'zakazenie': 'wniknięcie i rozwój w organizmie żywym biologicznego czynnika chorobotwórczego', 'epidemia':  'wystąpienie u ludzi zachorowań na określoną chorobę w określonym czasie i na określonym terenie w liczbie przypadków większej niż przeciętnie'}
print(slownik)



#zad3
gry = {'CS': 'wieloosobowa strzelanka pierwszoosobowa, stworzona oraz wydana przez Valve Corporation i Hidden Path Entertainment, które już wcześniej pracowały nad Counter-Strike: Source', 'Minecraft': ' komputerowa gra survivalowa o otwartym świecie stworzona przez Markusa Perssona i rozwijana przez Mojang Studios'}
print(len(gry))



#zad4
zdanie = input('Podaj zdanie: ')
print(zdanie.count('a'))



#zad5
system.stdout.write('Podaj liczbe a: ')
a = system.stdin.readline()
system.stdout.write('Podaj liczbe b: ')
b = system.stdin.readline()
system.stdout.write('Podaj liczbe c: ')
c = system.stdin.readline()
wynik = int(a)**int(b)+int(c)
system.stdout.write(str(wynik))



#zad6
a = input('Podaj liczne a: ')
a = int(a)
b = input('Podaj liczne b: ')
b = int(b)
c = input('Podaj liczne c: ')
c = int(c)

if(a > b) & (a > c):
    print('Liczba a jest najwieksza')
elif(b > a) & (c > b):
    print('Liczba c jest najwieksza')
else:
    print('Liczba b jest najwieksza')



#zad7
lista = [5, 6, 3, 2.5, 1.5]
do_kwadratu = []
x = 0
for x in lista:
    do_kwadratu.append(x**2)
print(do_kwadratuz)



#zad8
parzyste = []
z = 0
while z != 10:
    liczba = input('Podaj liczbe: \n')
    liczba = int(liczba)
    z += 1
    if liczba%2 == 0:
        parzyste.append(liczba)
print(parzyste)



#zad9
lista2 = [1, 2, 3, 4, 5]
for i in lista2:
    if i%2 == 0:
        print('E')
    else:
        print('E'*6)



#zad10
liczba = input('Podaj liczbe:')
liczba = float(liczba)
try:
    if liczba < 0:
        raise ValueError
    else:
        print(math.sqrt(liczba))
except ValueError:
    print('Liczba mniejsza od zera')
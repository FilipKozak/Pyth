import random

l = []

print(" Witaj w generatorze SZCZEPANIAKA \n", "Postępuj zgodnie z poleceniami i wylosuj wybrańca\n", "Z każdym zapytaniem programu podaj tylko jednego uczestnika\n")
while True:
    uczestnicy = str(input('Podaj imiona uczestników. Jeżeli dodałeś już wszystkich wpisz end: '))
    if 'end' in uczestnicy:
        break
    else:
        print("Udział biorą: "),l.append(uczestnicy)
        print(l)

uczestnik = random.choice(l)
print("Dla Szczepana prezkę robi: \n",uczestnik, "\n", "Gratulacje dla chętnego!!!\n", "Powodzenia :D\n")

input ("Wcisnij Enter aby wyjść :)")

# Trouver la somme de deux nombres entiers
nbr1 = input('Entrez le premier nombre: ')
nbr2 = input('Entrez le deuxième nombre: ')

# Additionner les deux nombres 
s = int(nbr1) + int(nbr2)
# Multiplication
m=int(nbr1) * int(nbr2)
# Division
d=int(nbr1) / int(nbr2)

# Afficher la somme
print('La somme de {0} et  {1} est {2}'.format(nbr1, nbr2, s))

# Afficher la multiplication
print('La multiplication de {0} et  {1} est {2}'.format(nbr1, nbr2, m))

# Afficher la divison avec erreur pour testet le CI
print('La multiplication de {0} et  {1} est {2}'.format(nbr1, nbr2, d))
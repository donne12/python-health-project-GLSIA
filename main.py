from fonction import *
print("===== Bienvenu dans le programme de cardiologie ====== ")
print("Taper 1 pour gerer les categories de maladie")
print("Taper 2 pour gerer les maladies")
print("Taper 3 pour gerer les Traitements des maladies")
print("Taper 4 pour gerer les Patients")
print("Taper 0 pour sortir du programme")
choix = str(input("Quelle est votre choix : "))
dico = {
	"0": exit,
	"1": gererCategorieMaladie,
	"2": gererMaladies,
	"3": gererTraitementsMaladies,
	"4": gererPatients
}
dico[choix]()
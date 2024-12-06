import csv
import matplotlib.pyplot as plt


donnees_2008 = []
with open('donnees_2008.csv', mode='r', encoding='utf-8') as fichier:
    lecteur = csv.reader(fichier)
    next(lecteur) #saut de la premiere ligne  
    for ligne in lecteur:
        donnees_2008.append({
            "Commune": ligne[6],  
            "Population": int(ligne[9]),  
            "Année": "2008"
        })

donnees_2016= []
with open('donnees_2016.csv', mode='r', encoding='utf-8') as fichier:
    lecteur = csv.reader(fichier)
    next(lecteur) #saut de la premiere ligne  
    for ligne in lecteur:
            donnees_2016.append({
            "Commune": ligne[6],  
            "Population": int(ligne[9]),  
            "Année": "2016"
        })


communes = ["Appoigny", "Auxerre", "Monéteau", "Cerizy", "Caen","Lizy"]
communes2 = ["Appoigny", "Auxerre", "Monéteau", "Cerizy", "Caen","Lizy"]

donnees_2008_filtrees = [ligne for ligne in donnees_2008 if ligne["Commune"] in communes]
donnees_2008_filtrees_triees = sorted(donnees_2008_filtrees, key=lambda x: x["Commune"]) #tri des données par ordre alphabetique 

donnees_2016_filtrees = [ligne for ligne in donnees_2016 if ligne["Commune"] in communes2]
donnees_2016_triees = sorted(donnees_2016_filtrees, key=lambda x: x["Commune"]) #tri des données par ordre alphabetique 


print("Données filtrées :")
for ligne in donnees_2008_filtrees_triees:
    print(ligne)

print("Données filtrées 2 :")
for ligne in donnees_2016_triees:
    print(ligne)


def population(donnees_2008, donnees_2016):

    communes_2008 = [ligne["Commune"] for ligne in donnees_2008]
    populations_2008 = [ligne["Population"] for ligne in donnees_2008]

    communes_2016 = [ligne["Commune"] for ligne in donnees_2016]
    populations_2016 = [ligne["Population"] for ligne in donnees_2016]


    plt.plot(communes_2008, populations_2008, marker='o', linestyle='-', color='b', label='2008')
    plt.plot(communes_2016, populations_2016, marker='o', linestyle='-', color='r', label='2016')


    plt.title("Comparaison des populations en 2008 et 2016")
    plt.xlabel("Commune")
    plt.ylabel("Population")
    plt.grid(True)
    plt.xticks(rotation=90) 
    plt.legend()
    plt.show()


population(donnees_2008_filtrees_triees, donnees_2016_triees)
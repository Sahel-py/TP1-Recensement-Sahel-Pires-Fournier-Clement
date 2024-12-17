import csv
import matplotlib.pyplot as plt

donnees = []

with open("RTE_2022.csv", mode="r", encoding="utf-8") as fichier:
    lecteur = csv.reader(fichier)
    header = next(lecteur)  # Saut de la première ligne
    for ligne in lecteur:
        
        consommation = float(ligne[header.index("Consommation")] or 0.0) #Si la donnée est vide ou invalide, elle est remplacée par 0.0.
        nucleaire = float(ligne[header.index("nucleaire")] or 0.0)   #header.index pour retrouver l'index d'un element ici Conso nucleaire et solaire c'est plus simple et rapide
        solaire = float(ligne[header.index("Solaire")] or 0.0)

        donnees.append({
            "Consommation": consommation,
            "nucleaire": nucleaire,
            "Solaire": solaire,
        })

consommation_totale = 0
production_nucleaire = 0
production_solaire = 0

for ligne in donnees:
    consommation_totale += ligne["Consommation"]
    production_nucleaire += ligne["nucleaire"]
    production_solaire += ligne["Solaire"]

print(f"Consommation totale : {consommation_totale} TWh")
print(f"Production nucléaire totale : {production_nucleaire} TWh")
print(f"Production solaire totale : {production_solaire} TWh")


consommation_totale = [ligne["Consommation"] for ligne in donnees]
nucleaire = [ligne["nucleaire"] for ligne in donnees]
solaire = [ligne["Solaire"] for ligne in donnees]



plt.plot(consommation_totale, label="Consommation totale", color="blue")

plt.ylabel("Consommation (TWh)")
plt.title("Consommation totale d'énergie (2022)")
plt.legend()
plt.show()


plt.plot(nucleaire, label="Production nucléaire", color="green")
plt.plot(solaire, label="Production solaire", color="orange")
plt.ylabel("Production (TWh)")
plt.title("Comparaison de la production nucléaire et solaire")
plt.legend()
plt.show()
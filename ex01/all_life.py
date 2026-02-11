from load_csv import load
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator


def main():
    data_frame = load("life_expectancy_years.csv")
    # on place lindex sur les pays
    data_frame.set_index("country", inplace=True)
    # on cible la france.
    france = data_frame.loc["France"]
    # en passant en int, laxe X devient une ligne numerique
    france.index = france.index.astype(int)
    # on prend ces donnees la.
    plt.plot(france.index, france.values)

    # on cree un titre
    plt.title("Évolution de l'espérance de vie en France")
    # On donne le label de laxe abscisse

    plt.xlabel("Années")
    # ordonnees.
    plt.ylabel("Âge")
    # On récupère l'objet "axe" du graphique actuel
    ax = plt.gca()

    # Un texte toutes les 50 années
    ax.xaxis.set_major_locator(MultipleLocator(50))

    #  Un petit trait (sans texte) toutes les 10 années
    ax.xaxis.set_minor_locator(MultipleLocator(10))
    # on ouvre une fenetre avec notre contenu.
    plt.show()
    return


if __name__ == "__main__":
    main()

from load_csv import load
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator


def parse_population(value):
    if isinstance(value, str):
        if value.endswith('M'):
            return float(value[:-1]) * 1_000_000
        elif value.endswith('k'):
            return float(value[:-1]) * 1_000
        return float(value)
    return value


def main():
    data_frame = load("population_total.csv")
    # on place lindex sur les pays
    data_frame.set_index("country", inplace=True)
    # on cible la france, la belgique et l allemagne mtn
    pays_vises = ["France", "Belgium", "Germany"]
    # on recup un tableau avec les pays vises
    comparaison = data_frame.loc[pays_vises].T
    # .T = transpose = ajoute auto une legende pour pays
    # en passant en int, laxe X devient une ligne numerique
    comparaison.index = comparaison.index.astype(int)
    # on ne peut pas faire lattribution ci dessous
    # une string vs un tab numpy
    # comparaison.values = parse_population(comparaison.values)
    # donc on doit utiliser .map() qui va passer chaque valeur
    comparaison = comparaison.map(parse_population)
    # pour sarreter a 2050
    comparaison = comparaison.loc[1800:2050]
    # on prend ces donnees la.
    (comparaison / 1_000_000).plot()

    # on cree un titre
    plt.legend(title="Pays")
    plt.title("Évolution de la population : France, Belgique, Allemagne")
    # On donne le label de laxe abscisse

    plt.xlabel("Années")
    # ordonnees.
    plt.ylabel("Nombre d'habitants en millions")
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

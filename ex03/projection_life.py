from load_csv import load
import matplotlib.pyplot as plt
import pandas as pd


def merge_func(df_life: pd.DataFrame, df_income: pd.DataFrame) -> pd.DataFrame:
    # On extrait uniquement la colonne country et l'année 1900
    # On utilise .copy() pour éviter les warnings de Pandas
    life_1900 = df_life[["country", "1900"]].copy()
    income_1900 = df_income[["country", "1900"]].copy()
    # On fusionne sur la colonne 'country'
    # suffixes permet de différencier les deux colonnes '1900'
    merged = pd.merge(life_1900, income_1900, on="country",
                      suffixes=("_life", "_income"))
    return merged


def main():
    data_life_exp = load("life_expectancy_years.csv")
    data_income_per_pp = load("income_per_person_gdppercapita_"
                              "ppp_inflation_adjusted.csv")
    merge_data = merge_func(data_life_exp, data_income_per_pp)
    # debug pour afficher types de data : print(merge_data.dtypes)
    plt.scatter(merge_data["1900_income"], merge_data["1900_life"])
    # plt.xscale('log') -> pour PIB
    # pour que tous les points ne soient pas tous colles a gauche
    plt.xscale('log')
    plt.title("1900")
    plt.xlabel("Gross domestic product")
    plt.ylabel("Life expectancy")

    # on dit de mettre que ces indices la sur laxe X
    plt.xticks([300, 1000, 10000], ['300', '1k', '10k'])
    plt.show()


if __name__ == "__main__":
    main()

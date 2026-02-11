from load_csv import load
import matplotlib.pyplot as plt
import pandas as pd

def main():
    data_frame = load("life_expectancy_years.csv")
    data_frame.set_index("country", inplace=True)
    france = data_frame.loc["India"]

    plt.plot(france.index, france.values)

    plt.title("Évolution de l'espérance de vie en France")
    plt.xlabel("Années")
    plt.ylabel("Âge")

    plt.show()
    return


if __name__ == "__main__":
  main()

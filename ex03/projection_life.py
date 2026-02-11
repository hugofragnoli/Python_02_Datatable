from load_csv import load
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.ticker import MultipleLocator

def merge_func(arrays: pd.DataFrame) -> pd.DataFrame:




    return 

def main():
    data_life_exp = load("life_expectancy_years.csv")
    data_income_per_pp = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    merge_func()


if __name__ == "__main__":
  main()

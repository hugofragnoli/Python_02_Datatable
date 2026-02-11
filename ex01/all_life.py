from load_csv import load
import matplotlib as plt
import pandas as pd

def main(data_frame: pd.DataFrame) -> any:
    data_frame = load("life_expectancy_years.csv")
    data_frame.set_index("country", inplace=True)
    france = data_frame.loc["France"]
    




if __name__ == "__main__":
  main()

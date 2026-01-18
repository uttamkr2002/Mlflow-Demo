import pandas as pd

def main():
    df = pd.read_csv("../wine-ratings.csv")
    print("Dataset shape:", df.shape)
    print("\nColumns:")
    print(df.columns)
    print("\nFirst 5 rows:")
    print(df.head())

if __name__ == "__main__":
    main()

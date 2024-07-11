import pandas as pd

def clean_data(filepath):
    df = pd.read_csv(filepath)
    df['TransactionDate'] = pd.to_datetime(df['TransactionDate'])
    df = df.drop_duplicates()
    df = df.dropna()
    return df

if __name__ == "__main__":
    df = clean_data('../data/starbucks_sales_data.csv')
    df.to_csv('../data/starbucks_sales_data_cleaned.csv', index=False)
    print("Data cleaning complete and saved to 'data/starbucks_sales_data_cleaned.csv'")
import pandas as pd
import numpy as np

def simulate_data():
    np.random.seed(0)
    num_customers = 1000
    num_products = 50
    num_transaction = 10000

    customer_ids = np.random.choice(range(1, num_customers+1), size=num_transaction, replace=True)
    product_ids = np.random.choice(range(1, num_products+1), size=num_transaction, replace=True)
    quantities = np.random.randint(1, 5, size=num_transaction)
    prices = np.round(np.random.uniform(2.0, 10.0, size=num_products), 2)
    dates = pd.date_range(start='2023-01-01', periods=365).to_list()
    transaction_dates = np.random.choice(dates, size=num_transaction, replace=True)


    data = {
        'CustomerID': customer_ids,
        'ProductID': product_ids,
        'Quantity': quantities,
        'Price': prices[product_ids - 1],
        'TransactionDate': transaction_dates
    }

    df = pd.DataFrame(data)
    df['TotalPrice'] = df['Quantity'] * df['Price']
    return df

if __name__ == "__main__":
    df = simulate_data()
    df.to_csv('../data/starbucks_sales_data.csv', index=False)
    print("Data simulation completed and saved to 'data/starbucks_sales_data.ccsv'")

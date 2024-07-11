import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def eda(filepath):
    df = pd.read_csv(filepath)

    #plot total sales over time
    sales_over_time = df.groupby('TransactionDate')['TotalPrice'].sum().reset_index().sort_values(by='TotalPrice', ascending=False)
    plt.figure(figsize=(12,6))
    plt.plot(sales_over_time['TransactionDate'], sales_over_time['TotalPrice'])
    plt.title('Total Sales Over Time')
    plt.xlabel('Data')
    plt.ylabel('Total Sales')
    plt.grid(True)
    plt.show()

    #plot sales by product
    sales_by_product = df.groupby('ProductID')['TotalPrice'].sum().reset_index().sort_values(by='TotalPrice', ascending=False)
    plt.figure(figsize=(12,6))
    sns.barplot(x='ProductID', y='TotalPrice', data=sales_by_product.head(10))
    plt.title('Top 10 Products by Sales')
    plt.xlabel('Product ID')
    plt.ylabel('Total Sales')
    plt.show()

    #plot customer segementation by total spending
    customer_spending = df.groupby('CustomerID')['TotalPrice'].sum().reset_index().sort_values(by='TotalPrice', ascending=False)
    plt.figure(figsize=(12,6))
    sns.histplot(customer_spending['TotalPrice'], bins=50)
    plt.title('Customer Segmentation by Total Spending')
    plt.xlabel('Total Spending')
    plt.ylabel('Number of Customers')
    plt.show()

if __name__=="__main__":
    eda('../data/starbucks_sales_data_cleaned.csv')
    print("EDA complete")

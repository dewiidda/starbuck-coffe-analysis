import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns


def customer_segmentation(filepath):
    df = pd.read_csv(filepath)
    customer_data = df.groupby('CustomerID').agg({
        'TotalPrice': 'sum',
        'Quantity': 'sum'
    }).reset_index()

    kmeans = KMeans(n_clusters=5, random_state=0)
    customer_data['Cluster'] = kmeans.fit_predict(customer_data[['TotalPrice', 'Quantity']])

    plt.figure(figsize=(12,6))
    sns.scatterplot(x='TotalPrice', y='Quantity', hue='Cluster', data=customer_data, palette='viridis')
    plt.title('Customer Seqmentation')
    plt.xlabel('Total Spending')
    plt.ylabel('Total Quantity Purchased')
    plt.show()

    return customer_data

if __name__ == "__main__":
    customer_data = customer_segmentation('../data/starbucks_sales_data_cleaned.csv')
    customer_data.to_csv('../data/customer_segments.csv', index=False)
    print("Customer segmentation complete and saved to 'data/customer_segments.csv'")
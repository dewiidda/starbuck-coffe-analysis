import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np


def create_user_product_matrix(df):
    user_product_matrix = df.pivot_table(index='CustomerID', columns='ProductID', values='Quantity', aggfunc='sum').fillna(0)
    return user_product_matrix

def recommend_products(customer_id, user_product_matrix, top_n=5):
    similarity_matrix = cosine_similarity(user_product_matrix)
    customer_idx = user_product_matrix.index.get_loc(customer_id)
    similarity_scores = similarity_matrix[customer_idx]
    similar_customers = user_product_matrix.index[np.argsort(-similarity_scores)[1:top_n+1]]

    similar_customer_products = user_product_matrix.loc[similar_customers].mean(axis=0)
    customer_purchased_products = user_product_matrix.loc[customer_id]
    recommended_products = similar_customer_products[customer_purchased_products == 0]
    recommended_products = recommended_products.sort_values(ascending=False).head(top_n)
    return recommended_products

if __name__ == "__main__":
    df = pd.read_csv('../data/starbucks_sales_data_cleaned.csv')
    user_product_matrix = create_user_product_matrix(df)
    customer_id = 1 #example of customer ID
    recommendations = recommend_products(customer_id, user_product_matrix)
    print(f"Recommended products for Customer {customer_id}:")
    print(recommendations)
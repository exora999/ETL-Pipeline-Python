import pandas as pd
import sqlite3 as sq
def extract_data():
    conn = sq.connect("super_store.db")
    query = """
    SELECT products.product_name,products.category,order_items.price_at_purchase,order_items.quantity
    FROM products
    INNER JOIN order_items ON order_items.product_id = products.product_id
    INNER JOIN orders ON orders.order_id = order_items.order_id
    WHERE orders.status = "Completed"
    """
    df = pd.read_sql(query,conn)
    conn.close()
    return df
def transform_data(df):
    df["revenue"] = df["quantity"] * df["price_at_purchase"]
    df_group = (df.groupby(['product_name','category'])['revenue']
                .sum()
                .reset_index()
                .sort_values(by="revenue",ascending=False)
                )
    return df_group
def load_data(df_group):
    df_group.to_csv("Finale.csv", index=False)


if __name__ == "__main__":
    print("Starting the ETL pipeline...")
    raw_data = extract_data()
    clean_data = transform_data(raw_data)
    load_data(clean_data)
    print("Donne")
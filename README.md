# 🔄 Python ETL Pipeline with SQLite & Pandas

A clean and modular Extract, Transform, Load (ETL) pipeline script built with Python, Pandas, and SQLite.

## 🚀 Pipeline Workflow
1. **Extract (`extract_data.py`):** 
   - Connects to a local SQLite database (`super_store.db`).
   - Executes an optimized SQL query using multiple `INNER JOIN` operations to fetch product and order details exclusively for "Completed" statuses.
2. **Transform (`transform_data`):** 
   - Computes total product revenue (`quantity * price_at_purchase`).
   - Groups, aggregates, and sorts the dataset by product name and category in descending order of revenue.
3. **Load (`load_data`):** 
   - Exports the final clean aggregated dataset into a structured CSV file (`Finale.csv`).

## 🛠️ Tech Stack
* **Language:** Python 3.x
* **Data Manipulation:** Pandas
* **Database:** SQLite / Relational Queries
* **Concepts:** ETL Architecture, SQL Joins, Data Aggregation

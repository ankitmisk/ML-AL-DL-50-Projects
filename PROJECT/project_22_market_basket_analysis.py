PROJECT = {
    "name": "Market Basket Analysis (Apriori)",
    "icon": "🛒",
    "dataset": "Groceries Dataset",
    "description": "Discover association rules using Apriori.",
    "steps": """
    1. Convert transactions to one-hot  
    2. Apply Apriori  
    3. Generate rules (support, confidence, lift)  
    4. Show top associations  
    """,
    "code": """
import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules

data = [line.strip().split(',') for line in open("groceries.csv")]

te = TransactionEncoder()
arr = te.fit(data).transform(data)
df = pd.DataFrame(arr, columns=te.columns_)

frequent = apriori(df, min_support=0.02, use_colnames=True)
rules = association_rules(frequent, metric="lift", min_threshold=1)

print(rules.sort_values("lift", ascending=False).head())
"""
}

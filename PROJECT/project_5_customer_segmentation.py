PROJECT = {
    "name": "Customer Segmentation (KMeans)",
    "icon": "🧩",
    "dataset": "Mall Customers",
    "description": "Cluster customers by income & spending score.",
    "steps": "Scale → KMeans → Plot",
    "code": """
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("Mall_Customers.csv")

X = df[["Annual Income (k$)", "Spending Score (1-100)"]]

sc = StandardScaler()
X_scaled = sc.fit_transform(X)

kmeans = KMeans(n_clusters=5)
df["Cluster"] = kmeans.fit_predict(X_scaled)

sns.scatterplot(
    x=df["Annual Income (k$)"],
    y=df["Spending Score (1-100)"],
    hue=df["Cluster"],
    palette="tab10"
)

plt.show()
"""
}

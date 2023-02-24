import json

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

if __name__ == "__main__":
    sns.set(style="darkgrid")

    data = {
        "latency": list(),
        "engine": list(),
        "query": list()
    }
    
    with open("presto/presto.json") as f:
        presto_data = json.load(f)

    with open("spark/spark.json") as f:
        spark_data = json.load(f)

    for key, value in presto_data.items():
        data["latency"].append(sum(value)/10)
        data["engine"].append("presto")
        data["query"].append(key)

    for key, value in spark_data.items():
        data["latency"].append(sum(value)/10)
        data["engine"].append("spark")
        data["query"].append(key)

    ax = sns.barplot(x="query", y="latency", hue="engine", data=data)
    plt.show()

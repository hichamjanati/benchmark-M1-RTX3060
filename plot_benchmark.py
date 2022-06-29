import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import glob


data = []
for filename in glob.glob('data/*.csv'):
    df = pd.read_csv(filename, index_col=0)
    data.append(df)
data = pd.concat(data)
data.reset_index(inplace=True)
data["Device"] = data.machine + " | " + data.device_name

f, ax = plt.subplots(1, 1)
sns.lineplot(y="time", x="n", hue="Device", data=data, ax=ax)
plt.ylabel("Time in (s)")
plt.xlabel("n")
plt.title("Run time of (A @ B).sum() for square n x n matrices")
plt.grid(True)
plt.savefig("benchmark.png")




    
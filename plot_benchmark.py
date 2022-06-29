import seaborn as sns
import pandas as pd
import glob


data = []
for filename in glob.glob('data/*.csv'):
    df = pd.read_csv(filename)
    data.append(df)
data = pd.concat(data)



# colors = ["black", "indianred", "forestgreen"]
# plt.figure()
# for color, (key, val) in zip(colors, scores.items()):
#     mean = val.mean(axis=0)
#     std = val.std(axis=0)
#     plt.fill_between(ns, mean - std, mean + std, alpha=0.5, color=color)
#     plt.plot(ns, mean, color=color, lw=3, label=key)
#     plt.grid(True)

# plt.ylabel("Time in (s)")
# plt.xlabel("n")
# plt.title("Run time of (A @ B).sum() for square n x n matrices")
# plt.legend()
# plt.savefig("benchmark.png")




    
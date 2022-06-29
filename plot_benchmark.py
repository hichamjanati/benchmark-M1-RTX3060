import matplotlib.pyplot as plt
import numpy as np
import pickle

with open("scores-victus.pkl", "rb") as ff:
    scores_victus = pickle.load(ff)


with open("scores-macbook.pkl", "rb") as ff:
    scores_mac = pickle.load(ff)


scores = scores_mac | scores_victus

ns = [5, 20, 100, 500, 750, 1000, 1500, 2000, 3000, 3500, 4000, 4500, 5000]
colors = ["black", "indianred", "forestgreen"]
plt.figure()
for color, (key, val) in zip(colors, scores.items()):
    mean = val.mean(axis=0)
    std = val.std(axis=0)
    plt.fill_between(ns, mean - std, mean + std, alpha=0.5, color=color)
    plt.plot(ns, mean, color=color, lw=3, label=key)
    plt.grid(True)

plt.ylabel("Time in (s)")
plt.xlabel("n")
plt.title("Run time of (A @ B).sum() for square n x n matrices")
plt.legend()
plt.savefig("benchmark.png")




    
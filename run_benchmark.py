import torch
import pickle
import numpy as np
from time import time


def f(n, device):
    t = time()
    A = torch.randn(n, n).to(device)
    B = torch.randn(n, n).to(device)
    C = (A @ B).sum()
    return time() - t

devices = ["cpu"]

if torch.cuda.is_available():
    torch.cuda.init()
    devices.append("cuda:0")
    device_names = ["AMD Ryzen 7 5700", "RTX 3060"]
    filename = 'victus'
else:
    device_names = ["M1"]
    filename = 'macbook'


if __name__ == "__main__":
    n_runs = 20
    ns = [5, 20, 100, 500, 750, 1000, 1500, 2000, 3000, 3500, 4000, 4500, 5000]
    scores = dict()

    for device, device_name in zip(devices, device_names):
        times = np.empty((n_runs, len(ns)))
        for jj, n in enumerate(ns):
            for run in range(n_runs):
                times[run, jj] = f(n, device)
        scores[device_name] = times
    
    with open("scores-%s.pkl" % filename, 'wb') as ff:
        pickle.dump(scores, ff)
    



from platform import machine
import torch
import pandas as pd
import numpy as np
from time import time


torch.manual_seed(42)

def f(n, device):
    t = time()
    A = torch.randn(n, n).to(device)
    B = torch.randn(n, n).to(device)
    C = (A @ B).sum()
    return time() - t

devices = ["cpu"]

machine_name = input("Enter a name for your machine:\n")
cpu_name = input("Enter a name for your CPU:\n")
device_names = [cpu_name]

if torch.cuda.is_available():
    torch.cuda.init()
    gpu_name = input("Enter a name for your GPU:\n")
    devices.append("cuda:0")
    device_names.append(gpu_name)


if __name__ == "__main__":
    n_runs = 10
    ns = [10, 50, 100, 250, 500, 1000, 1500, 2000, 3000, 4000]

    data = []
    for device, device_name in zip(devices, device_names):
        times = np.empty((n_runs, len(ns)))
        for jj, n in enumerate(ns):
            for run in range(n_runs):
                times[run, jj] = f(n, device)
        times = pd.DataFrame(times, columns=ns)
        times["device"] = device
        times["machine"] = machine_name
        times["device_name"] = device_name
        data.append(times)
    df = pd.concat(data)
    df = df.melt(["device", "machine", "device_name"], var_name="n", value_name="time")
    df.to_csv("data/%s.csv" % machine_name)
    



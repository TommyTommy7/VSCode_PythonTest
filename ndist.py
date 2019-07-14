# %%

import math
import random

def pdf(x, mu, sigma):
    sigma_pow = sigma ** 2
    return (
        1
        / math.sqrt(2 * math.pi * sigma_pow)
        * math.exp(-(x - mu) ** 2 / 2 * sigma_pow)
    )

# pdf関数を可視化して確認
import matplotlib.pyplot as plt


x = [x * 0.01 for x in range(-500, 500)]
y = [pdf(x_, 0, 1) for x_ in x]
fig, ax = plt.subplots()
ax.plot(x, y)
ax.hist([random.gauss(0, 1) for _ in range(10000)],
        bins=20, density=True);

#%%

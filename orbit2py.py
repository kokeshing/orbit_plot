# coding: UTF-8

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import math

# 使用する変数の宣言 azはボーア半径の10の11乗倍 znは原子番号 trはifの成立階数
i = 0
zn = 18.0

# グラフの作成
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d', aspect='equal')


# 軸ラベルの設定
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")
ax.set_xlim([-0.5, 0.5])
ax.set_ylim([-0.5, 0.5])
ax.set_zlim([-0.5, 0.5])

# モンテカルロ法による電子雲描画 rはボーア半径との比
while i < 300000:
	p = np.random.rand()
	x = np.random.rand() * 1.0 - 0.5
	y = np.random.rand() * 1.0 - 0.5
	z = np.random.rand() * 1.0 - 0.5
	r = np.sqrt(x ** 2 + y ** 2 + z ** 2)
	rho = zn * r
	pls = 0.5 / np.sqrt(6.0) * zn * np.sqrt(zn) * rho * np.exp( - rho * 0.5) * 0.5 * np.sqrt(3.0 / np.pi) * y / r
	if p < pls ** 2:
		ax.scatter3D(x, y, z, s=0.1, color='#000000', alpha=0.01)
		i += 1

#グラフを描画
plt.savefig("Argraph2py.png")
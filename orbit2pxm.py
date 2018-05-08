# coding: UTF-8

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from multiprocessing import Pool
from multiprocessing import Process

# 使用する変数の宣言 azはボーア半径の10の11乗倍 znは原子番号 trはifの成立階数
zn = 1.0

# グラフの作成
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d', aspect='equal')


# 軸ラベルの設定
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")
ax.set_xlim([-15, 15])
ax.set_ylim([-15, 15])
ax.set_zlim([-15, 15])

# モンテカルロ法による電子雲描画 rはボーア半径との比
def monte():
	p = np.random.rand()
	x = np.random.rand() * 30.0 - 15.0
	y = np.random.rand() * 30.0 - 15.0
	z = np.random.rand() * 30.0 - 15.0
	r = np.sqrt(x ** 2 + y ** 2 + z ** 2)
	rho = zn * r
	pls = 0.5 / np.sqrt(6.0) * zn * np.sqrt(zn) * rho * np.exp( - rho * 0.5) * 0.5 * np.sqrt(3.0 / np.pi) * x / r
	if p < pls ** 2:
		ax.scatter3D(x, y, z, s=0.1, color='#000000', alpha=0.1)

def multi():
    p = Pool(10) #最大プロセス数:10
    p.map(monte, range(300000000))


multi()

#グラフを描画
plt.savefig("Hgraph2px.png")
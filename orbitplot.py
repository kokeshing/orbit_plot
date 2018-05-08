# coding: UTF-8

import numpy
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import math

# 使用する定数の宣言 azはボーア半径の10の11乗倍 znは原子番号 trはifの成立階数
i = 0
az = 5.2917006 / (10 ** 11)
zn = 18.0
tr = 0

# グラフの作成
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d', aspect='equal')


# 軸ラベルの設定
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")
ax.set_xlim([-10, 10])
ax.set_ylim([-10, 10])
ax.set_zlim([-10, 10])

# モンテカルロ法による1s軌道の電子雲描画 rはボーア半径との比
def f1splot():
	while i < 1000000:
		x = numpy.random.rand() - 0.5
		y = numpy.random.rand() - 0.5
		z = numpy.random.rand() - 0.5
		p = numpy.random.rand()
		r = math.sqrt(x ** 2 + y ** 2 + z ** 2)
		rho = 2 * zn * r
		pls = 4 * (zn ** 3) * (r ** 2) * ( math.e ** -rho )
		if p < pls:
			ax.scatter3D(x, y, z, s=0.1, color='#000000', alpha=0.01)
			tr += 1
		i += 1

	#グラフを描画
	plt.savefig("Argraph1s.png")

# モンテカルロ法による2s軌道電子雲描画 rはボーア半径との比
def f2splot():
	while i < 1000000:
		x = numpy.random.rand() * 10 - 5
		y = numpy.random.rand() * 10 - 5
		z = numpy.random.rand() * 10 - 5
		p = numpy.random.rand()
		r = math.sqrt(x ** 2 + y ** 2 + z ** 2)
		rho = 2 * zn * r
		pls = (zn ** 3) * (r ** 2) * (2 - (rho ** 2)) * ( math.e ** -rho ) / 8
		if p < pls:
			ax.scatter3D(x, y, z, s=0.1, color='#000000', alpha=0.01)
			tr += 1
		i += 1

	#グラフを描画
	plt.savefig("Argraph2s.png")

# モンテカルロ法による2p軌道電子雲描画 rはボーア半径との比
def f2pplot():
	while i < 1000000:
		x = numpy.random.rand() * 10 - 5
		y = numpy.random.rand() * 10 - 5
		z = numpy.random.rand() * 10 - 5
		p = numpy.random.rand()
		r = math.sqrt(x ** 2 + y ** 2 + z ** 2)
		rho = zn * r
		pls = (zn ** 3) * (r ** 2) * (rho ** 2) * ( math.e ** -rho ) / 24
		if p < pls:
			ax.scatter3D(x, y, z, s=0.1, color='#000000', alpha=0.01)
			tr += 1
		i += 1
	plt.savefig("Argraph2p.png")
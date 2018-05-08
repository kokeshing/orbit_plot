# coding: UTF-8

import numpy
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import math

# znは原子番号
i = 0
az = 5.2917006 / (10 ** 11)
zn = 18.0
# グラフの作成
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d', aspect='equal', azim=180, elev=0)


# 軸ラベルの設定
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")
ax.set_xlim([-0.5, 0.5])
ax.set_ylim([-0.5, 0.5])
ax.set_zlim([-0.5, 0.5])

# モンテカルロ法による電子雲描画 rはボーア半径との比
while i < 30000:
	x = numpy.random.rand() * 0.5 - 0.25
	y = numpy.random.rand() * 0.5 - 0.25
	z = numpy.random.rand() * 0.5 - 0.25
	p = numpy.random.rand()
	r = math.sqrt(x ** 2 + y ** 2 + z ** 2)
	rho = 2 * zn * r
	pls = 4 * (zn ** 3) * (r ** 2) * ( math.e ** -rho )
	if p < pls:
		ax.scatter3D(x, y, z, s=0.1, color='#000000', alpha=0.01)
		i += 1

#グラフを描画
plt.savefig("Argraph1s.png")


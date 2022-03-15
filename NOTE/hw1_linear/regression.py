import matplotlib.pyplot as plt
import numpy as np
import random

x = np.array([0, 1, 2, 3, 4], dtype=np.float32)
y = np.array([2, 3, 4, 5, 6], dtype=np.float32)
# x = np.array([0, 1, 2, 3, 4], dtype=np.float32)
# y = np.array([1.9, 3.1, 3.9, 5.0, 6.2], dtype=np.float32)

def predict(a, xt):
	return a[0]+a[1]*xt

def MSE(a, x, y):
	total = 0
	for i in range(len(x)):
		total += (y[i]-predict(a,x[i]))**2
	return total

def loss(p):
	return MSE(p, x, y)

# p = [0.0, 0.0]
# plearn = optimize(loss, p, max_loops=3000, dump_period=1)
def optimize(p, maxGens, maxFails, step = 0.1):
    # 請修改這個函數，自動找出讓 loss 最小的 p
    # p = [2,1] # 這個值目前是手動填的，請改為自動尋找。(即使改了 x,y 仍然能找到最適合的回歸線)
    fails = 0                             # 失敗次數設為 0
    # 當代數 gen<maxGen，且連續失敗次數 fails < maxFails 時，就持續嘗試尋找更好的解。
    for gens in range(maxGens):
        sx = p[0]+step if random.random() > 0.5 else p[0]-step
        sy = p[1]+step if random.random() > 0.5 else p[1]-step
        snew =[sx,sy]       #  取得鄰近的解
        if (loss(snew) <= loss(p)):          #  如果鄰近解比目前解更好
            # print(gens, ':', snew.str())  #    印出新的解
            p = snew                      #    就移動過去
            fails = 0                     #    移動成功，將連續失敗次數歸零
        else:                             #  否則
            fails = fails + 1             #    將連續失敗次數加一
        if (fails >= maxFails):
            break
    return p

p = optimize([0.0, 0.0], 100000, 1000)

# Plot the graph
y_predicted = list(map(lambda t: p[0]+p[1]*t, x))
print('y_predicted=', y_predicted)
plt.plot(x, y, 'ro', label='Original data')
plt.plot(x, y_predicted, label='Fitted line')
plt.legend()
plt.show()
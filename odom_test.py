import time
import numpy as np
import matplotlib.pyplot as plt


class odom():
    def __init__(self,start_position, time):
        self.position=np.array([start_position[0],start_position[1]])
        self.start_time = time

    def update_odom(self,time):
        diff_time = time - self.start_time
        self.position[0] += diff_time * 0.1 + np.random.normal(0.0,5.0)
        self.position[1] += diff_time * 0.2 + np.random.normal(0.0,5.0)

    def add_noise(self):
        self.position[0] += 10

def task():
    print(time.time())


#初期位置
start = np.array([0,0])
#クラス作成
robot = odom(start, time.time())

plt.plot(100,100,"o")
while True:
    task()
    time.sleep(1)
    robot.update_odom(time.time())
    print(robot.position)

    plt.plot(robot.position[0],robot.position[1],"o")
    plt.pause(.02)



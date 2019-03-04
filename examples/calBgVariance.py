import numpy as np
import os
import sys

row_num = 8
col_num = 8
pixel_num = 64
#使矩阵完整显示
np.set_printoptions(threshold = np.inf)
if len(sys.argv) > 1:
    try:
        dataDir = sys.argv[1]
    except:
        raise ValueError("please input the correct dir of npy data")
else:
    raise ValueError("please input the dir of npy data")
#读取路径
currDir = os.path.abspath(os.path.dirname(__file__))
if currDir.endswith("examples"):
    dataDir = currDir + "/" + dataDir
all_frame = np.load(dataDir)
all_var = []

for i in range(row_num):
    for j in range(col_num):
        curr_pixel = all_frame[:,i:i+1,j:j+1]
        curr_var = np.var(curr_pixel)
        all_var = np.append(all_var,curr_var)

print(np.max(all_var))
#print(np.var(all_frame, ddof = 1))
#bg_average = np.sum(all_frame) / np.size(all_frame)


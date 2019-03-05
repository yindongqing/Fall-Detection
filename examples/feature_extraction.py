import numpy as np
import os
import sys
import time
row_num = 8
col_num = 8
pixel_num = 64
k_start = 0 
k_end = 0
max_moving_frame = 0
max_variance = 0.0
max_therhold_pixel_num = 0
therhold = 0.8
is_human = False
max_var_list = [] #存放最大方差的矩阵
active_pixel_num_list = []


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
if np.size(all_frame) < 10 * pixel_num:
    raise ValueError("please input the dir larger than 10*64")

frame_num = np.size(all_frame) // pixel_num #帧数
#print(frame_num)
curr_all_var = np.zeros(pixel_num)
for k in range(10,frame_num):
    curr_frame = all_frame[k - 10:k,:,:]
    for i in range(row_num):
        for j in range(col_num):
            curr_pixel = curr_frame[:,i,j]
            curr_var = np.var(curr_pixel)
            curr_all_var[i * 8 + j ] = curr_var
    #当前温度分布最大方差        
    curr_max_var = np.max(curr_all_var)
    #如果存在方差分布有超过阈值的像素点，则证明有人在传感器范围内
    if curr_max_var > therhold:
        if not is_human:
            is_human = True
            k_start = k
        #存放当前最大方差
        max_var_list.append(curr_max_var)
        #存放活跃像素数量
        active_pixel = np.where(curr_all_var > therhold)
        active_num = np.size(active_pixel)
        """
        print(curr_all_var)
        print(active_pixel)
        print(curr_max_var,active_num)
        """
        active_pixel_num_list.append(active_num)
    else:
        if is_human:
            is_human = False
            k_end = k
            #计算出最大运动帧数
            max_moving_frame = k_end - k_start + 1
            #计算出最大方差
            max_variance = np.max(max_var_list)
            #计算出最大活跃像素数量
            max_therhold_pixel_num = np.max(active_pixel_num_list)
            print(max_moving_frame,max_variance,max_therhold_pixel_num)

        else:
            continue




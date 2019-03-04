import numpy as np
import os
import sys

if len(sys.argv) > 2:
    try:
        dataDir = sys.argv[1]
    except:
        raise ValueError("please input the correct dir of npy data")
else:
    raise ValueError("please input the dir of npy data")

currDir = os.path.abspath(os.path.dirname(__file__))

all_frame = np.load(dataDir)


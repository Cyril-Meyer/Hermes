import math
import argparse
import numpy as np

parser = argparse.ArgumentParser(description='view user list')
parser.add_argument('filename', type=str, help='user filename')
parser.add_argument('number', type=int, help='number of splits')
args = parser.parse_args()
filename = args.filename

db = np.load(filename)
assert db.dtype == np.int64
assert len(db.shape) == 1

r = math.ceil(len(db) / args.number)

j = 1
for i in range(0, len(db), r):
    np.save(f'{filename[:-4]}_{j}.npy', db[i:i+r])
    j += 1

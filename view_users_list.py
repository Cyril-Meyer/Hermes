import argparse
import numpy as np

parser = argparse.ArgumentParser(description='view user list')
parser.add_argument('filename', type=str, help='user filename')
args = parser.parse_args()
filename = args.filename

db = np.load(filename)
assert db.dtype == np.int64
assert len(db.shape) == 1

for user in db:
    print(user)

print(len(db))
print(len(np.unique(db)))

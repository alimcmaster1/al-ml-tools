import time
import numpy as np
import dask.bag as db
import dask.array as da
import dask

from dask.distributed import Client
# Use all 8 cores
client = Client(processes=False)


def square(x):
    return x **2


A = da.arange(10000000, chunks=10000)
ret = dask.array.apply_along_axis(square, 0, A)
ret = dask.array.sum(ret)
tot = ret.compute()
start = time.time()

end = time.time()
print("Time Taken {}".format(end-start))
print(tot)

start = time.time()
arr = np.array(range(10000000))
res = np.sum(arr ** 2)
end = time.time()
print("Time Taken {}".format(end-start))
print(res)
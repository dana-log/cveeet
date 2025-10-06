import numpy as np
print(np.iinfo(np.int64))
print(np.finfo(np.float128))
print(np.sctypeDict)
print(len(np.sctypeDict))
print(*sorted(map(str, set(np.sctypeDict.values()))), sep='\n')
a = -456
print(np.uint8(-456))
print(np.finfo(np.float32))
arr, step = np.linspace(-6, 21, 60, endpoint=False, retstep=True)
print(round(step, 2))
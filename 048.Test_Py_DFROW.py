import random
import pandas as pd

r = []
for i in list("ABCD"):
    j = random.choice([t for t in range(10)])
    for ij in range(j):
        r.append([i, random.choice([t for t in range(20)])])

dr = pd.DataFrame(r).sort_values(by=[0, 1])

dr1 = dr.copy()
dr1["diffs"] = dr1.groupby(by=0).diff()
print(dr1)
"""
    0   1  diffs
0   A  12    NaN
3   B   9    NaN
2   B  17    8.0
4   B  17    0.0
1   B  18    1.0
8   C   2    NaN
5   C   9    7.0
9   C  12    3.0
7   C  13    1.0
10  C  15    2.0
6   C  17    2.0
11  C  19    2.0
12  D   8    NaN
14  D  12    4.0
16  D  17    5.0
15  D  18    1.0
13  D  19    1.0
"""

dr2 = dr.copy()
dr2["shift"] = dr2.groupby(by=0).shift()
print(dr2)
"""
    0   1  shift
0   A  12    NaN
3   B   9    NaN
2   B  17    9.0
4   B  17   17.0
1   B  18   17.0
8   C   2    NaN
5   C   9    2.0
9   C  12    9.0
7   C  13   12.0
10  C  15   13.0
6   C  17   15.0
11  C  19   17.0
12  D   8    NaN
14  D  12    8.0
16  D  17   12.0
15  D  18   17.0
13  D  19   18.0
"""

dr3 = dr.copy()
dr3["shift"] = dr3.groupby(by=0).shift(-1)
print(dr3)
"""
    0   1  shift
0   A   0    0.0
1   A   0    6.0
2   A   6   17.0
3   A  17    NaN
7   B   0    0.0
9   B   0    1.0
6   B   1   13.0
5   B  13   16.0
4   B  16   17.0
8   B  17    NaN
15  C   4    5.0
16  C   5    8.0
10  C   8    9.0
12  C   9   11.0
13  C  11   17.0
11  C  17   17.0
14  C  17    NaN
17  D   1    2.0
18  D   2    NaN
"""

import pandas as pd
import numpy as np
# !pip install Ipython
from IPython.display import Image

a1 = pd.DataFrame({"a" : [1,2,3], "b" : [4,5,6], "c" : [7,8,9]})
a2 = pd.DataFrame([[1,2,3], [4,5,6], [7,8,9]], ["a","b","c"])
a1
a2
import random
import pandas as pd
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
print(data)
data = pd.DataFrame([[int(i=='robot'),int(i=='human')] for i in lst ],columns=['robot','human'])
print(data)
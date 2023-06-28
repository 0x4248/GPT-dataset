# Machine Learning 
# Data from: https://github.com/lewisevans2007/GPT-dataset/tree/fe8f4dfce5642806b636918279ec0bbed68581e6/dataset/2612
# By: Lewis Evans

import numpy as np
from sklearn import linear_model

temp = [20,25,30,35,40,20,25,30,35,40,15,22,27,32,38]
ph = [7.0,7.2,7.5,7.8,8.0,7.0,7.2,7.5,7.8,8.0,6.8,7.4,7.3,7.7,8.2]

regr = linear_model.LinearRegression()
regr.fit(np.array(temp).reshape(-1, 1), ph)

print(regr.predict([[25]]))

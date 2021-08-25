import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
from sklearn.decomposition import PCA

data = pd.read_csv("/Users/shashankasharma/cs_stuff/Introduction to Data Science/MiddleSchoolProject/Student Response.csv")


r = data.corr()

zscoredData = stats.zscore(r)
pca = PCA().fit(zscoredData)
varianceExplained = pca.explained_variance_ratio_
loadings = pca.components_
rotatedData = pca.fit_transform(zscoredData)

x_label_list = list(r.columns)
y_label_list = x_label_list[-1::-1]

numCat = 6
plt.bar([1,2,3,4,5,6],varianceExplained)
plt.xlabel('Principal component')
plt.ylabel('Eigenvalue')


fig, ax = plt.subplots(1,1)

img = ax.imshow(r,extent=[-1,1,-1,1])

x_label_list = list(r.columns)
y_label_list = x_label_list[-1::-1]

ax.set_xticks([-0.825,-0.495,-.165,.165,.495,.825,])
ax.set_yticks([-0.825,-0.495,-.165,.165,.495,.825,])

ax.set_xticklabels(x_label_list, rotation = 90)
ax.set_yticklabels(y_label_list, rotation = 0)


fig.colorbar(img)

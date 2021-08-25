import numpy as np
import pandas as pd
import scipy as stats
import matplotlib.pyplot as plt


def main():
    file = open("/Users/shashankasharma/cs_stuff/Introduction to Data Science/MiddleSchoolProject/Proportion.csv")
    data = np.genfromtxt(file, delimiter=",")
    dataset = []
    
    for i in range(len(data)):
        if data[i] != 0:
            dataset.append(data[i])
            
    count = 4014
    dataset.pop(0)
    beta = 0
    dataset.sort()
    len(dataset)
    gamma = 0
    
    for i in range(len(dataset) - 1,1,-1):
        if beta < count: 
            beta += dataset[i]
            gamma += 1
        else:
            print(i)
            break
    
    #plt.bar([i for i in range(len(dataset))],dataset)
    fig = plt.figure()
    ax = fig.add_axes([0,0,1,1])
    langs = ['C', 'C++', 'Java', 'Python', 'PHP']
    students = [23,17,35,29,12]
    ax.bar(langs,students)
    plt.show()
     
    print()
    print(dataset[283])
    print(count)
    print(beta)
    print(gamma)
            
            
main()
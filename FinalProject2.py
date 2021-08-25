
import numpy as np
import pandas as pd
import scipy as stats


def main():
    file = open("/Users/shashankasharma/cs_stuff/Introduction to Data Science/MiddleSchoolProject/AsianAcceptances.csv")
    data = np.genfromtxt(file, delimiter=",")
    totalSchools = len(data) # 587 total schools
    schools = [] # 125 above average acceptance rates
    percentEthnicity = []
    
    for i in range(len(data)):
        if data[i][1] >= 0.08:
            schools.append(i)
            
    print(len(schools))       
    
    for i in schools:
        if data[i][0] >= 50:   
            percentEthnicity.append(data[i][0])

    print(len(percentEthnicity))      
    
    
    
    
main()
import numpy as np
import pandas as pd
import scipy as stats

# 83 out of 126 schools that have poor supportive environments 
# also have low grades

# 40 out of 80 schools with poor trust
# also have low grades

# 61 out of 102 with poor strong families
# also have low grades

# 57 out of 98 with poor rigorous instruction 
# also have low grades


# 40 out of 80 with poor collaborative teachers
# also have low grades

# 53 out of 94 with poor effective leadership 
# also have low grades






def frequencies(data,lowerBound, upperBound):
    result = 0
    for i in range(len(data)):
        if (lowerBound <= data[i] <= upperBound):
            result += 1
    
    return result

def main():
    file = open("/Users/shashankasharma/cs_stuff/Introduction to Data Science/MiddleSchoolProject/MathScores.csv")
    data = np.genfromtxt(file, delimiter=",")
    schools = [] 
    mathScores = [] 
    poorMathScores = []
    
    for i in range(len(data)):
        if data[i][1] <= 4:
            schools.append(i)
    
    print(len(schools))
    
    for  i in range(len(schools)):
        mathScores.append(data[i][0])
        
    for i in range(len(mathScores)):
        if mathScores[i] <= 0.43:
            poorMathScores.append(mathScores[i])
            
    #print(gamma)
    print(len(gamma))
        
    lowerBound = .91
    upperBound = 1
    #print(frequencies(data,lowerBound,upperBound))
    
    
main()
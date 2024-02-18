from typing import List

def add_binary_integers(a: List, b: List) -> List:

    if len(a) == len(b):
        result = [0] * (len(a) + 1)
        memory = 0
        for i in range(len(a)-1, -1, -1):
            if a[i] + b[i] + memory > 1:
                result[i+1] = 0
                memory = 1
            else:
                result[i+1] = a[i] + b[i] + memory
                memory = 0
            result[0] = memory
        
        return result 
    
    else:
        print('Numbers should be equal size')


a = [1,0]
b = [1,1]

print(add_binary_integers(a, b))
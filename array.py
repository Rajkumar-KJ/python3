import numpy as np


arr = np.array([10, 20, 30, 40])
np.zeros(5)        
np.ones((2, 3))    

np.arange(0, 10, 2)  
np.linspace(0, 1, 5)   

print(arr[0])       
print(arr[1:3])     

arr[0] = 100
print(arr)

arr = np.delete(arr, 1)
print(arr)

arr = np.insert(arr, 1, 200)
print(arr)

arr = np.append(arr, [300, 400])
print(arr)

arr = np.array([1, 2, 3, 4])


print(arr + 5)    
print(arr - 2)   
print(arr * 3)    
print(arr / 2)     
print(arr ** 2)   
print(np.sqrt(arr))


print(arr.sum())     
print(arr.mean())  
print(arr.min())      
print(arr.max())    
print(arr.std())    
print(arr.var())     
print(arr.cumsum())  
print(arr.cumprod())  


print(np.all(arr > 0))    
print(np.any(arr > 3))     
print(arr[arr > 2]) 
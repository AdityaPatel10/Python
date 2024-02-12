# # def name(N):
# #     print(N)
# # name(N="Aditya")  #Keyword Argument
# # name("Arneet")   #Positional Argument
# from scipy.optimize import minimize
# def ob(x):
#     return x**2 + 4*x + 4
# result = minimize(ob, x0=0)
# print(result)
import numpy as np 
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9 , 10])
mean_value=np.mean(arr)
print(mean_value)

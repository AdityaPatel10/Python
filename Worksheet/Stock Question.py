from scipy.optimize import linprog
# Objective function coefficients (negative because linprog minimizes)
c = [-0.08, -0.1]
# Inequality constraints matrix
A = [[-1, 0],[0, -1],[1, 1]]
b = [-2000, -3000, 10000]
x_bound = (2000, 7000)
y_bound = (3000, 6000)
# Solve the linear programming problem
res = linprog(c, A_ub=A, b_ub=b, bounds = (x_bound, y_bound), method='highs') 
# Check if the optimization was successful
if res.success: # Extract results
    stock_A_qty = int(round(res.x[0]))
    stock_B_qty = int(round(res.x[1])) # Calculate total investment and total return
    total_investment = stock_A_qty * 1000 + stock_B_qty * 1000
    total_return = -res.fun * total_investment # Print results
    print(f"Number of Stock A: {stock_A_qty}")
    print(f"Number of Stock B: {stock_B_qty}")
    print(f"Total Investment: ${total_investment}")
    print(f"Total Return: ${total_return}")
else:
    print("Optimization was not successful.")
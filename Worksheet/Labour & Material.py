from scipy.optimize import linprog
# Objective function coefficients (negative because linprog minimizes)
c = [-10, -15] # Profit from Product X and Product Y
# Inequality constraints matrix
A = [[2, 3], [1, 2]] # Material constraint for Product X and Product Y
# Inequality constraints bounds
b = [100, 80]
x_bound = (0, None)
y_bound = (0, None)
# Solve the linear programming problem
res = linprog(c, A_ub=A, b_ub=b, bounds = (x_bound, y_bound), method='highs')
# Check if the optimization was successful
if res.success:
# Extract results
    product_X_qty = int(round(res.x[0]))
    product_Y_qty = int(round(res.x[1]))
# Calculate total profit
    total_profit = -res.fun # Convert negative minimum to positive maximum
# Print results
    print(f"Number of Product X: {product_X_qty}")
    print(f"Number of Product Y: {product_Y_qty}")
    print(f"Total Profit: ${total_profit}")
else:
    print("Optimization was not successful.")
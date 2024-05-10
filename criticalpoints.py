from sympy import symbols,solve

# Define the symbols using sympy.Symbol for nicely written output
X, Y1, Y2 = symbols(r'X Y_1 Y_2')

# Define the parameters with Greek letters and appropriate LaTeX formatting
Pi, mu, beta1, beta2, c, gamma1, gamma2, tau = symbols(r'\Pi \mu \beta_1 \beta_2 c \gamma_1 \gamma_2 \tau')

# Define N in terms of X, Y1, and Y2
N = X + Y1 + Y2

# Define the differential equations using N
dX_dt = Pi - mu*X - ((1/N)*(beta1*c*X*Y1)) -((1/N)*(beta2*c*X*Y2))
dY1_dt = (1/N)*beta1*c*X*Y1 - (mu + gamma1 + tau)*Y1
dY2_dt = (1/N)*beta2*c*X*Y2 - (mu + gamma2 + tau)*Y2

# Find critical points
critical_points = solve([dX_dt, dY1_dt, dY2_dt], (X, Y1, Y2))

print("Critical points:")
for point in critical_points:
    print(point)



    
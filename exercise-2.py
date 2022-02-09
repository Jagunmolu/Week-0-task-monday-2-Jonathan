def quadraticSolver(a, b, c):
    if a == 0:
        return "This is not a quadratic equation."
    return f"The roots of the equation are: {(((-b) - ((b**2 - 4*a*c)**0.5))/(2*a))} and {(((-b) + ((b**2 - 4*a*c)**0.5))/(2*a))}."


print(quadraticSolver(0, 1, -9))

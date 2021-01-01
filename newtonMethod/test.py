from python_code import Newton

newton = Newton()

print("Derivative is {}".format(newton.calculate_derivative(500)))
print("Function value: {}".format(abs(newton.calculate_f_value(500))))

sol, num_iterations = newton.calculate_roots(500)
print(sol, num_iterations)


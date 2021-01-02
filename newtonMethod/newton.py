import sympy as sym
import numpy as np
import matplotlib.pyplot as plt

class Newton():
    def __init__(self, f='x**2', max_iter=1e6, eps=1e-14):
        self.f = f
        self.max_iter = max_iter
        self.eps = eps

        # Define x as mathematical symbol
        x = sym.symbols('x')
        self.x = x

    def calculate_f_value(self, x):
        f = sym.lambdify([self.x], self.f)
        return f(x)
 
        
    def calculate_derivative(self, x):
        # Symbolic expression of the function - user input
        
        self.dfdx_expr = sym.diff(self.f, self.x)
        dfdx = sym.lambdify([self.x], self.dfdx_expr)
        
        return dfdx(x)
    
    def plot_function(self, a=-10, b=10):
        x = np.linspace(a,b,100)
        y = sym.lambdify([self.x], self.f)(x)
        
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        ax.spines['left'].set_position('center')
        ax.spines['bottom'].set_position('zero')
        ax.spines['right'].set_color('none')
        ax.spines['top'].set_color('none')
        ax.xaxis.set_ticks_position('bottom')
        ax.yaxis.set_ticks_position('left')
        plt.plot(x, y)
        plt.show()
        

    def find_solution(self, x0):
        iter_counter = 0
        f_value = self.calculate_f_value(x0)
        while abs(f_value) > self.eps and iter_counter < self.max_iter:
            try:
                x0 = x0 - float(f_value) / self.calculate_derivative(x0)
            except ZeroDivisionError:
                # Handling ZeroDivisonError - if the derivative of the initial guess is 0, increment x0 
                print("Error! - derivative zero for x = {}. Incrementing by 1...".format(x0))
                x0 += 1
            f_value = self.calculate_f_value(x0)
            iter_counter += 1
            
            print("X = {}, f(x) = {}, iteration #{}".format(x0, f_value, iter_counter))

        print("Solution found at {} with {} iterations".format(x0, iter_counter))
        if abs(f_value) > self.eps:
            print("Solution not found! Try changing the initial guess")
            iter_counter = -1
            x0 = None

        return x0
        
        
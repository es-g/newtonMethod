import sympy as sym
import numpy as np
import matplotlib.pyplot as plt

class Newton():
    def __init__(self, max_iter=1000):
        # Define x as mathematical symbol
        self.x_sym = sym.symbols('x')
        self.f_expr = self.x_sym ** 2
        self.max_iter = max_iter
        self.eps = 1.0e-12
        
        
    def calculate_f_value(self, x):
        f = sym.lambdify([self.x_sym], self.f_expr)
        return f(x)
        
    def calculate_derivative(self, x):
        # Symbolic expression of the function - user input
        
        dfdx_expr = sym.diff(self.f_expr, self.x_sym)
        dfdx = sym.lambdify([self.x_sym], dfdx_expr)
        
        return dfdx(x)
    
    def plot_function(self):
        x = np.linspace(-5,5,100)
        y = sym.lambdify([self.x_sym], self.f_expr)(x)
        
        plt.plot(x)
        
#         fig = plt.figure()
#         ax = fig.add_subplot(1, 1, 1)
#         ax.spines['left'].set_position('center')
#         ax.spines['bottom'].set_position('zero')
#         ax.spines['right'].set_color('none')
#         ax.spines['top'].set_color('none')
#         ax.xaxis.set_ticks_position('bottom')
#         ax.yaxis.set_ticks_position('left') 
#         plt.plot(x)
        
    def calculate_roots(self, x):
        iter_counter = 0
        f_value = self.calculate_f_value(x)
        print("Instantiated f_value {}".format(f_value))
        print("eps: {}".format(self.eps))
        while abs(f_value) > self.eps and iter_counter < self.max_iter:
            try:
                x = x - float(f_value) / self.calculate_derivative(x)
            except ZeroDivisionError:
                print ("Error! - derivative zero for x = ")
                sys.exit(1)     # Abort with error
            f_value = self.calculate_f_value(x)
            iter_counter += 1
            
            print("X value: {}, f_value: {}, iteration #{}".format(x, f_value, iter_counter))

        if abs(f_value) > self.eps:
            iter_counter = -1
        return x, iter_counter
        
        
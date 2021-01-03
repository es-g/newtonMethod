# Newton-Raphson Method
## Definition
The Newton-Raphson (N-R) method is one of the most widely used methods for root finding. 
It uses the idea that a continuous and differentiable function can be approximated by a straight line tangent to it.
It can be easily generalized to the problem of finding solutions of a system of non-linear equations, which is referred to as Newton's technique. 

In addition, it the technique is quadratically convergent as we approach the root. 

The most basic version starts with a 
- single-variable function *f* 
- defined for a real variable *x*,
- the function's derivative *f′*, 
- initial guess x0 for a root of *f*

If the function satisfies sufficient assumptions and the initial guess is close, then
```
x1 = x0- f(x0)/f'(x0)
 ```

## Disadvantages of Newton Method
* It is not guaranteed that Newton's method will converge if we select an x0 that is too far from the exact root. 
* We are not guaranteed convergence if our tangent line becomes parallel or almost parallel to the x-axis

# Motivation
This project is created for education purposes to demonstrate how Newton-Raphson method works 

# Installation

To install the package, simply run
```
pip install newtonMethod
```

# How to Use?
1. Import package
    ```
    from newtonMethod import Newton
    ```
2. Provide function and Instantiate object
    ```
    f = '2*x**2 - 50'
    newton = Newton(f)
    ```
3. Plot function to get the approximate idea of the solution
    ```
    newton.plot_function()
    ```
4. Find the closest solution (with the initial guess of, e.g., 1)
    ```
    newton.find_solution(1)
    ```

# Examples
Let's take function _2*x^2 - 50_
```
f = '2*x**2 - 50'
newton = Newton(f)
```
Let's plot the function to get the approximate idea of the solution(s)
```
# Specify intervals for x: from -50 to 50
newton.plot_function(-50, 50)
```

The plot looks like this: 
![Example 1](https://raw.githubusercontent.com/es-g/newtonMethod/master/newtonMethod/example_1.png "Logo Title Text 1")


Finally, let's find the solutions. We saw that the function crossed x-axis twice, i.e. there are 2 solutions - one positive and one negative.

Newton method does not find all solutions - it approximates the closest one. We'll start from the positive solution. 

We know that the technique is quadratically convergent, so even if we give initial guess that is way off, it should still converge pretty quickly. Let's find out!

```
newton.find_solution(1e4)
```
The output is as follows:
```
x = 5000.00125, f(x) = 49999975.00000313, iteration #1
x = 2500.0031249993754, f(x) = 12499981.250013284, iteration #2
x = 1250.0065624934377, f(x) = 3124982.8125533215, iteration #3
x = 625.0132811942192, f(x) = 781233.2033383282, iteration #4
x = 312.52664017212044, f(x) = 195295.8016345481, iteration #5
x = 156.30331667640885, f(x) = 48811.4536080915, iteration #6
x = 78.23163104937778, f(x) = 12190.37619329194, iteration #7
x = 39.275597441955966, f(x) = 3035.1451088451563, iteration #8
x = 19.956062498339314, f(x) = 746.4888608752494, iteration #9
x = 10.604407319150408, f(x) = 174.90690918090147, iteration #10
x = 6.480958834079521, f(x) = 34.00565481806677, iteration #11
x = 5.1692063724201756, f(x) = 3.4413890413387023, iteration #12
x = 5.002769360942944, f(x) = 0.05540255757893675, iteration #13
x = 5.000000766511454, f(x) = 1.5330230262122768e-05, iteration #14
x = 5.000000000000059, f(x) = 1.1723955140041653e-12, iteration #15
x = 5.0, f(x) = 0.0, iteration #16
Solution found at 5.0 with 16 iterations
```

So even though the initial guess was 10000, the solution was found after 16 iterations only!

We can now repeat the same with negative solution:
```
newton.find_solution(-1e4)
```
Solution was found at -5.0 with 16 iterations
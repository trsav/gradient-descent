# Gradient Descent optimization and plotting utility using finite difference approximations within Python

## Gradient Descent Background
Gradient descent is an optimization algorithm that locates the minimum of a function by utilizing the gradient of the function. 
 Quite simply every iteration the following is performed:

The gradient at the current 'position' is found. Here through the use of a finite difference approximation. 
The search direction is then set to be the negative of this gradient (for n dimensions this gradient is of course represented by an array of n length.)

A line search is then performed in order to find the optimum step size for the algorithm to take in the previously decided search direction.

The position of the current location is then updated in the direction of the negative gradient and with the step size calculated in the line search.

This procedure is then repeated until the gradient falls below a tolerance value.

### Finite Difference Approximation

Here, I've used the central difference method in order to approximate the derivative of the function at a certain point. For each dimension the derivative is calculated using the following formula.  <img src="https://github.com/TomRSavage/GradientDescent/blob/master/CentralDifference.png" width="200">

### Back-track Line Search
A line search is a 2 dimensional optimization problem that occurs within each iteration. On the y-axis is function value, and on the x-axis is step size (often referred to as alpha). As it is not desirable to find exactly the optimum step size (sometimes it is when you're reaching the end of the gradient descent, and looking to converge on an exact answer) a line search is performed. 

Implemented here is the back-track line search with the Armijo–Goldstein exit condition. Simply, the step size is varied and if it falls below a certain tolerance value (dictated by the Armijo-Goldstien condition) then the line search is terminated. The full explanation can be found on wikipedia (https://en.wikipedia.org/wiki/Backtracking_line_search)

### Momentum within Gradient Descent

A major addition to the effectiveness of gradient descent was the addition of momentum. Whilst simple gradient descent produces zig-zag movements, the addition of velocity allows for the point to gain momentum in certain directions, and converge on the minimum better. It is analogous to a ball rolling down the function space. 

This momentum term comes with yet another tunable parameter (along with the 3 in the back-track line search). This parameter is analogous to the friction experienced by the point, and regulates how much the velocity of the point effects it's overall path. 

Tuning these parameters can take the shape of a meta-optimization problem. 


 ### Effect of Mu on descent trajectory 

 <img align="center" src="https://github.com/TomRSavage/GradientDescent/blob/master/mu.gif" width="400">
 The above animation shows the effect of changing mu on the trajectory. Here the analogy of a ball rollilng down a hill becomes relatively clear, with friction of the function space being determined by mu. 


### Prerequisites

Python 3.0 is required. The GradientDescentUtils.py file must be in the same directory as the GradientDescent.py file in order to enable the utility to be used.

## Function Use
``` 
    INPUTS
    f           : function to be optimized
    X           : Coordinates of initial guess ([x1,x2,x3...])
    mu          : Coefficiant of 'friction'
    tol         : Tolerance criteria for gradient
    plot        : Set to =True to display a plot of the trajectory
    
    OUTPUTS
    The number of iterations it took to reach the solution, along with the coordinates at the solution.
```

## Example

Running the following:
```
f=Rosenbrock
initial_conds=[-1,0]
mu=0.5
tol=0.001
GradientDescent(f,initial_conds,mu,tol,plot=True)

```
Produces the following outputs:
```
Optimum at [0.999120450230318, 0.9982402306901063]
Function value at Optimum: 7.738161314471374e-07
Iterations: 978

```
<img align="center" src="https://github.com/TomRSavage/GradientDescent/blob/master/traj.png" width="400"> <img align="center" src="https://github.com/TomRSavage/GradientDescent/blob/master/func.png" width="400">

## Authors

* **Tom Savage** - *Initial work* - [TomRSavage](https://github.com/TomRSavage)

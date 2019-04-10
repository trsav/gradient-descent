import numpy as np
from GradientDescentUtils import *

def GradientDescent(f,X,mu,tol,plot=False):
    '''
    DESCRIPTION: 
    Gradient Descent optimization utilizing finite 
    difference approximations via the
    central difference method. As well as implementing 
    a back-strack line search for step size. 
    Finally momentum has been added 
    for a faster convergence.

    INPUTS
    f     :function to be optimized
    X     :initial guess
    mu    :coefficient of 'friction'
    tol   :tolerance for gradient (i.e.terminates if the gradient is less than tol)
    plot  : set to true to display a plot of trajectory and function value
    
    OUTPUTS
    optimum value, and function value at optimum
    as well as plot if plot=True
    
    '''
    d=len(X) #finding the number of dimensions 
    if d!=2 and plot==True: #displays error if plot wanted for 
                            # more than 2 dimensions
        print('Plotting only available for 2 Dimensions!')
        plot=False
    
    e=tol
    it_count=0 #initializing iteration counter
    a,Grad,func_val=BackTrackLineSearch(f,X) #calculting gradient and step size
    # at initial point 
    if plot==True: #setting up stores for plotting
        x_list = [X]
        f_list = [np.log(f(X))]
    v=np.zeros(d)
    while sum(abs(Grad[i]) for i in range(d)) > e:
        # while the gradient is greater than a certain 
        # tolerance... (i.e. minima has not been reached)
        it_count+=1 #increase iteration counter

        a,Grad,func_val=BackTrackLineSearch(f,X) #calculating gradient and step size
        print('Current function value: ',func_val)

        v[:]=(mu*v[:])-a*Grad[:] # calculate the velocity 
                                 # accounting for momentum
        X[:]=X[:]+v[:] # calculate the new position 

        if plot==True:
            x_list.append(X[:])
            f_list.append(np.log(f(X)))

    print('Optimum at', X) # after tolerance has been reached print results 
    print('Function value at Optimum:', f(X))
    print('Iterations:',it_count)

    if plot==True: #there is some repetition of code within the 
                   #plotting utility here, but it is needed to provide bounds
                   #for the contour plot
        x_list[0]=x_list[1]
        x_storeX=[0]*int(len(x_list)) 
        #creates empty array for x values
        x_storeY=[0]*int(len(x_list)) 
        #creates empty array for y values
        for i in range(len(x_list)): #separating x1 and x2 values
            x_storeX[i]=(x_list[i][0])
            x_storeY[i]=(x_list[i][1])
        x_lower=min(x_storeX)-min(x_storeX)*0.1
        x_higher=max(x_storeX)+max(x_storeX)*0.1
        y_lower=min(x_storeY)-min(x_storeY)*0.1
        y_higher=max(x_storeY)+max(x_storeY)*0.1

        trajplot(f,[[x_lower,x_higher],[y_lower,y_higher]]\
            ,x_list,f_list,contour=True)

    return 

f=Rosenbrock
initial_conds=[-1,0]
mu=0.5
tol=0.001
GradientDescent(f,initial_conds,mu,tol,plot=True)




            
            
            
        


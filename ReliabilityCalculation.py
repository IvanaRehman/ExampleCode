def reliability(r, t):
    RE = 1.268/r + 0.2/t + 1.028/(r*t) #this is the formula for calculating relative error
    rel = 1.089 / (1.089 + RE) #this is the formula for calculating the relative dependability index
    return rel

print(reliability(5, 20)) #here, a varied number of raters and tasks (respectively) can be entered in order to get different dependability indices values

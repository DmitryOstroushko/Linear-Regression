# Linear Regression 

## About project
This is the School 42 project.  
It implements a simple linear regression with a single feature - in this case, the mileage of the car.

## Model Training

The first program [trainer.py](https://github.com/DmitryOstroushko/Linear-Regression/blob/master/trainer.py) does train the model and saves coefficients for linear regression model to a file.  
Usage is: python trainer.py [-v] [-b] [-i] [-l] [-d] [-c] [-q]  
There are parameters of the script:  
* -v: If present verbosity mode is set. In verbosity mode the program prints debug messages in different colors: green - a successful operation, red - an unsuccessful operaion, and normal message. Default value is false.  
* -b: It is an auto break option. Default a program performs all a number of iterations which given as a paramenter. If option [-b] present a program processing can be stopped when a cost function current value is less then it on previous step.  
* -i: It is option to set a number of iterations (default is 500).  
* -l: It is option to set learning coefficient (default is 0.2).  
* -d: If present drawing mode is set. In this mode a script draws a curve for cost function and charts for prices: real vs prediction.  
* -c: If present counting will start from known coefficients from CSV file. Default it starts from zeros array.  
* -q: If present a model calculates mean-square deviation. Default it uses the linear formula.  


For this goal the script performs next:  
1. reads dataset file
and perform a linear regression on the data.
Once the linear regression has completed, you will save the variables theta0 and
theta1 for use in the first program.
You will be using the following formulas :
X
1 m−1
(estimateP rice(mileage[i]) − price[i])
tmpθ 0 = learningRate ∗
m i=0
tmpθ 1 = learningRate ∗
X
1 m−1
(estimateP rice(mileage[i]) − price[i]) ∗ milleage[i]
m i=0
I let you guess what m is :)
Note that the estimatePrice is the same as in our first program, but here it uses
your temporary, lastly computed theta0 and theta1.
Also, don’t forget to simultaneously update theta0 and theta1.




The first program will be used to predict the price of a car for a given mileage.
When you launch the program, it should prompt you for a mileage, and then give
you back the estimated price for that mileage. The program will use the following
hypothesis to predict the price :
estimateP rice(mileage) = θ 0 + (θ 1 ∗ mileage)
Before the run of the training program, theta0 and theta1 will be set to 0.



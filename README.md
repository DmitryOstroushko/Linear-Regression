# Linear Regression 

## About project
This is the School 42 project.  
It implements a simple linear regression with a single feature - in this case, the mileage of the car.

## Prediction

The first program [predict.py](https://github.com/DmitryOstroushko/Linear-Regression/blob/master/predict.py) predicts the price of a car for a given mileage.

When you launch the program, it should prompt you for a mileage, and then give
you back the estimated price for that mileage. The program will use the following
hypothesis to predict the price :
estimateP rice(mileage) = θ 0 + (θ 1 ∗ mileage)
Before the run of the training program, theta0 and theta1 will be set to 0.

## Model Training

The second program [trainer.py](https://github.com/DmitryOstroushko/Linear-Regression/blob/master/trainer.py) does train the model and saves coefficients for linear regression model to a file.  
Usage is: python trainer.py [-v] [-b] [-i] [-l] [-d] [-c] [-q]  
There are parameters of the script:  
* -v: If present verbosity mode is set. In verbosity mode the program prints debug messages in different colors: green - a successful operation, red - an unsuccessful operaion, and normal message. Default value is false.  
* -b: It is an auto break option. Default a program performs all a number of iterations which given as a paramenter. If option [-b] present a program processing can be stopped when a cost function current value is less then it on previous step.  
* -i: It is option to set a number of iterations (default is 500).  
* -l: It is option to set learning coefficient (default is 0.2).  
* -d: If present drawing mode is set. In this mode a script draws a curve for cost function and charts for prices: real vs prediction.  
* -c: If present counting will start from known coefficients from CSV file. Default it starts from zeros array.  
* -q: If present a model calculates mean-square deviation. Default it uses the linear formula.  

[trainer.py](https://github.com/DmitryOstroushko/Linear-Regression/blob/master/trainer.py) performs a stream of actions:
1. Reads a dataset file
2. Scales data: both features and target
3. Fits the model choosing cost function depending option `-q`.  
Result of a model fitting is array of theta variables (theta0 and theta1).  
In default mode the program uses the following formulas:  
_tmpθ[0] = learningRate * (1/m) * SUM(estimaPrice(mileage[i]) − price[i])_  
_tmpθ[1] = learningRate * (1/m) * SUM(estimaPrice(mileage[i]) − price[i]) ∗ milleage[i]), i=0,...,m-1_  
The __estimatePrice__ is the same as in [predict.py](https://github.com/DmitryOstroushko/Linear-Regression/blob/master/predict.py) program, but here it uses temporary, lastly computed theta0 and theta1.  
It updates theta0 and theta1 simultaneously.
4. Saves array of theta variables (theta0 and theta1) to a file to use it later in the second program




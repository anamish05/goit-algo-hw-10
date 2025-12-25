Function to integrate chosen is Bell curve (normal distribution):  

$$f(x) = e^{-x^2}$$  

Integral of f(x) was calculated for x=(0,2) using Monte-Carlo method and quad function from SciPy library.  
Results of the calculation were compared:  
1. 100 simulations with 15.000 points generated randomly - error (deviation of Monte-Carlo result from the quad result) is 0.1591%.
2. 100 simulations with 100.000 points generated randomly - error (deviation of Monte-Carlo result from the quad result) is 0.01399%.
3. 10.000 simulations with 15.000 points generated randomly - error (deviation of Monte-Carlo result from the quad result) is -0.00638% (however, much more time consuming than experiment 2).

As a conclusion, Monte-Carlo method can be quite precise and close to theoric calculation with larger number of simulations (rather than increasing number of points generated), 
however it is more time and resources consuming.

# xor_tensorflow
Flask application solving the xor problem
resolved with a 3 layers deep ANN using TensorFlow

This repository contain all the necessary python code required to build a ML application that is able to solve the xor problem. This application is purely done in an educative context.


# Build environment 

Using python3.6,
you need to install tensorflow

```
pip install tensorflow
```
or

```
python3.6 -m pip install tensorflow
```

# Execute

run this command in the main directory

```
python3.6 tensorflow_classification_web_app.py
```

then launche the application in your browser at http://localhost:5000/xor 

# The XOR problem 

The xor problem is a classic problem in ANN research. Given two inputs, the problem will be resolved by using a neural network to give an output of xor logic gates. 
0 0 -> 0
0 1 -> 1 
1 0 -> 1 
1 1 -> 0 

This problem is a classification problem, hence all the outputs should be known in advance. Therefore a supervised learning approach is used.

for more about the XOR problem : 
https://medium.com/@jayeshbahire/the-xor-problem-in-neural-networks-50006411840b


# Architecture of the ANN used 

the ANN used in this application to solve this problem is completly arbitrary, it was created for getting the most optimal results.
It can be further optimized.

2 inputs 
3 hidden layers ( 10 nodes, 20 node, 10 nodes ) 
1 output 

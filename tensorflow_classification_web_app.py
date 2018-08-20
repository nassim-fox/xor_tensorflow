
#####################################
##  by Nassim Bouhadouf 
##  https://www.linkedin.com/in/nassim-bouhadouf-a61804107/
##

import tensorflow as tf
from flask import Flask as f
from flask import redirect, url_for, request, render_template

app = f(__name__) 


def tensorflow_xor(xa,xb,epochs,rate) : 
    x = tf.placeholder(tf.float32,shape=(None,2)) 

    number_input = 2
    number_output = 1

    layer1_nodes = 10
    layer2_nodes = 20
    layer3_nodes = 10


    with tf.variable_scope("layer1",reuse=tf.AUTO_REUSE) : 
        weights = tf.get_variable(name="weights1",shape=[number_input,layer1_nodes],initializer=tf.contrib.layers.xavier_initializer())
        biases = tf.get_variable(name="biases1", shape=[layer1_nodes] , initializer=tf.zeros_initializer()) 
        l1 = tf.nn.relu(tf.matmul(x,weights)+biases)
    with tf.variable_scope("layer2",reuse=tf.AUTO_REUSE) : 
        weights = tf.get_variable(name="weights2",shape=[layer1_nodes,layer2_nodes],initializer=tf.contrib.layers.xavier_initializer()) 
        biases = tf.get_variable(name="biases2",shape=[layer2_nodes],initializer=tf.zeros_initializer())
        l2 = tf.nn.relu(tf.matmul(l1,weights)+biases)
    with tf.variable_scope("layer3",reuse=tf.AUTO_REUSE) : 
        weights = tf.get_variable(name="weigths3",shape=[layer2_nodes,layer3_nodes],initializer=tf.contrib.layers.xavier_initializer())
        biases = tf.get_variable(name="biases3",shape=[layer3_nodes],initializer=tf.zeros_initializer())
        l3 = tf.nn.relu(tf.matmul(l2,weights)+biases)
    with tf.variable_scope("output",reuse=tf.AUTO_REUSE) : 
        weights = tf.get_variable(name="weights4",shape=[layer3_nodes,number_output],initializer=tf.contrib.layers.xavier_initializer()) 
        biases = tf.get_variable(name="biases4",shape=[number_output],initializer=tf.zeros_initializer()) 
        predictions = tf.nn.relu(tf.matmul(l3,weights)+biases)
    with tf.variable_scope("cost",reuse=tf.AUTO_REUSE) : 
        y = tf.placeholder(tf.float32,shape=(4,1))
        cost = tf.reduce_mean(tf.squared_difference(y,predictions))
    with tf.variable_scope("train",reuse=tf.AUTO_REUSE) : 
        train = tf.train.AdamOptimizer(rate).minimize(cost)


    xi = [[0,0],[0,1],[1,0],[1,1]]
    yi = [[0],[1],[1],[0]]
    
    s = "" 
    
    print(" ************************************* {}".format(xa)+" {}".format(xb)) 
    
    with tf.Session() as session : 
            
         session.run(tf.global_variables_initializer()) 
         
         for i in range(epochs) : 
              session.run(train,feed_dict={x:xi,y:yi})
              if i % 1000 == 0 : 
                  print("Epoch {}".format(i))
                  c = session.run(cost,feed_dict={x:xi,y:yi})
                  print("cost {}".format(c))
                  
         print("complete")

         print(xa,xb) 
         
         print(session.run(predictions,feed_dict={x:[[xa,xb]]}))
         
         s = session.run(predictions,feed_dict={x:[[xa,xb]]})
         
    return [s[0][0],"{}".format(c)] 


epochs = 3000 
rate = 0.01 

@app.route("/cnfg",methods=['POST'])
def cnfg() : 
    global epochs , rate 
    if request.method == 'POST' : 
        epochs = int(request.form["epochs"])
        rate = float(request.form["rate"])
        return render_template("xor_web.html",epochs=epochs,rate=rate)
        
@app.route("/xor",methods=['GET','POST'])  
def xor() : 
    #tensorflow_xor() 
    #return "{}".format(tensorflow_xor()) 
    if request.method == 'POST' : 
      xa = request.form["a"] 
      xb = request.form["b"] 
      print(" xa !!!!!!!!!!!!!!!!!!! {}".format(xa)+" {}".format(xb))
      t = tensorflow_xor(xa,xb,epochs,rate)
      result = "{}".format(t[0])  
      cost = "{}".format(t[1])  
      return result+","+cost
    if request.method == 'GET' : 
      t = tensorflow_xor(0,0,epochs,rate)
      result = "{}".format(t[0])  
      cost = "{}".format(t[1])  
      return render_template("xor_web.html",result=result,cost=cost,epochs=epochs,rate=rate)
 
if __name__ == "__main__" : 
     app.run(debug=True) 
    


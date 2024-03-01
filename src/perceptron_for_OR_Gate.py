import numpy as np

class Perceptron():
  def __init__(self,inputs,bias=1.0):
    self.weights=(np.random.rand(inputs+1) * 2)-1
    self.bias=bias
  def run(self,x):
    sum=np.dot(np.append(x,self.bias),self.weights)
    return self.sigmoid(sum)
  def set_weights(self,*x_init):
    self.weights=np.array(x_init)
  def sigmoid(self,x):
    return 1/(1+np.exp(-x))
  
neuron=Perceptron()
neuron.set_weights(15,15,-10)

print("OR Gate : ")
print(f'0 0 : {neuron.run([0,0])}')
print(f'0 1 : {neuron.run([0,1])}')
print(f'1 0 : {neuron.run([1,0])}')
print(f'1 1 : {neuron.run([1,1])}')
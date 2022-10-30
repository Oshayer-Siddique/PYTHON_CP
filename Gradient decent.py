import numpy as np
def gradient_decent(x,y):
  m_curr = b_curr = 0
  itter = 1000
  n = len(x)
  learning_rate = 0.001
  for i in range(itter):
    y_predict = m_curr * x+ b_curr
    md = -(2/n)*sum(x*(y-y_predict))
    bd = -(2/n)*sum((y-y_predict))
    m_curr = m_curr - learning_rate * md
    b_curr = b_curr - learning_rate * bd
    print("m{},b{},itter{}".format(m_curr,b_curr,i))

  

x = np.array([1,2,3,4,5])
y = np.array([5,7,9,11,13])
gradient_decent(x,y)
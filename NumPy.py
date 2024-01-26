import numpy as np

# random vector of size 20 with float in the range 1-20
vec = np.random.uniform(1,20,20)
print("The original vector:" ,vec)

# reshape vector to 4 by 5
vec_reshaped = vec.reshape(4,5)
print("The reshaped vector before replace: ", vec_reshaped)

# replace max in each row by 0
vec_reshaped[np.arange(4),vec_reshaped.argmax(axis=1)] = 0
print("The reshaped vector after replace: " ,vec_reshaped)
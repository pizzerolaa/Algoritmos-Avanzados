import numpy as np

#with specific numbers 
arr = np.array([1.2, 2.4, 3.6, 4.8]) 
matriz = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
zeros = np.zeros((5, ), dtype=int) #arreglo o matriz de 0
ones = np.ones((2, ), dtype=int) #arreglo o matriz de 1
#print(ones)

#with sequences of numbers
seq_num = np.arange(5, 12) # [ 5  6  7  8  9 10 11]
#print(seq_num)

#with random numbers 
rand_num_bt50and100 = np.random.randint(low=50, high=101, size=(6, )) #ex: [84 92 55 76 63 92]
rand_num_float_bt0and1 = np.random.random((6, )) #ex: [0.8960666  0.17723881 0.51472545 0.9467938  0.00273154 0.91174138] ONLY of 0 to 1
#print(rand_num_float)

#math operations on NP operands
rand_float_bt2and3 = rand_num_float_bt0and1 + 2.0 #ex: [2.27109298 2.30223702 2.1091721  2.47590177 2.1486764  2.31649952]
rand_num_bt150and300 = rand_num_bt50and100 * 3 #ex: [297 225 237 186 255 174]
#print(rand_num_bt150and300)

#task 1
feature = np.arange(6, 21)
#print(feature)
label = (feature * 3) + 4
#print(label)

#task 2
noise = (np.random.random([15]) * 4) - 2
print(noise)
label = label + noise
print(label)

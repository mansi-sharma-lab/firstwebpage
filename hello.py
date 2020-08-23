#question 1 Import numpy as np
import numpy as np

# question 2 Make a python list => [1,2,3,4,5]
#Convert it into numpy array and print it
a = np.array([1,2,3,4])
print(a)

# question 3 Make a python matrix (3 x 3) => [[1,2,3],[4,5,6],[7,8,9]] 
# Convert it into numpy array and print it
x = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(x)

# question 4 Make a matrix (3 x 3) using built-in methods (like arange(), reshape() etc.):
#[ [1,3,5],
#[7,9,11],
#[13,15,17] ]
y = np.arange(1,18,2).reshape(3,3)
print(y)

# question 5 Create a numpy array with 10 random numbers from 0 to 10 (there should be few numbers greater than 1)
z = np.random.randint(0,10,(3,3))
print(z)

# question 6 Create numpy array => [1,2,3,4,5] and convert it to 2D array with 5 rows
m = np.array([1,2,3,4,5])
print(m)
m2 = np.reshape(m, (5,1))
print(m2)

# question 7 Print the shape of the above created array
print(m2.shape)

# question 8 Create a numpy array with 10 elements in it. Access and print its 3rd, 4th and 9th element.
m3 = np.array([4,6,8,7,9,15,31,7,21,35])
print(m3[2],m3[3],m3[8])

# question 9 Print alternate elements of that array
print(m3[0::2])

# question 10 Change last 3 elements into 100 using broadcasting and print
m4 = np.zeros((3,3))
m4[[3,3]] = [0,0]
print(m4)

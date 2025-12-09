#Create a program that replaces the values of the main diagonal with 1. Use a loop statement. 
# Print the modified array. Sample result:
matrix = [
   [0,0,0],
   [0,0,0],
   [0,0,0]
]

# Use a loop to iterate through the matrix and replace the main diagonal values with 1
# The main diagonal elements are those where the row index (i) equals the column index (i)
for i in range(len(matrix)):
    matrix[i][i] = 1

# Print the modified array in the desired format
for row in matrix:
    print(*(row))
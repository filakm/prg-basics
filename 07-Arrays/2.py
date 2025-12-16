def f(array2D):
    """
    Checks if the sum of each row equals the sum of its corresponding column 
    in a square 2D array.
    """
    # Assuming the array is square (same number of rows and columns)
    num_rows = len(array2D)
    
    # Iterate through each index i from 0 up to (but not including) num_rows
    for i in range(num_rows):
        
        # Calculate the sum of the current row (row i)
        row_sum = sum(array2D[i])
        
        # Calculate the sum of the corresponding column (column i)
        column_sum = 0
        for j in range(num_rows):
            # Add the element at row j, column i to the column sum
            column_sum += array2D[j][i]
            
        # If at any point the sums don't match, return False immediately
        if row_sum != column_sum:
            return False
            
    # If all rows matched their corresponding columns throughout the loop
    return True

print(f([[7,7,7],[7,8,7],[9,9,9]]))
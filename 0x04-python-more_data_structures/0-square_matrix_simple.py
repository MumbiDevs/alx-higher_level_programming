def square_matrix_simple(matrix=[]):
    """
    Computes the square value of all integers of a matrix.

    Args:
        matrix (list of list): A 2-dimensional array.

    Returns:
        list of list: A new matrix with the square values.
                     Same size as the input matrix.

    Description:
        This function computes the square value of all integers in the input
        matrix. It returns a new matrix where each value is the square of the
        corresponding value in the input matrix. The input matrix remains
        unmodified.
    """
    # Create a new matrix to store the square values
    new_matrix = []

    # Iterate over each row in the input matrix
    for row in matrix:
        # Create a new row to store the square values for the current row
        new_row = []

        # Iterate over each element in the current row
        for element in row:
            # Compute the square of the current element and append it to the new row
            new_row.append(element ** 2)

        # Append the new row to the new matrix
        new_matrix.append(new_row)

    # Return the new matrix
    return new_matrix

# Example usage:
if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    new_matrix = square_matrix_simple(matrix)
    print(new_matrix)
    print(matrix)

import numpy as np

data_outer = [[1, 2, 6], [2, 6, 8],
              [3, 4, 8], [7, 9, 0],
              [5, 6, 3], [6, 5, 6]]
output_outer = [4, 3, 7, 5, 8, 2]


# Generate polynomial hypersurface model.
# return list of lists of coefficients for each variable
# last element of each list will be the same (intercept)
# data is a list of lists of data points
# output is array of identifiers
def overfit(data, output):
    n_coefficients = len(data)
    dimensions = len(data[0])
    min_exponent = (n_coefficients - 1) // dimensions

    # n_exponents is an array of the number of terms for each variable.
    n_exponents = np.zeros(dimensions, dtype=np.int)
    n_exponents = n_exponents + min_exponent
    n_one_more_exponent = n_coefficients - 1 - dimensions * min_exponent
    for i in range(n_one_more_exponent):
        n_exponents[i] = n_exponents[i] + 1

    matrix = []
    for point in data:
        row = []
        for index, coordinate in enumerate(point):
            for exponent in range(n_exponents[index], 0, -1):
                row.append(coordinate ** exponent)
        row.append(1)
        matrix.append(row)

    return np.dot(np.linalg.inv(np.array(matrix)), output)


print(overfit(data_outer, output_outer))

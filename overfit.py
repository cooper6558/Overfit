import numpy as np

data_outer = [[1, 2, 6], [2, 6, 8],
              [3, 4, 8], [7, 9, 0],
              [5, 6, 3], [6, 5, 6]]
output_outer = [4, 3, 7, 5, 8, 2]


# Generate polynomial hypersurface model.
# data is a list of lists of data points
# output is array of identifiers
# returns a function with the model built in
def overfit(data, output):
    n_coefficients = len(data)
    dimensions = len(data[0])
    min_exponent = (n_coefficients - 1) // dimensions

    # n_exponents is an array of the number of terms for each variable.
    n_exponents = np.zeros(dimensions, dtype=np.int)
    n_exponents = n_exponents + min_exponent
    n_one_more_exponent = n_coefficients - 1 - dimensions * min_exponent
    for index in range(n_one_more_exponent):
        n_exponents[index] = n_exponents[index] + 1

    # exponents for each variable, for each term
    model_exponents = np.zeros((dimensions, n_coefficients), dtype=np.int)
    for axis in range(dimensions):
        leading_zeros = sum(n_exponents[:axis])
        for term in range(leading_zeros, leading_zeros+n_exponents[axis]):
            model_exponents[axis, term] = (leading_zeros +
                                           n_exponents[axis] - term)

    matrix = []
    for point in data:
        row = []
        for index, coordinate in enumerate(point):
            for exponent in range(n_exponents[index], 0, -1):
                row.append(coordinate ** exponent)
        row.append(1)
        matrix.append(row)
    model_coefficients = np.dot(np.linalg.inv(np.array(matrix)), output)

    def model(points):
        out = 0
        for a in range(n_coefficients):
            model_term = 1
            for b in range(dimensions):
                model_term = (model_term * points[b] ** model_exponents[b, a])
            model_term = model_term * model_coefficients[a]
            out = out + model_term

        return out

    return model


m = overfit(data_outer, output_outer)
for i in data_outer:
    print(m(i))

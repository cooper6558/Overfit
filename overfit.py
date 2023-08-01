import numpy as np
from import_data import import_data
from plot import plot


# Generate polynomial hypersurface model.
# data is a list of lists of data points
# output is array of identifiers
# returns a function with the model built in
# TODO: Consider allowing user input of polynomial structure
def overfit(data, output):
    n_coefficients = len(data)
    dimensions = len(data[0])
    min_exponent = (n_coefficients - 1) // dimensions

    # n_exponents is an array of the number of terms for each variable.
    n_exponents = np.zeros(dimensions, dtype=int)
    n_exponents = n_exponents + min_exponent
    n_one_more_exponent = n_coefficients - 1 - dimensions * min_exponent
    for index in range(n_one_more_exponent):
        n_exponents[index] = n_exponents[index] + 1

    # exponents for each variable, for each term
    model_exponents = np.zeros((dimensions, n_coefficients), dtype=int)
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


# [file_name] ["plot"] [start] [end] [y_start] [y_end] or
# [file_name] [data1] ... [data_n]
if __name__ == "__main__":
    import sys
    data_outer, output_outer = import_data(sys.argv[1])
    sys_model = overfit(data_outer, output_outer)
    if sys.argv[2].lower() == "plot":
        plot(sys_model, [(int(sys.argv[3]), int(sys.argv[4])),
                         (int(sys.argv[5]), int(sys.argv[6]))])
    else:
        test_case = []
        for data_index, _ in enumerate(data_outer[0]):
            test_case.append(float(sys.argv[data_index + 2]))
        print('Prediction: %f' % sys_model(test_case))

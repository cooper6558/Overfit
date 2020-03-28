# Emulates overfit.py as being run from console instead of command line

from overfit import overfit
from import_data import import_data

file_name = input('Data file name: ')
data_outer, output_outer = import_data(file_name)
model = overfit(data_outer, output_outer)
test_case = []
for i in range(1, len(data_outer[0]) + 1):
    value = input('Enter coordinate #%d: ' % i)
    test_case.append(int(value))
print('\nPrediction: %f' % model(test_case))

import csv


def import_data(file_name):
    data = []
    function_values = []

    with open(file_name, 'r') as file:
        reader = csv.reader(file, quoting=csv.QUOTE_NONNUMERIC)
        for line in reader:
            function_values.append(line[0])
            data.append(line[1:])

    return data, function_values

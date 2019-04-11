from solver.cost import cost_function
import json
import sys, getopt

INPUT_FILE_PATH = "tests/sample_data.json"
CAPACITIES = 18
USAGE = "main.py -i <inputfile> -c <capacities>"

def main(argv, input_file = INPUT_FILE_PATH, capacities = CAPACITIES):
    """ Main function """
    #TODO implement and call solver
    try:
        opts, args = getopt.getopt(argv,"hi:c",["help","inputfile=", "capacities="])

    except getopt.GetoptError:
        #command line syntax errors
        print(USAGE)
        sys.exit(2)

    #Options management    
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print("test.py -i <inputfile>")
            sys.exit()
        elif opt in ("-i", "--inputfile"):
            input_file = arg
        elif opt in ("-c", "--capacities"):
            capacities = arg

    data = input_reader(input_file)


def input_reader(input_file_path):
    """Read the input data file and create the computed data structure.
    :param inputs: input data file path
	:return data: the matrix of the input data with computed value
    """
    ids = []
    weights = []
    values = []
    with open(input_file_path) as f:
        items = json.load(f)
        for item in items:
            ids.append(item["id"])
            weights.append(item["weight"])
            # TODO modifiy the parameters of the cost_functions
            values.append(cost_function(item["x"], item["y"], item["z"]))
    data = [ids, weights, values]
    print(data)

if __name__ == "__main__":
    main(sys.argv[1:])
    
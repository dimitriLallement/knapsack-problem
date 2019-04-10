from solver.cost import cost_function
import json
import sys, getopt

INPUT_FILE_PATH = "tests/sample_data.json"
USAGE = "main.py -i <inputfile>"

def main(argv):
    """ Main function """
    #TODO implement and call solver
    input_file = INPUT_FILE_PATH
    try:
        opts, args = getopt.getopt(argv,"hi:",["inputfile="])

    except getopt.GetoptError:
        #command line syntax errors
        print(USAGE)
        sys.exit(2)

    #Options management    
    for opt, arg in opts:
        if opt == '-h':
            print('test.py -i <inputfile>')
            sys.exit()
        elif opt in ("-i", "--inputfile"):
            input_file = arg
    
    input_reader(input_file)

def input_reader(input_file_path):
    with open(input_file_path) as f:
        items = json.load(f)
        for item in items:
            print(item['id'])
    

if __name__ == "__main__":
    main(sys.argv[1:])
    
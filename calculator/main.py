import sys #import sys module from standard library
from pkg.calculator import Calculator # pkg is the folder name calculator is the file name Calculator is the class
from pkg.render import format_json_output # pkg is the folder name render is the file name and format_json_output is a function


def main():
    calculator = Calculator() # instantiates the Calculator class
    if len(sys.argv) <= 1: # ensures that there are no command line args after the script name
        print("Calculator App")
        print('Usage: python main.py "<expression>"')
        print('Example: python main.py "3 + 5"')
        return

    expression = " ".join(sys.argv[1:]) # creates a single string from the list of strings after the script name
    try: 
        result = calculator.evaluate(expression) # calls the evaluate method from the calculator class
        if result is not None: # see pkg > calculator.py > Calculator class > evaluate
            to_print = format_json_output(expression, result)
            print(to_print)
        else:
            print("Error: Expression is empty or contains only whitespace.")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
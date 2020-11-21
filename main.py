# Select a problem number to compute and compare the answer to a list of correct answers. 
import importlib

def select():
    try:
        selection = input('Select a problem number to compute: ')
        if len(selection) == 1: selection = '00' + selection
        if len(selection) == 2: selection = '0' + selection
        
        #import the problem file
        return importlib.import_module(selection)    
        
    except ModuleNotFoundError:
        print("File not found, try again.")
        return select()

if __name__ == "__main__":
    problem = select()
    print(problem.solve())
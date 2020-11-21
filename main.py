# Select a problem number to compute and compare the answer to a list of correct answers. 
import importlib, answers

def select():
    try:
        selection = input('Select a problem number to compute: ')
        if len(selection) == 1: selection = '00' + selection
        if len(selection) == 2: selection = '0' + selection
        
        return selection
        
    except ModuleNotFoundError:
        print("File not found, try again.")
        return select()

def check(problem):
    problemfile = importlib.import_module(problem)
    solution = problemfile.solve()
    print("Found solution: " + str(solution))
    
    if solution == answers.answerlist[problem]:
        print("The solution is correct.")        
    return

if __name__ == "__main__":
    problem = select()
    correctanswer = check(problem)
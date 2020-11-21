# Find the sum of even valued Fibonacci sequence numbers under four million.

def solve():
    term1 = 1
    term2 = 2
    answer = 0
    while term2 < 4000000:
        if term2 % 2 == 0: 
            answer += term2
        term1, term2 = term2, term1 + term2
        #nextterm = term1 + term2
        #term1 = term2
        #term2 = nextterm
    
    return answer
    
if __name__ == "__main__":
    print(solve())
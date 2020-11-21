# List all multiples of 3 or 5 below 1000

def solve():
    answer = sum(i for i in range(1000) if i % 3 == 0 or i % 5 == 0)
    return answer
    
if __name__ == "__main__":
    print(solve())
'''
@author: Rohith.
This is a sample exmaple to explain hill climbing algorithm. It is a heuristic search algorithm.
It is a type of generate-and-test type of algorithm.
1. Generate a random solution.
2. Evaluate/calculate the score.
3. Mutate the solution to lower the score and reach the global maximum.
This algorithm may not find the optimal solution to the given problem, but it will
give the best possible solution in a reasonable amount of time.

'''

import random
import string

# generate random solution
def generate_random_solution(length=13):
    return [random.choice(string.printable) for _ in range(length)]
# evaluate the distance metric between the expected solution and the generated random solution.
def evaluate(solution):
    target = list("Hello, World!")
    diff = 0
    for i in range(len(target)):
        s = solution[i]
        t = target[i]
        diff += abs(ord(s)-ord(t))
    return diff


# Mutate the solution 
def mutate_solution(solution):
    index = random.randint(0, len(solution)-1)
    solution[index]=random.choice(string.printable)


def main():
    best = generate_random_solution()
    best_score = evaluate(best)
    while True:
        print("Best score so far ",best_score, "Solution ","".join(best))
        if best_score == 0:
            break
        new_solution = list(best)
        mutate_solution(new_solution)
        score = evaluate(new_solution)
        if score < best_score:
            best = new_solution
            best_score = score

if __name__ == '__main__':
    print("Running the hill climbing algorithm.")
    main()

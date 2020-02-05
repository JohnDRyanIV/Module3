# Program: average_scores.py
# Author: John Ran
# Last modified: 2/5/2020

# The purpose of this program is to accept user inputs consisting of name, age, and
# scores and provide an output displaying a summary of that student and their average
# score


def average():
    # Get input for scores and determine average
    # Could scale by adding for loop iterating from 0 to less than
    # constant 'SCORES_TO_GRADE' and dividing result by 'SCORES_TO_GRADE'

    score1 = get_input(1)
    score2 = get_input(2)
    score3 = get_input(3)

    return (score1 + score2 + score3) / 3


def get_input(number):
    # Validate user input without bloating code in average
    score = float(input("Enter grade number%2.0f: " % number))

    while score < 0.0 or score > 100.0:     # Validating input
        score = float(input("Error: you must enter a valid score between 0 and 100: "))

    return score


def main():
    # Get the student's first and last name, print out their average scores
    last_name = input("Enter the student's last name: ")        # Accepting inputs
    first_name = input("Enter the student's first name: ")
    age = input("Enter the student's age: ")
    average_scores = average()
    print(last_name + ", " + first_name + " age: " + age + " average grade: %2.2f" % average_scores)
    return 0


if __name__ == '__main__':
    main()

#    Input    |  Expected Output  |  Actual Output  |
# 90,90,90    |        90         |        90       |
# 90,90,91    |       90.33       |       90.33     |
# 90,90,90.5  |       90.17       |       90.17     |

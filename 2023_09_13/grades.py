# 2023_09_06
'''
Andy Siegel
CSC 110
Project 2
This program has several functions which calculate the user's grade.
'''

def letter_grade(grade):
    '''
    This function returns the letter grade (A,B,C,D,E) given a float
    Args:
        grade: the user's grade as a float argument
        
    Returns:
        the letter grade.
    '''
    if grade > 100 or grade < 0:
        return "X"
    elif grade >= 90:
        return "A"
    elif grade >= 80:
        return "B"
    elif grade >= 70:
        return "C"
    elif grade >= 60: 
        return "D"
    else: 
        return "E"

def pass_or_fail(letter_grade):
    '''
    This function returns whether a given grade counts as a pass or a fail.
    Args:
        letter_grade: the user's grade as a single letter
    Returns:
        "Pass" or "Fail"
    '''
    if len(letter_grade) > 1:
        return "Error"
    elif letter_grade in "abcdABCD":
        return "Pass"
    else: 
        return "Fail"
    
def point_grade(score, total_points):
    '''
    This function returns the percentage score of an assignment given a user's score and the total points of the assignment
    Args:
        score: the user's points earned
        total_points: the total points of the assignment
    Returns:
        the percentage grade rounded to two decimals
    '''
    percent_grade = round(score/total_points * 100, 2) 
    return percent_grade

def get_grade_results(score, total_points):
    '''
    This function returns the full formatted grade of an assignment given a user's score and the total points of the assignment
    Args:
        score: the user's points earned
        total_points: the total points of the assignment
    Returns:
        "Your grade is" + the percentage grade with the letter grade and whether it was a pass or fail in parentheses
    '''
    percent_grade = point_grade(score, total_points)
    letter = letter_grade(percent_grade)
    p_or_f = pass_or_fail(letter)
    return f"Your grade is {percent_grade} ({letter} - {p_or_f})"



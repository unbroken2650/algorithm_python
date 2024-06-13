def calculate_gpa(grade):
    if grade[0] == "A":
        if grade[1] == "+":
            return 4.3
        elif grade[1] == "0":
            return 4.0
        elif grade[1] == "-":
            return 3.7
    elif grade[0] == "B":
        if grade[1] == "+":
            return 3.3
        elif grade[1] == "0":
            return 3.0
        elif grade[1] == "-":
            return 2.7
    elif grade[0] == "C":
        if grade[1] == "+":
            return 2.3
        elif grade[1] == "0":
            return 2.0
        elif grade[1] == "-":
            return 1.7
    elif grade[0] == "D":
        if grade[1] == "+":
            return 1.3
        elif grade[1] == "0":
            return 1.0
        elif grade[1] == "-":
            return 0.7
    elif grade == "F":
        return 0.0
    else:
        return None


# Example usage
grade = input("")
print(calculate_gpa(grade))

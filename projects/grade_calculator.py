def calculate_average(marks):
    return sum(marks) / len(marks)


def get_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"


print("=== Student Grade Calculator ===")

marks = []

for i in range(3):
    while True:
        try:
            mark = float(input(f"Enter subject {i + 1} marks: "))

            if 0 <= mark <= 100:
                marks.append(mark)
                break
            else:
                print("Please enter marks between 0 and 100.")

        except ValueError:
            print("Please enter a valid number.")


average = calculate_average(marks)
grade = get_grade(average)

print("\nAverage:", round(average, 2))
print("Grade:", grade)
def analyze_result(name, roll, marks):
    total = sum(marks)
    average = total / len(marks)

    if average >= 90:
        grade = "A"
    elif average >= 75:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 40:
        grade = "D"
    else:
        grade = "Fail"

    below_40 = []
    for i in range(len(marks)):
        if marks[i] < 40:
            below_40.append(f"Subject {i + 1}")

    print(f"Student: {name} (Roll: {roll})")
    print(f"Total: {total}, Average: {average}")
    print(f"Grade: {grade}")
    if below_40:
        print(f"Subjects below 40: {', '.join(below_40)}")
    else:
        print("Subjects below 40: None")
    print("-" * 40)


def main():
    num_students = 5
    for i in range(1, num_students + 1):
        print(f"Enter details for Student {i}:")
        name = input("Name: ")
        roll = int(input("Roll Number: "))

        marks = []
        for subj in range(1, 6):
            mark = float(input(f"Marks for Subject {subj}: "))
            marks.append(mark)

        print()
        analyze_result(name, roll, marks)
        print()


if __name__ == "__main__":
    main()

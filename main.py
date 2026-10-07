import numpy as np
import matplotlib.pyplot as plt


class Student:
    def __init__(self, student_id, name, age, semester, email):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.semester = semester
        self.email = email
        self.attendance = 0
        self.marks = {}

    def add_marks(self, subject, marks):
        self.marks[subject] = marks

    def set_attendance(self, attendance):
        self.attendance = attendance

    def calculate_total(self):
        return sum(self.marks.values())

    def calculate_percentage(self):
        total = self.calculate_total()
        return total / len(self.marks)

    def calculate_grade(self):
        percentage = self.calculate_percentage()

        if percentage >= 90:
            return "A+"
        elif percentage >= 80:
            return "A"
        elif percentage >= 70:
            return "B"
        elif percentage >= 60:
            return "C"
        elif percentage >= 50:
            return "D"
        else:
            return "F"

    def calculate_status(self):
        percentage = self.calculate_percentage()

        if percentage >= 50:
            return "Pass"
        else:
            return "Fail"

    def attendance_status(self):
        if self.attendance >= 75:
            return "Eligible"
        else:
            return "Short Attendance"

    def display_student(self):
        print("----------------------")
        print("\nStudent Details")
        print("----------------------")
        print("Student ID:", self.student_id)
        print("Name:", self.name)
        print("Age:", self.age)
        print("Semester:", self.semester)
        print("Email:", self.email)
        print("Attendance:", self.attendance, "%")
        print("Marks:", self.marks)
        print("Total Marks:", self.calculate_total())
        print("Percentage:", f"{self.calculate_percentage():.2f}", "%")
        print("Grade:", self.calculate_grade())
        print("Result:", self.calculate_status())
        print("Attendance Status:", self.attendance_status())


class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def display_all_students(self):
        for student in self.students:
            student.display_student()

    def search_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None

    def delete_student(self, student_id):
        student = self.search_student(student_id)

        if student:
            self.students.remove(student)
            print("Student deleted successfully.")
        else:
            print("Student not found.")


class PerformanceAnalyzer:
    def __init__(self, students):
        self.students = students

    def class_average(self):
        percentages = np.array(
            [student.calculate_percentage() for student in self.students]
        )

        return np.mean(percentages)

    def subject_averages(self):
        subjects = {}

        for student in self.students:
            for subject, marks in student.marks.items():

                if subject not in subjects:
                    subjects[subject] = []

                subjects[subject].append(marks)

        averages = {}

        for subject, marks in subjects.items():
            marks_array = np.array(marks)
            averages[subject] = np.mean(marks_array)

        return averages

    def highest_performer(self):
        percentages = np.array(
            [student.calculate_percentage() for student in self.students]
        )

        highest_index = np.argmax(percentages)

        return self.students[highest_index]

    def lowest_performer(self):
        percentages = np.array(
            [student.calculate_percentage() for student in self.students]
        )

        lowest_index = np.argmin(percentages)

        return self.students[lowest_index]

    def average_attendance(self):
        attendance = np.array(
            [student.attendance for student in self.students]
        )

        return np.mean(attendance)

    def grade_distribution(self):
        distribution = {}

        for student in self.students:
            grade = student.calculate_grade()

            if grade not in distribution:
                distribution[grade] = 0

            distribution[grade] += 1

        return distribution

    def pass_fail_distribution(self):
        results = []

        for student in self.students:
            if student.calculate_status() == "Pass":
                results.append(1)
            else:
                results.append(0)

        results = np.array(results)

        passed = np.sum(results == 1)
        failed = np.sum(results == 0)

        return {
            "Pass": passed,
            "Fail": failed
        }

    def marks_statistics(self):
        all_marks = []

        for student in self.students:
            for marks in student.marks.values():
                all_marks.append(marks)

        marks_array = np.array(all_marks)

        return {
            "Maximum": np.max(marks_array),
            "Minimum": np.min(marks_array),
            "Mean": np.mean(marks_array),
            "Standard Deviation": np.std(marks_array)
        }


student_manager = StudentManager()


student1 = Student(101, "Somya Gupta", 19, 3, "somya@gmail.com")
student1.add_marks("Python", 85)
student1.add_marks("DBMS", 78)
student1.add_marks("OOPS", 82)
student1.add_marks("Software Engineering", 74)
student1.add_marks("Communication Skills", 88)
student1.set_attendance(87)


student2 = Student(102, "Rahul Sharma", 20, 3, "rahul@gmail.com")
student2.add_marks("Python", 38)
student2.add_marks("DBMS", 29)
student2.add_marks("OOPS", 43)
student2.add_marks("Software Engineering", 45)
student2.add_marks("Communication Skills", 20)
student2.set_attendance(65)


student3 = Student(103, "Subham Thakur", 20, 3, "subham@gmail.com")
student3.add_marks("Python", 91)
student3.add_marks("DBMS", 88)
student3.add_marks("OOPS", 94)
student3.add_marks("Software Engineering", 86)
student3.add_marks("Communication Skills", 90)
student3.set_attendance(93)


student_manager.add_student(student1)
student_manager.add_student(student2)
student_manager.add_student(student3)


print("ALL STUDENTS")
print("====================")

student_manager.display_all_students()


print("\nSEARCHING FOR STUDENT")
print("====================")

student = student_manager.search_student(102)

if student:
    student.display_student()
else:
    print("Student not found.")


analyzer = PerformanceAnalyzer(student_manager.students)


print("\nPERFORMANCE ANALYSIS")
print("====================")

print("Class Average:", f"{analyzer.class_average():.2f}", "%")


print("\nSubject Averages:")

for subject, average in analyzer.subject_averages().items():
    print(subject + ":", f"{average:.2f}")


highest = analyzer.highest_performer()

print("\nHighest Performer:")
print(highest.name)
print("Percentage:", f"{highest.calculate_percentage():.2f}", "%")


lowest = analyzer.lowest_performer()

print("\nLowest Performer:")
print(lowest.name)
print("Percentage:", f"{lowest.calculate_percentage():.2f}", "%")


print("\nAverage Attendance:", f"{analyzer.average_attendance():.2f}", "%")


print("\nGrade Distribution:")
print(analyzer.grade_distribution())


print("\nPass/Fail Distribution:")
print(analyzer.pass_fail_distribution())


print("\nMarks Statistics:")

statistics = analyzer.marks_statistics()

for key, value in statistics.items():
    print(key + ":", f"{value:.2f}")

# MATPLOTLIB VISUALIZATIONS

# 1. BAR CHART - SUBJECT AVERAGES

subject_data = analyzer.subject_averages()

subjects = list(subject_data.keys())
subject_averages = list(subject_data.values())

plt.figure(figsize=(9, 5))

plt.bar(subjects, subject_averages)

plt.title("Average Marks by Subject")
plt.xlabel("Subjects")
plt.ylabel("Average Marks")
plt.xticks(rotation=25)
plt.ylim(0, 100)

plt.tight_layout()

# 2. PIE CHART - PASS/FAIL DISTRIBUTION

result_data = analyzer.pass_fail_distribution()

labels = list(result_data.keys())
values = list(result_data.values())

plt.figure(figsize=(6, 6))

plt.pie(
    values,
    labels=labels,
    autopct="%.1f%%",
    startangle=90
)

plt.title("Pass/Fail Distribution")

# 3. LINE CHART - STUDENT PERCENTAGES

student_names = [
    student.name for student in student_manager.students
]

student_percentages = [
    student.calculate_percentage()
    for student in student_manager.students
]

plt.figure(figsize=(9, 5))

plt.plot(
    student_names,
    student_percentages,
    marker="o"
)

plt.title("Student Performance")
plt.xlabel("Students")
plt.ylabel("Percentage")
plt.ylim(0, 100)

plt.grid(True)

plt.tight_layout()

# 4. HISTOGRAM - PERCENTAGE DISTRIBUTION

plt.figure(figsize=(8, 5))

plt.hist(
    student_percentages,
    bins=5
)

plt.title("Distribution of Student Percentages")
plt.xlabel("Percentage")
plt.ylabel("Number of Students")

plt.tight_layout()

plt.show()
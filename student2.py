class Student:
    """Represents a student."""

    def __init__(self, name, number):
        """All scores are initially 0."""
        self.name = name
        self.scores = [0] * number

    def getName(self):
        """Returns the student's name."""
        return self.name
  
    def setScore(self, i, score):
        """Sets the ith score, counting from 1."""
        self.scores[i - 1] = score

    def getScore(self, i):
        """Gets the ith score, counting from 1."""
        return self.scores[i - 1]
   
    def getAverage(self):
        """Finds the average score."""
        return sum(self.scores) / len(self.scores)
    
    def getHighScore(self):
        """Finds the highest score."""
        return max(self.scores)
 
    def __str__(self):
        """Returns student details as a string."""
        return "Name: " + self.name + "\nScores: " + " ".join(map(str, self.scores)) + "\nAverage: {:.2f}".format(self.getAverage()) + "\nHigh Score: " + str(self.getHighScore())

    # Comparison methods based on names
    def __eq__(self, other):
        """Checks if two students have the same name."""
        return self.name == other.name if isinstance(other, Student) else False

    def __lt__(self, other):
        """Checks if one student's name is less than another's name."""
        return self.name < other.name if isinstance(other, Student) else NotImplemented

    def __ge__(self, other):
        """Checks if one student's name is greater or equal to another's name."""
        return self.name >= other.name if isinstance(other, Student) else NotImplemented

def main():
    # Create a list of Student objects
    students = [
        Student("Jane", 5),
        Student("Mark", 5),
        Student("Sam", 5),
        Student("Marielle", 5),
        Student("Jon", 5)
    ]

    # Initialize scores
    sample_scores = [
        [88, 92, 86, 91, 95],
        [80, 85, 89, 91, 87],
        [70, 75, 93, 80, 90],
        [85, 82, 90, 92, 97],
        [78, 82, 85, 94, 88]
    ]

    for i, student in enumerate(students):
        for j in range(5):
            student.setScore(j + 1, sample_scores[i][j])

    # Manual shuffle 
    students[0], students[3] = students[3], students[0]
    students[1], students[4] = students[4], students[1]

    print("Shuffled List:")
    for student in students:
        print(student)
        print()

    # Sort the list
    students.sort()
    print("Sorted List:")
    for student in students:
        print(student)
        print()

    # Comparisons
    print("Name comparisons:")
    print("students[0] == students[1]:", students[0] == students[1])
    print("students[0] < students[1]:", students[0] < students[1])
    print("students[1] >= students[0]:", students[1] >= students[0])


if __name__ == "__main__":
    main()
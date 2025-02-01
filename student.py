""" 
File: student.py
Resources to manage a student's name and test scores.
"""

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
        return "Name: " + self.name + "\nScores: " + " ".join(map(str, self.scores))

    # Comparison methods added
    def __eq__(self, other):
        """Checks if two students have the same name."""
        return self.name == other.name if isinstance(other, Student) else False

    def __lt__(self, other):
        """Checks if one student's name is less than another's."""
        return self.name < other.name if isinstance(other, Student) else NotImplemented

    def __ge__(self, other):
        """Checks if one student's name is greater or equal to another's."""
        return self.name >= other.name if isinstance(other, Student) else NotImplemented

def main():
    student1 = Student("Jane", 5)
    student2 = Student("Jane", 5)
    student3 = Student("Mark", 5)

    print(student1)
    print(student2)
    print(student3)

    print("Name comparisons:")
    print("student1 == student2:", student1 == student2)
    print("student1 == student3:", student1 == student3)
    print("student1 < student2:", student1 < student2)
    print("student2 >= student1:", student2 >= student1)
    
if __name__ == "__main__":
    main()

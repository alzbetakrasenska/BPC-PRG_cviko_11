from sorting import random_numbers

class StudentsGrades:
    def __init__(self, scores):
        self.scores = scores

    def get_by_index(self, index):
        return self.scores[index]

    def count(self):
        return len(self.scores)

    def get_grade(self, index):
        points = self.scores[index]
        if points >= 90:
            return "A"
        elif points >= 80:
            return "B"
        elif points >= 70:
            return "C"
        elif points >= 60:
            return "D"
        elif points >= 50:
            return "E"
        else:
            return "F"


    def find(self, points):
        idx = []
        for i in range(len(results.scores)):
            if results.scores[i] == points:
                idx.append(i)
        return idx

    def get_sorted(self):
        num_copy = results.scores
        sorted_n = 0
        while sorted_n < len(num_copy):
            for i in range(1, len(num_copy)):
                if num_copy[i - 1] > num_copy[i]:
                    num_copy[i - 1], num_copy[i] = num_copy[i], num_copy[i - 1]
            sorted_n += 1
        return num_copy

    def main(self):
        print(results.count())
        for i in range(results.count()):
            grade = results.get_grade(i)
            print(f"Student {i}: {results.scores[i]} points - {grade}")
        print(results.get_sorted())



if __name__ == "__main__":
    results = StudentsGrades([85, 42, 91, 67, 50, 73, 100, 38, 58])

    # print(results.count())
    # print(results.get_by_index(2))
    # print(results.scores)
    # print(results.get_grade(7))
    # print(results.find(50))
    # print(results.get_sorted())
    # print(results.main())
    random_results = StudentsGrades(random_numbers(30, 0, 100))
    print(random_results.count())
    print(random_results.get_sorted())
 class Student:

    def __init__(self,roll,name,marks_list):
        self.roll = roll
        self.name = name
        self.marks_list = marks_list
        self.percent = None

    def calculate_percentage(self):
        summ = sum(self.marks_list)
        count = len(self.marks_list)
        percentage = summ//count
        self.percent = percentage      
        return percentage

    def find_grade(self):
        percent = self.percent
        if(percent >=  80):
            grade = 'A'
        elif(percent >= 60):
            grade = 'B'
        elif(percent >= 40):
            grade = 'C'
        else:
            grade = 'F'
        return grade
       
if __name__ == '__main__':
    roll=int(input())
    name=input()
    count=int(input())
    marks=[]
    for i in range(count):
        marks.append(int(input()))
    s=Student(roll,name,marks)
    print(s.calculate_percentage())
    print(s.find_grade())

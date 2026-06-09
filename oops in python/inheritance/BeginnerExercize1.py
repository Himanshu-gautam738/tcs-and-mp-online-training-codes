class Course:
    def getSchedule(self):
        print("General course schedule")

class OnlineCourse(Course):
    def getSchedule(self):
        print("Online Course: Self-paced videos + Live weekend sessions")

class OfflineCourse(Course):
    def getSchedule(self):
        print("Offline Course: Classroom Monday to Friday 10 AM")

class HybridCourse(Course):
    def getSchedule(self):
        print("Hybrid Course: Online videos + Weekend classroom")

courses = [
    OnlineCourse(),
    OfflineCourse(),
    HybridCourse()
]

for c in courses:
    c.getSchedule()
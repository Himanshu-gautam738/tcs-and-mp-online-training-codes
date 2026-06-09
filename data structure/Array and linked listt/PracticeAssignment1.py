courses = []
def add_course(course_id, name, instructor, credits, max_enroll):
    courses.append({
        "CourseID": course_id,
        "CourseName": name,
        "Instructor": instructor,
        "Credits": credits,
        "MaxEnrollment": max_enroll,
        "Enrolled": 0
    })

def update_course(course_id, instructor=None, credits=None):
    for c in courses:
        if c["CourseID"] == course_id:
            if instructor:
                c["Instructor"] = instructor
            if credits:
                c["Credits"] = credits

def check_availability(course_id):
    for c in courses:
        if c["CourseID"] == course_id:
            return c["MaxEnrollment"] - c["Enrolled"]
    return -1

class Node:
    def __init__(self, student_id, course_id, grade, status):
        self.student_id = student_id
        self.course_id = course_id
        self.grade = grade
        self.status = status
        self.next = None

class AcademicProgress:
    def __init__(self):
        self.head = None

    def add_record(self, student_id, course_id, grade, status):
        new = Node(student_id, course_id, grade, status)
        new.next = self.head
        self.head = new

    def update_grade(self, student_id, course_id, new_grade):
        curr = self.head
        while curr:
            if curr.student_id == student_id and curr.course_id == course_id:
                curr.grade = new_grade
                return
            curr = curr.next

    def remove_course(self, student_id, course_id):
        curr = self.head
        prev = None
        while curr:
            if curr.student_id == student_id and curr.course_id == course_id:
                if prev:
                    prev.next = curr.next
                else:
                    self.head = curr.next
                return
            prev = curr
            curr = curr.next

    def display(self):
        curr = self.head
        while curr:
            print(curr.student_id, curr.course_id, curr.grade, curr.status)
            curr = curr.next

add_course(101, "Data Structures", "Dr. Sharma", 4, 60)
add_course(102, "Algorithms", "Dr. Mehta", 4, 50)

update_course(102, instructor="Dr. Rao")

print("Seats available in Data Structures:", check_availability(101))


progress = AcademicProgress()

progress.add_record(1, 101, "A", "Completed")
progress.add_record(1, 102, "B", "Ongoing")

progress.update_grade(1, 102, "A")
progress.remove_course(1, 101)

print("Academic Progress:")
progress.display()

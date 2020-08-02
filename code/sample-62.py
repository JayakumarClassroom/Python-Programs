#Functions

def course_info(course_name, student_number, course_hours):
	course ={
		'Course Name':course_name.title(),
		'Student Number': student_number,
		'Course Hourse': course_hours
	}
	return course
	
def drop(course):
	course['Student Number'] -= 1
	print(f"Droping Student from {course['Course Name']}.")
	print(f"After Dropped Student Number is {course['Student Number']}.")
	

python = course_info("Python Programming", 65, 3)
for k,v in python.items():
	print(f'{k}\t:  {v}')	
	
drop(python)
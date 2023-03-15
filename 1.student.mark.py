students ={}
courses ={}

        
def student_input(s, ID, name, DOB) :
    s[ID]={"name":name, "DOB": DOB}
    
def student_input_from_user(s) :
    s[input("ID:")]= {"name": input("name:"), "DOB": input("DOB:")}
    
def course_input(c, ID, name) :
    c[ID]={"name":name}
    
def course_input_from_user(c) :
    c[input("ID:")]={"name":input("name:")}
    
def mark_input(c,ID, name, mark) :
    c[ID].update({name: mark})

def mark_input_from_user(c) :
    m={input("name: "): int(input("Mark: "))}
    c[input("course ID: ")].update(m)

print("add student:")
student_input_from_user(students)
print("add course: ")
course_input_from_user(courses)
print("add mark:  ")
mark_input_from_user(courses)


print(courses)
print(students)
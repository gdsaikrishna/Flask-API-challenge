"""Routines associated with the application data.
"""
import json
courses = {}

def load_data():
    """Load the data from the json file.
    """
    f = open('json/course.json',)
    data = json.load(f) 
    for i in data: 
        #print(i) 
        if i["id"] not in courses:
            courses[i["id"]] = i
    #print(len(courses))
    f.close() 
    return courses

def get_course_by_id(id):
    #courses = load_data()
    return courses[id]

def add_course(request_data):
    id = max(courses.keys())+1
    y = {"id":id}
    course = request_data
    course["id"] = id
    #print(request_data.update(y))
    courses[id] = course
    return courses[id]

def update_course_by_id(id,request_data):
    courses[id] = request_data
    return courses[id]

def delete_course_by_id(id):
    del courses[id]

def get_courses_by_words(string):
    words = string.split(",")
    set_of_courses = []
    for id, course in courses.items():
        if any(word in course["title"] for word in words):
            set_of_courses.append(courses[id])
    return set_of_courses

def get_all_courses():
    set_of_courses = []
    for id, course in courses.items():
        set_of_courses.append(course)
    return set_of_courses




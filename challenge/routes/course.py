"""Routes for the course resource.
"""

from run import app
from flask import request, jsonify, Response
from http import HTTPStatus
import data, math
from data import *


@app.route("/course/<int:id>", methods=['GET'])
def get_course(id):
    """Get a course by id.

    :param int id: The record id.
    :return: A single course (see the challenge notes for examples)
    :rtype: object
    """

    """
    -------------------------------------------------------------------------
    Challenge notes:
    -------------------------------------------------------------------------   
    1. Bonus points for not using a linear scan on your data structure.
    """
    # YOUR CODE HERE
    #course = get_course_by_id[id]
    try:
        return jsonify({"data":get_course_by_id(id)})
    except KeyError:
        return jsonify({"message":f"Course {id} does not exist"})


@app.route("/course", methods=['GET'])
def get_courses():
    """Get a page of courses, optionally filtered by title words (a list of
    words separated by commas".

    Query parameters: page-number, page-size, title-words
    If not present, we use defaults of page-number=1, page-size=10

    :return: A page of courses (see the challenge notes for examples)
    :rtype: object
    """

    """
    -------------------------------------------------------------------------
    Challenge notes:
    ------------------------------------------------------------------------- 
    1. Bonus points for not using a linear scan, on your data structure, if
       title-words is supplied
    2. Bonus points for returning resulted sorted by the number of words which
       matched, if title-words is supplied.
    3. Bonus points for including performance data on the API, in terms of
       requests/second.
    """
    # YOUR CODE HERE
    request_data = request.get_json
    title = request.args.get("title-words")
    page_size = 5
    if(request.args.get("page-size")!=None):
        if(request.args.get("page-size").isdigit()):
            page_size = int(request.args.get("page-size"))
    page_number = 1
    if(request.args.get("page-number")!=None):
        if(request.args.get("page-number").isdigit()):
            page_number =int(request.args.get("page-number"))
    if(title != None):
        courses_list = get_courses_by_words(title)
    else:
        courses_list = get_all_courses()
    #print(courses_list)
    dic = {}
    dic["page_count"] = math.ceil(len(courses_list)/page_size)
    dic["page_number"] = page_number
    dic["page_size"] = page_size
    dic["record_count"] = len(courses_list)
    return jsonify({"data":courses_list[(page_number-1)*page_size:page_number*page_size],"meta-data": dic})



@app.route("/course", methods=['POST'])
def create_course():
    """Create a course.
    :return: The course object (see the challenge notes for examples)
    :rtype: object
    """

    """
    -------------------------------------------------------------------------
    Challenge notes:
    -------------------------------------------------------------------------
    1. Bonus points for validating the POST body fields
    """
    # YOUR CODE HERE
    request_data = request.get_json()
   # print(request_data)
    course = add_course(request_data)
    return jsonify({"data":course})


@app.route("/course/<int:id>", methods=['PUT'])
def update_course(id):
    """Update a a course.
    :param int id: The record id.
    :return: The updated course object (see the challenge notes for examples)
    :rtype: object
    """

    """
    -------------------------------------------------------------------------
    Challenge notes:
    -------------------------------------------------------------------------
    1. Bonus points for validating the PUT body fields, including checking
       against the id in the URL

    """
    # YOUR CODE HERE
    request_data = request.get_json()
    course = update_course_by_id(id,request_data)
    try:
        return jsonify({"data":course})
    except KeyError:
        return jsonify({"message":"The id does match the payload"})

@app.route("/course/<int:id>", methods=['DELETE'])
def delete_course(id):
    """Delete a course
    :return: A confirmation message (see the challenge notes for examples)
    """
    """
    -------------------------------------------------------------------------
    Challenge notes:
    -------------------------------------------------------------------------
    None
    """
    # YOUR CODE HERE
    delete_course_by_id(id)
    try:
        return jsonify({"message": "The specified course was deleted"})
    except KeyError:
        return jsonify({"message": "Course 201 does not exist"})


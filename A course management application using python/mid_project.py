import json

filename = 'course.json'


def add_course():

    code = input("Enter the course code:")
    title = input("Enter the course title:")
    credit = input("Enter the Course credit:")
    precode = input("Enter the Prerequisites Course code, Enter 'empty' if there is no prerequisites:")

    keyword = precode

    with open(filename, 'r') as file:
        info = json.load(file)

        flag = 0

        data = {}

        data["code"] = code
        data["title"] = title
        data["credit"] = credit
        data["pre_code"] = precode

        for row in info:
            code = row["code"]
            if keyword == code or keyword=="empty":

                with open(filename, 'r') as file:
                    info = json.load(file)

                    info.append(data)


                with open(filename, 'w') as file:
                    json.dump(info, file, indent=2)

                file.close()

                print("Success! The course successfully added")
                flag = 1
                break
        if flag == 0:
            print(
                "\nSorry!The Prerequisites Course is not exists. Please add the course first.\n")



def display_course():

    with open(filename, 'r') as file:
        info = json.load(file)

        for row in info:
            code = row["code"]
            title = row["title"]
            credit = row["credit"]
            pre_code = row["pre_code"]

            print("\nCourse Code:"+code)
            print("Course Title:"+title)
            print("Course Credit:"+credit)
            print("Prerequisite Course Code:"+pre_code)
            print("\n")
    file.close()




def update_course():
    keyword = input("\nEnter a course code for Update:")

    with open(filename, 'r') as file:
        info = json.load(file)

        flag = 0

        for idx, row in enumerate(info):
            code = row["code"]
            title = row["title"]
            credit = row["credit"]
            pre_code = row["pre_code"]

            if keyword == row["code"]:
                print("\nSelected Course Information below:\n")
                print("Course Code:"+code)
                print("Course Title:"+title)
                print("Course Credit:"+credit)
                print("Prerequisite Course Code:"+pre_code)
                print("\n")

                print("Enter the course information for update:\n")

                info[idx]['code'] = input("Enter Course Code:")
                info[idx]['title'] = input("Enter Course Title:")
                info[idx]['credit'] = input("Enter Course Credit:")
                info[idx]['pre_code'] = input(
                    "Enter Prerequisite Course Code:")

                with open(filename, 'w') as file:
                    json.dump(info, file, indent=2)

                file.close()
                flag = 1
                break
        if flag == 0:
            print("\nSorry!No match found. Please add the course.\n")


def search_course():
    keyword = input("\nEnter a course code for search:")

    with open(filename, 'r') as file:
        info = json.load(file)

        flag = 0

        for row in info:
            code = row["code"]
            title = row["title"]
            credit = row["credit"]
            pre_code = row["pre_code"]

            if keyword == code:
                print("\nCourse Code:"+code)
                print("Course Title:"+title)
                print("Course Credit:"+credit)
                print("Prerequisite Course Code:"+pre_code)
                print("\n")
                flag = 1
                break
        if flag == 0:
            print("\nSorry! Found no matches. Add the course, please.\n")
    file.close()





def delete_course():

    keyword = input("\nTo remove, enter the course code:")

    with open(filename, 'r') as file:
        info = json.load(file)

        flag = 0

        for idx, row in enumerate(info):

            if keyword == row['code']:
                info.pop(idx)
                with open(filename, 'w') as file:
                    json.dump(info, file, indent=2)

                file.close()
                flag = 1
                break
        if flag == 0:
            print("\nSorry!No match found.\n")








while True:
    print("Welcome to course management application")

    print("Enter 'A' to add a new course")
    print("Enter 'U' to update an existing course")
    print("Enter 'D' to delete an existing course")
    print("Enter 'Y' to display information about all the courses")
    print("Enter 'S' to search pick a certain course and show all the course information")
    print("Enter 'Q' to quit")

    inp = input("Enter Button:")

    if inp == "A":
        add_course()

    elif inp == "U":
        update_course()

    elif inp == "D":
        delete_course()

    elif inp == "Y":
        display_course()

    elif inp == "S":
        search_course()

    elif inp == "Q":
        break
    else:
        print("\nSorry! You pressed the incorrect button.")

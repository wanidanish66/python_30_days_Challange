# This program is a contact book that allows users to store the name and phone number of students. 
# The contact information is saved in a text file called "contact_book.txt". 
# The user is prompted to enter the name and phone number of the student, 
# which is then written to the file and stored in a dictionary for easy access.

def student_contact(name, phone_number):
    with open("contact_book.txt", "a") as file:
        file.write(name + " : " + phone_number + "\n")
        store_contact = {}            # this dictionary will be used to store the contact information of the students
        store_contact[name] = phone_number      # the name of the student will be the key and the phone number will be the value in the dictionary
        return store_contact
print("welcome to the contact book program")
print("want to add a contact to the book")
if input("enter yes or no: ").lower() == "yes":
    student_contact(input("enter the name of the student: "), input("enter the phone number of the student: ")) 
else:
    print("thank you for using the contact book program")
# This is Muhammad Rizwan Lab 8 Utility File for COMPUTING I
def calculate_letter_grade(score): # define letter grade function
if score >= 90: # if score is greater than or equal to 90
return 'A'; # return A
elif score >= 80: # if score is greater than or equal to 80
return 'B'; # return B
elif score >= 70: # if score is greater than or equal to 70
return 'C'; # return C
elif score >= 60: # if score is greater than or equal to 60
return; 'D'; # return D
else: # otherwise
return 'F'; # return f
def print_num_of_students(): # define print function
num_students = userinput_for_students(); # number of students is equal to the
user input for students function
return num_students; # return number of students
def userinput_for_students(): # define user input for students function
num_students = int(input("Enter the number of students (more than 5 only): "));
# number of students is equal to giving an input prompt of entering the number of
students
if num_students < 5: # if the inputted value is less than 5
print('Invalid input, please try again.'); # it is an invalid input
return userinput_for_students(); # keep loop going until valid input
return int(num_students); # return the number of students value
def studentinput_values(num_students): #define studentinput_values function
studentfirstlast_grade = {}; #calling the studentfirstlast_grade dictionary
studentfirstlast_grade_searchresult = {};
student_data = []; # student data array is open
for i in range(num_students): # for i in the range of number of students
name = input(f"Enter full name of student {i + 1}: "); #name is equal to an
input value which has a prompt of first name of student
score = int(input(f"Enter score for student {name}: ")); #score is equal to
an input value which has a prompt of enter score for student
studentfirstlast_grade[name] = score; #studentfirstlast_grade with name
parameter
print(studentfirstlast_grade); #print studentfirstlast_grade
mykey = input("Search by full name: "); #mykey variable is equal to input value
"Search by full name: "
myvalresult= studentfirstlast_grade.get(mykey); #my value result is equal
studentfirstlast_grade, whilst getting the key
studentfirstlast_grade_searchresult[mykey] = myvalresult; #adding search by key
result in new structure
print(myvalresult); #print studentfirstlast_grade and get the input from
'mykey' variable
myval = input("Search by score: "); #myval is equal to input "Search by score:
"
key_list = list(studentfirstlast_grade.keys()); #key_list is equal to all the
keys of the studentfirstlast_grade dictionary
val_list = list(studentfirstlast_grade.values()); #val_list is equal to all the
values of the studentfirstlast_grade dictionary
position = val_list.index(int(myval)); #position is equal to index of input
value (myval) in val_list
mykeyresult = key_list[position];
studentfirstlast_grade_searchresult[mykeyresult] = myval; #adding search by val
result in new structure
print(mykeyresult); #print result
print(studentfirstlast_grade_searchresult); #printing new structure values

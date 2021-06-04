import csv
def  write_into_csv(info_list):
     with open("student_info.csv",'a',newline=" ") as csv_file:
         writer = csv.writer(csv_file)
         writer.writerow(info_list)


con = True

while  (con):
    student_info =input("enter the student information in the following format (name age  contactnumber email_id :")
    print("information entered by you:"+ student_info)
    student_info_list = student_info.split(' ')
    print("entered splitup information is:" + str(student_info_list))

    write_into_csv(student_info_list)

    Check1= input("enter (yes/no) to continue to enter data of another student:")
    if  Check1=="yes":
        con = True
    elif Check1=="no":
        con = False
    

import os , datetime
os.system("cls")
import sqlite3
import string
from random import *
from tabulate import tabulate
connect = sqlite3.Connection("User.db")
curs = connect.cursor()
curs.execute(''' CREATE TABLE IF NOT EXISTS Boss(
                Name text,
                Lastname text,
                User_Name text,
                Password text,
                Age intiger,
                Level text,
                Phone_number text,
                Email text,
                Pay intiger,
                Join_Date text
                )''')
curs.execute(''' CREATE TABLE IF NOT EXISTS Assistant(
                Name text,
                Lastname text,
                User_Name text,
                Password text,
                Age intiger,
                Level text,
                Phone_number text,
                Email text,
                Pay intiger,
                Join_Date text
                )''')
curs.execute(''' CREATE TABLE IF NOT EXISTS Employee(
                Name text,
                Lastname text,
                User_Name text,
                Password text,
                Age intiger,
                Level text,
                Phone_number text,
                Email text,
                Pay intiger,
                Join_Date text
                )''')
#----------------------------------------------------------------------------
class Employee():
    employee_number = 0
    def __init__(self,post,name,lastname,age,level,phone_number,pay):
        ##User Information
        self.post = post
        self.name = name
        self.lastname = lastname
        self.age = age
        self.level = level
        self.__phone = str(phone_number)
        self.__pay = pay
        Employee.employee_number +=1
        # Making User_Name For User
        curs.execute(f"SELECT User_Name FROM {self.post}")
        user_names = curs.fetchall()
        x = randint(100,1000)
        if f"{self.name}{x}" not in user_names: self.user_name = f"{self.name}{x}"
        else:
            while f"{self.name}{x}" in user_names:
                if f"{self.name}{randint(100,1000)}" not in user_names: self.user_name = f"{self.name}{x}"
        self.email = f"{self.user_name}@company.com"
        # Making Password For User
        ch = string.ascii_uppercase + string.digits + string.ascii_uppercase
        psw = str("".join(choice(ch) for x in range(randint(6,8))))
        curs.execute(f"SELECT Password FROM {self.post}")
        psw_check = curs.fetchall()
        if (psw,) not in psw_check: self.psw = psw
        else:
            while (psw,) in psw_check:
                psw = str("".join(choice(ch) for x in range(randint(6,8))))
                if (psw,) not in psw_check: self.psw = psw
        # Cheking User_Name , Phone_Number , Email
        if self.__phone not in Item_Getter(["Boss" , "Assistant" , "Employee"],["Phone_Number"]) and self.email not in Item_Getter(["Boss" , "Assistant" , "Employee"],["Email"]) and self.lastname not in Item_Getter(["Boss" , "Assistant" , "Employee"],["Lastname"]):
            curs.execute(f"INSERT INTO {self.post} VALUES (:Name,:Lastname,:User_Name,:Password,:Age,:Level,:Phone_Number,:Email,:Pay,:Join_Date)",{"Name":self.name,"Lastname":self.lastname,"User_Name":self.user_name,"Password":self.psw,"Age":self.age,"Level":self.level,"Phone_Number":self.__phone,"Email":self.email,"Pay":self.__pay,"Join_Date":str(datetime.date.today())})
            connect.commit()
        elif self.__phone in Item_Getter(["Boss" , "Assistant" , "Employee"],["Phone_Number"]) : print("Phone number Already Exist!!!")
        elif self.email in Item_Getter(["Boss" , "Assistant" , "Employee"],["Email"]) : print("Email Already Exist!!!")
        elif self.lastname in Item_Getter(["Boss" , "Assistant" , "Employee"],["Lastname"]) : print("User Already Exist!!!")
#----------------------------------------------------------------------------
class Manager():
    def __init__(self,usn,psw , post):
        self.user_name = usn
        self.password = psw
        self.post = post
        self.access = False
        if self.post == "Boss": self.access = True
    def self_info_edit(self): Manager_self_info_Edit(self)
    def add_new_user(self) : Manager_Add_New_User(access=self.access)
    def edit_user(self): Manager_edit_user(self)
    def delete_user(self): Manager_delete_user(self)
    def resume(self): Manager_Resume(self)
    def exit(): Manager_Exit()
    def all_user(): Show_All_Employees()
#-----------
class Boss(Manager):
    def __init__(self, usn, psw, post):
        super().__init__(usn, psw, post)
        print(f"Number Of Users Added By This Acount: {Employee.employee_number}\n")
        self.select = int(input("What do you want?\nEdit_Self_Information : 1\nAdd_New_User : 2\nEdit_User : 3\nDelet_User : 4\nEXIT : 5\n"))
        if self.select == 1 : self.self_info_edit()
        if self.select == 2: self.add_new_user()
        if self.select == 3 : self.edit_user()
        if self.select == 4 : self.delete_user()
        if self.select == 5: Manager.exit()
        self.resume()
#-----------
class Assistant(Manager):
    def __init__(self, usn, psw, post):
        super().__init__(usn, psw, post)
        print(f"Number Of Users Added By This Acount: {Employee.employee_number}\n")
        self.select = int(input("What do you want?\nEdit_Self_Information : 1\nAdd_New_User : 2\nEdit_User : 3\nEXIT : 4\n"))
        if self.select == 1 : self.self_info_edit()
        if self.select == 2: self.add_new_user()
        if self.select == 3 : self.edit_user()
        if self.select == 4 : Manager.exit()
        self.resume()
#-----------
class Employee__(Manager):
    def __init__(self, usn, psw, post):
        super().__init__(usn, psw, post)
        self.select = int(input("What Do You Want?\nEdit Self_Information : 1\nEXIT : 2\n"))
        if self.select == 1 : self.self_info_edit()
        if self.select == 2: Manager.exit()
        self.resume()
#----------------------------------------------------------------------------
# The Following Function Is Used In Some Parts Of The Program
def Item_Getter(table , column):
    getx = list()
    for item in table :
        for valuse in column:
            curs.execute(f"SELECT {valuse} FROM {item}")
            getx = curs.fetchall()
    for i in getx: getx[getx.index(i)] = i[0]
    return getx
#----------------------------------------------------------------------------
# Manager Class Methods
def Manager_self_info_Edit(self):
    selfedit = int(input("What Self_Information do you want to edit?\nAge : 1\nPhone_number : 2\n"))
    if selfedit == 1 :
        internewage = int(input("Inter New Age : "))
        curs.execute(f"UPDATE {self.post} SET Age = :newage WHERE User_Name = :interuser",{"newage" : internewage ,"interuser" : self.user_name})
        connect.commit()
    if selfedit == 2 :
        internewphone = input("Inter New Phone_Number : ")
        curs.execute(f"UPDATE {self.post} SET Phone_Number = :newphone WHERE User_Name = :interuser",{"newphone" : internewphone ,"interuser" : self.user_name})
        connect.commit()
#-----------
def Insert_Employee(post,name,lastname,age,level,phone_number,pay): new_user = Employee(post,name,lastname,age,level,phone_number,pay)
def Manager_Add_New_User(access = False):
    post = ''
    level = ''
    if access == True :
        interpost = int(input("Inter Employee Post\nBoss : 1\nAssistant : 2\nEmployee : 3\n"))
        if interpost == 1 : post = "Boss"
        if interpost == 2: post = "Assistant"
        if interpost == 3: post = "Employee"
    if access == False :
        interpost = int(input("Inter Employee Post\nAssistant : 1\nEmployee : 2\n"))
        if interpost == 1: post = "Assistant"
        if interpost == 2: post = "Employee"
    if post == "Boss" : level = "Advanced"
    if post == "Assistant" :
        interlevel = int(input("Inter Employee Post\nAdvanced : 1\nAverage : 2\n"))
        if interlevel == 1 : level = "Advanced"
        if interlevel == 2 : level = "Average"
    if post == "Employee" :
        interlevel = int(input("Inter Employee Post\nAverage : 1\nElementary : 2\n"))
        if interlevel == 1 : level = "Average"
        if interlevel == 2 : level = "Elementary"
    print(post , level)
    Insert_Employee(post , input("Name : ").capitalize() , input("Lastname : ").capitalize() , input("Age : ") , level , input("Phone_Number : "), input("Pay :") )
#-----------
def edit(table , valuse):
    getusername = str(input("Inter User_name :"))
    interlevel = int(input("Inter New Leve :\nAdvanced : 1\nAverage : 2\nElementary : 3\n"))
    for post in table :
        if getusername in Item_Getter(table,valuse) :
            if interlevel == 1 :
                curs.execute(f"UPDATE {post} SET Level = :newlevel WHERE User_Name = :interuser",{"newlevel" : "Advanced" ,"interuser" : getusername})
                connect.commit()
            if interlevel == 2 :
                curs.execute(f"UPDATE {post} SET Level = :newlevel WHERE User_Name = :interuser",{"newlevel" : "Average" ,"interuser" : getusername})
                connect.commit()
            if interlevel == 3 :
                curs.execute(f"UPDATE {post} SET Level = :newlevel WHERE User_Name = :interuser",{"newlevel" : "Elementary" ,"interuser" : getusername})
                connect.commit()
def Manager_edit_user(self):
    if self.access == True:
        editpart = int(input("What part do you want to edit?\nLevel : 1\nor\nPay: 2\n"))
        if editpart == 1: edit(["Employee","Assistant"],["User_Name"])
        if editpart == 2:
            inerusername = input("Inter User_Name : ")
            if inerusername in Item_Getter(["Employee","Assistant"],["User_Name"]) :
                interpay = int(input("Inter Pay : "))
                for i in ["Employee","Assistant"] :
                    curs.execute(f"UPDATE {i} SET Pay = :newpay WHERE User_Name = :interuser" , {"newpay" : interpay , "interuser" : inerusername})
                    connect.commit()
    elif self.access == False and self.post == "Assistant" : edit(["Employee","Assistant"],["User_Name"])
    else:
        print(self.user_name , " Has No Access To This !!!")
#-----------
def Manager_delete_user(self):
    if self.access == True:
        user = str(input("Inter username which you want to delet : "))
        makesure = input(f"Do you Sure to delete user {user}? Yes or No\n").upper()
        if makesure == "YES":
            if user in Item_Getter(["Employee","Assistant"],["User_Name"]):
                for i in ["Employee","Assistant"] :
                    curs.execute(f"DELETE FROM {i} WHERE User_Name = :interuser" , {"interuser" : user})
                    connect.commit()
            print(f"User {user} Deleted!!!!")
#-----------
def Manager_Resume(self):
    self.position = int(input("What do you do next?\nEXIT : 1\nStay Login : 2\n"))
    if self.position == 1:
        os.system("cls")
        Employee.employee_number = 0
        Manager.all_user()
        login(input("User_Name : "), input("Password : "), " ")
    if self.position == 2:
        print("--------------------------------------------------")
        self.__init__(self.user_name, self.password, self.post)
#-----------
def Manager_Exit(self):
    os.system("cls")
    Employee.employee_number = 0
    Manager.all_user()
    print("--------------------------------------------------")
    Start.__init__()
    login(input("User_Name : ") , input("Password : ") , " ")
#----------------------------------------------------------------------------
# On Start , Exit Methods
def Print_EmployeeS_By_level(level):
    curs.execute(f"SELECT Name,Age,Pay FROM Boss WHERE Level = :level ",{"level":level})
    boss = tabulate(curs.fetchall())
    curs.execute(f"SELECT Name,Age,Pay FROM Assistant WHERE Level = :level ",{"level":level})
    assistant = tabulate(curs.fetchall())
    curs.execute(f"SELECT Name,Age,Pay FROM Employee WHERE Level = :level ",{"level":level})
    employee = tabulate(curs.fetchall())
    print(f"{level} Users in Boss: {boss}")
    print(f"{level} Users in Assistant: {assistant}")
    print(f"{level} Users in Employee: {employee}")
#-----------
def Print_EmployeeS_Join_Date(joinDate):
    curs.execute(f"SELECT Name,Lastname,Age,Pay,Join_Date FROM Boss WHERE Join_Date = :jd ",{"jd":joinDate})
    boss = tabulate(curs.fetchall())
    curs.execute(f"SELECT Name,Lastname,Age,Pay,Join_Date FROM Assistant WHERE Join_Date = :jd ",{"jd":joinDate})
    assistant = tabulate(curs.fetchall())
    curs.execute(f"SELECT Name,Lastname,Age,Pay,Join_Date FROM Employee WHERE Join_Date = :jd ",{"jd":joinDate})
    employee = tabulate(curs.fetchall())
    print(f"\nUsers Added In {joinDate}:\n{boss}\n{assistant}\n{employee}")
#-----------
def Show_All_Employees():
    curs.execute(f"SELECT Name,Lastname,User_Name,Password,Age,Level,Pay,Phone_number,Email,Join_Date FROM Boss ")
    boss = tabulate(curs.fetchall())
    curs.execute(f"SELECT Name,Lastname,User_Name,Password,Age,Level,Pay,Phone_number,Email,Join_Date FROM Assistant ")
    assistant = tabulate(curs.fetchall())
    curs.execute(f"SELECT Name,Lastname,User_Name,Password,Age,Level,Pay,Phone_number,Email,Join_Date FROM Employee ")
    employee = tabulate(curs.fetchall())
    print(f"Users in Boss:\n{boss}\n")
    print(f"Users in Assistant:\n{assistant}\n")
    print(f"Users People in Employee:\n{employee}\n")
#-----------------------------------------------------------------
# Login Function To Check The User_Name And Password
def Login_Check(login__):
    def wrapper(usn,psw,p):
        pswlist2 = list()
        for post in ["Boss" , "Assistant" , "Employee"]:
            curs.execute(f"SELECT Password FROM {post} WHERE User_Name = :interuser",{"interuser":usn})
            x  = curs.fetchall()
            pswlist = list()
            if len(x)>0:
                for i in x :
                    pswlist.append(i[0])
                    pswlist2.append(i[0])
                if usn in Item_Getter([post],["User_Name"]) and psw in pswlist :
                    print("{:-^70}\n\tUser_Name : {}\t\tPost : {}\n".format("Login Succesfull",usn,post))
                    return login__(usn,psw,post)
        while usn not in Item_Getter(["Boss" , "Assistant" , "Employee"],["User_Name"]) or psw not in pswlist2 :
            print("User_Name Or Password Was Incorrect!!!!")
            login(input("User_Name : ") , input("Password : ")," ")
    return wrapper
@Login_Check
def login(usn,psw,p):
    if p == "Boss": user =  Boss(usn,psw,p)
    if p == "Assistant" : user =  Assistant(usn,psw,p)
    if p == "Employee": user =  Employee__(usn,psw,p)
#----------------------------------------------------------------------------
curs.execute("SELECT * FROM Boss")
checknew =  curs.fetchall()
# Check Database When Project Start
# Add User If Database Was Empty
if len(checknew) == 0:
    print("Your Database Is Empty ,New One Was Created!!!\n You Must Import Boss First.\n")
    def firststart() :
        Insert_Employee("Boss", input("Name : ").capitalize(), input("Lastname : ").capitalize(), input("Age : "),input("Level : ") ,input("Phone_Number : "), input("Pay :"))
        x = input("Do You Want To Add New Boss?\n Yes Or No\n")
        if x.upper() == "YES": firststart()
        elif x.upper() == "NO" : login(input("User_Name : "), input("Password : "), " ")
    firststart()
# #----------------------------------------------------------------------------
# Starting Point
Manager.all_user()
class Start():
    def __init__():
        start = input("Login: L\nPrint_EmployeeS_Join_Date: EJ\nPrint_EmployeeS_By_Level: EL\n").upper()
        if start == "L" : login(input("User_Name : ") , input("Password : ")," ")
        if start == "EJ" :
            Print_EmployeeS_Join_Date(input("Enter Date Year_Month_Day: "))
            Start.__init__()
        if start == "EL" : 
            Print_EmployeeS_By_level(input("Enter Date 'Level': "))
            Start.__init__()
if __name__ == "__main__" : Start.__init__()
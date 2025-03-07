import feepending
import feepaid
import otp

admin_username=input("enter a user name: ")
if admin_username=="admin":
    otp = otp.send_otp("lavanyakaicharla11@gmail.com")
    
    x = int(input("enter otp: "))
    if x == otp:
        print("login sucess !")
    else:
        print("login failed! ")
        exit()
else:
    print("In Valid Username")
    exit()
userdetails={
    101 : ["lavanya","20u41a4211@diet.edu.in","false"],
    102 : ["dileep","dileeppolipilli@gmail.com","false"],
    103 : ["lav","lavanyakaicharla1152@gmail.com","false"],
    104 : ["roopa","roopakintada31@gmail.com","true"],
    }
print("Welcome Admim")
while True:
    print("choose your option: ")
    print(" 1. edit information")
    print("2. send mail to fee pending users")
    print("3. send mail to fee paid users")
    print("4. exit")
    x1 = int(input("enter yout option: "))
    if x1==1:
        for user in userdetails:
            if userdetails[user][2]=="false":
                status= input(f"enter the status of {userdetails[user][0]}")
                userdetails[user][2]=status.lower()
                print(f"{userdetails[user][0]} Data Updated! ")
        else:
            print("Data Updated")
    elif x1==2:
        res=[]
        for user in userdetails:
            if userdetails[user][2]=="false":
                res.append([userdetails[user][0],userdetails[user][1]])
        feepending.send_mails(res)
        print("All mails sent to fee fending users")
    elif x1==3:
        res=[]
        for user in userdetails:
            if userdetails[user][2]=="true":
                res.append([userdetails[user][0],userdetails[user][1]])
        feepaid.send_mails(res)
        print("All mails sent to fee paid users")
    else:
        print("Thank you")
        print("Visit Again")
        break
             
            
                

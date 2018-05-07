from datetime import datetime
class User:
    def __init__(self,fn,mn,ln,g,d,n,m,e,u,p,c):
        self.fname=fn
        self.mname=mn
        self.lname=ln
        self.gen=g
        self.date=d
        self.notional=n
        self.mobile=m
        self.email=e
        self.user=u
        self.passW=p
        self.cpass=c

    @staticmethod
    def checkName(n) :              #USED FOR CHECKING FIRST NAME DOESN'T EXISTS OR NOT
        if len(n)>=1:
            return 0
        else:
            print"First name can't be blank"
            return 1
        
    @staticmethod
    def checkMobile(m):             #USED FOR CHECKING MOBILE NUMBER CONSISTS 10 DIGITS OR NOT
        if len(m)==10:
            for i in m:
                if i>="0" and i<="9":
                    flag=0
                else:
                    flag=1
                    break
            if flag==1:
                print"Mobile number shouldn't have any other characters"
                return 1
            else:
                return 0
        else:
            print"Mobile number must contain 10 digits only"
            return 1
        
    @staticmethod
    def checkUser(user):            #USED FOR CHECKING WEITHER USER EXISTD IN THE LIST(REGISTER) OR NOT.
        if user in di.keys():
            print"User exists try with different mobile number"
            print
            return 1
        else:
            return 0
        
    @staticmethod
    def checkPass(p,c):             #USER FOR CHECKING PASSWORD AND CONFIRM PASSWORD ARE SAME OR NOT.
        if p==c:
            return 0
        else:
            print"Password doesn't match, try again!"
            return 1
        
    @staticmethod
    def checkPassw(p):              #USED TO CHECK WEITHER PASSWORD CONSISTS OF ALL THE SPECIFED CHARACTERS OR NOT
        A=0
        a=0
        n=0
        s=0
        for i in p:
            if i>='a' and i<='z':
                a=a+1
            elif i>='A' and i<='Z':
                A=A+1
            elif i>='0' and i<='9':
                n=n+1
            else:
                s=s+1
        if a>=1 and A>=1 and n>=1 and s>=1 and len(p)>=8:
            return 0
        else :
            print"Password must have min 1 a-z,1 A-Z,1 0-9,1 (!@#$....),and no of character min 8"
            #print"Password must contain atleast 1-(A-Z),1-(a-z),1-(0-9) and 1 special character(!@#$%^&*.....)"
            return 1
        
    @staticmethod
    def checkEmail(e):              #USER TO CHECK WEITHER THE ENTERED EMAIL ID IS VALID OR NOT.
        if '@' in e and( ".com" in e or".co.in" in e or "ac.in" in e or ".org" in e) :
            return 0
        else:
            print"Enter proper email id"
            return 1

    @staticmethod  
    def checkGender(gender):            #USED TO CHECK WEITHER ENTERED GENDER IS VALID OR NOT
        li=["F","M","O"]
        if gender in li:
            return 0
        else:
            print"Invalid entry it should be'F/M/O'"
            return 1
    @staticmethod
    def checkNation(n):                 #USED FOR CHECKING WITHER NATIONALY CONSISTS ANY OTHER SPECIAL CHARACTER THAN ALPHABETS
        for i in n:
            if (i>="a" and i<="z")or(i>="A" and i<="Z"):
                flag=0
            else:
                flag=1
                break
        if flag==1:
            print"Nationality doesn't contain special character or numaric values"
            return 1
        else:
            return 0
    def checkUserPass(self):            #USED FOR CHECK WITHER ENTERED USER NAME MATCHES WITH PASSWORD OR NOT
        if di[username].passW==passWord:
            print"Logged in Successfully"
            return 0
        else:
            print"Wrong password try again"
            return 1
    @staticmethod
    def checkDate(d):
        d1=datetime.now()                #CHECK WETHER ENTERED DATE IS IN CURRENT DATE OR NOT
        T=str(d1-d)
        t=T.split(",")
        t1=t[0].split()
        tp=int(t1[0])
        if tp>6574 and tp<36525:
            return 0
        else:
            print t1[0]
            print"User must be atleast 18 year old"
            return 1
        
di=dict()
while True:
    flagU=1
    flagP=1
    flagI=1
    choice=raw_input("Choice\n1.Sign up\n2.Sign in\n")
    if choice=="1":
        while flagI==1:
            fp=1
            fe=1
            fm=1
            fn=1
            fg=1
            fl=1
            flm=1
            while fn==1:
                firstName=raw_input("First Name:(Can't be blank)\n")
                fn=User.checkName(firstName)
            middleName=raw_input("Middle Name:\n")
            lastName=raw_input("Last Name:\n")
            while fg==1:
                gender=raw_input("Gender(F/M/O):\n")
                fg=User.checkGender(gender)
            while flm==1:
                try:
                    dateOfBirth=raw_input("Date of Birth('dd/mm/yyyy'):\n")
                    dt=datetime.strptime(dateOfBirth,"%d/%m/%Y")
                    flm=User.checkDate(dt)
                except :
                    print"DOF should be in 'dd/mm/yyyy' format only"
            while fl==1:
                nationality=raw_input("Nationality:\n")
                fl=User.checkNation(nationality)
            while fm==1:
                mobileNumber=raw_input("Mobile Number:\n")
                fm=User.checkMobile(mobileNumber)
            while fe==1:
                email=raw_input("Email id\n")
                fe=User.checkEmail(email)
            userName=mobileNumber
            while fp==1:
                fcp=1
                while fcp==1:
                    passWord=raw_input("Password\n")
                    fcp=User.checkPassw(passWord)
                    cpassWord=raw_input("Confirm Password\n")
                    fp=User.checkPass(passWord,cpassWord)                       
            t=User.checkUser(userName)
            if t==0:
                u=User(firstName,middleName,lastName,gender,dateOfBirth,nationality,mobileNumber,email,userName,passWord,cpassWord)
                di[userName]=u
                flagI=0
            #print di
    elif choice=="2":
        while flagU==1:
            username=raw_input("Username:\n")
            if username in di.keys():
                flagU=0
                while flagP==1:
                    passWord=raw_input("Password:\n")
                    flagP=u.checkUserPass()
            else:
                print"User not present"
    else:
        print"Enter the correct choice"

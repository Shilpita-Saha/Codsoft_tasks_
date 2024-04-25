print("..........Mini Calculator...........")
while True:
   num1=float(input("Enter the first number:"))
   num2=float(input("Enter the second number:"))

   print("Press 1 for addition,Press 2 for subtraction,Press 3 for Multiplication,Press 4 for Division")
   choice=int(input("Enter your choice:"))
   if choice==1:
           sum=num1+num2
           print(num1,"+",num2)
           print("Addition of two numbers:",sum)
   elif choice==2:
           sub=num1-num2
           print(num1,"-",num2)
           print("Subtraction of two numbers:",sub)

   elif choice==3:
           mul=num1*num2
           print(num1,"*",num2)
           print("Multiplication of two numbers:",mul)

   elif choice==4:
           div=num1/num2
           print(num1,"/",num2)
           print("Divition of two numbers:",div)

print("\n=======CALCULATOR=====\n")

while True:
 number1=int(input("Enter the first number ="))
 number2=int(input("Enter the second number ="))
 print("<<< Operations >>>")
 print("1. Addition")
 print("2. Subtraction")
 print("3. Multiplication")
 print("4. Division")
 print("5. Modulus")
 print("6. Exponentiation")
 print("7. Floor division")

 operation=int(input("Choose any Operation\n"))

 if operation==1:
  print("The SUM is = ",number1+number2 )
  print("\n")
 elif operation==2:
  print("The SUB is = ",number1-number2 )
  print("\n")
 elif operation==3:
  print("The MUL is = ",number1*number2 )
  print("\n")
 elif operation==4:
  if number2==0:
    print("Error: Division by zero is not allowed.")
  else:
   print("The DIV is = ",number1/number2 )
   print("\n")
 elif operation==5: 
    if number2==0:
      print("Error: Modules by zero is not allowed.")
    else:
     print("The MOD DIV is = ",number1%number2 )
     print("\n")
 elif operation==6:
  print("The EXPO is = ",number1**number2 )
  print("\n")
 elif operation==7:
  if number2==0:
    print("Error: Division by zero is not allowed.")
  else:
   print("The FLOOR DIV is = ",number1//number2 )
   print("\n")
  
 else:
  print("\n^^^Enter the valid Operation^^^\n")
 
 opt=input(print("Do you want to continue (yes/no) :\t")) .strip().lower()
 if opt!="yes":
  print("\n<---Thank you for using the calculator  Goodbye!--->\n")
  break
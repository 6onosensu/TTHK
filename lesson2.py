#
s = 0
numbers = []
runApp = True

while runApp: 
  user_input = input("Input quit or your number: ").lower().strip()
  print(user_input)
  if user_input == "quit":
    runApp = False
  else:
    try:
      number = float(user_input)
      numbers.append(number)
      print(numbers)
      for n in numbers:
        if isinstance (n, (int, float)) and n >= 0:
          s += n
      print(s)
    except ValueError:
      print("That´s not a number!")


            


#voileib
soov = input("Kas sa tahad suua?: ").lower()
if soov == "yes":
  valik = int(input("1-juustuga voileib\n2-vorstiga voileib\n"))
  if valik in [1,2]:
    if valik == 1:
      print("palun juustuga voileib")
    else:
      print("palun vorstiga voileib")
  else:
    print("vale valik!")
else:
  print("ei taha, siis ei taha")


#Grant
student = input("Answer yes or no to all questions, except this one: What is your name?: ")
grantCancelled = "Your grant application has been cancelled!"
grant = "Congratulations, ",student,"!Your grant application has been approved!"
group = input("Is your group TARgv23?: ")
if group == "yes" :
  mark = input("Is average mark >= 3.8?: ")
  if mark == "yes":
    absence = input("Do you have any absence?:")
    if absence == "no":
      print(grant)
    else :
      print(grantCancelled)
  else :
    print(grantCancelled)     
else :
  print(grantCancelled)

#Kalkulator
try:
  a = float(input("first number: "))
  try:
    b = float(input("Second number: ")) 
    t = input("Do:")
    if t in ["+","-","*","/","**","%","//"]:
      if t == "+" :
        v = a + b
      elif t == "-" :
        v = a - b
      elif t == "*" :
        v = a * b
      elif t == "/" :
        if b == 0 :
          v = "DIV/0"
        else :
          v = a / b
      elif t == "**" :
        v = a ** b
      elif t == "%" :
        v = a % b
      else :
        v = a // b
        print("{0}{1}{2} = {3}".format(a,t,b,v))
    else:
      print("Sign entered incorrectly")
  except :
    print("Wrong data type")
      
except:
  print("Data entered incorrectly")



#A Triangle
a=float(input("Alpha:"))
b=float(input("Betta:"))
c=float(input("Gamma:"))

if a > 0 and b > 0 and c > 0:
  if a + b + c == 180 :
    print("The triangle")
  else :
    print("Not a triangle")
else:
  print("Data entered incorrectly")
number=int(input("enter the number"))
def reversed_number(num):
 reversed_num=0
 while num>0:
  last_digit=num%10
  reversed_num=reversed_num+last_digit
  num//=10
 return reversed_num
reversed_number=reversed_number(number)
print(f"the reversed numberof {number} is {reversed_number}")
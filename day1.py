# def greet():
#  print("hello")
#  print("how do you do")
#  print("is not the weather nice today?")
 
# greet()
# def greet_with_name(something):
#  print(f"hello {something}")
#  print(f"how do you do {something}")
 
# greet_with_name("Jack Buer")
import math

def prime_checker(number):
 for i in range(2,number):
  is_prime=True
  if number%i==0:
   is_prime=False
 if is_prime:
  print("it is prime")
 else:
  print("ain't prime")
n=int(input("check this number: "))
prime_checker(n)
alphabet=['a','b','c','d','e','f','g','i','h','g','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','g','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']


def caesar(start_text,shift_amount,cipher_direction):
 end_text=""
 if cipher_direction=="decode":
   shift_amount=shift_amount*-1
 for char in start_text:
   if char in alphabet:
      position=alphabet.index(char)
      new_position=position+shift_amount
      end_text+=alphabet[new_position]
   else:
     end_text+=char
 print(f"the {cipher_direction} text is {end_text}")
should_continue=True
while should_continue:
  direction=input("type encode to ecrpt,type(decode to):\n")
  text=input("type your message: \n").lower().strip()
  shift=int(input("type the shift number:\n"))
  caesar(text,shift,direction)
  result=input("type (yes) if you wanna go again ,otherwise type (no).\n")
  if result=="no":
    should_continue=False
    print("Goodbye")
  
# def encrypt(plain_text,shift_amiount):
#  cipher_text=""
#  for letter in plain_text:
#   position=alphabet.index(letter)
#   new_position=position+shift_amount
#   new_letter=alphabet[new_position]
#   cipher_text+=new_letter
#  print(f"The encoded text is {cipher_text}")
# def decrypt(cipher_text,shift_amount):
#  plain_text=""
#  for letter in cipher_text:
#   position=alphabet.index(letter)
#   new_position=position-shift_amount
#   plain_text+=alphabet[new_position]
#  print(f"the decoded text is {plain_text}")
# if direction=="encode":
#   encrypt(text,shift)
# elif direction=="decode":
#  decrypt(text,shift)
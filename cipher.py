# assignment: programming assignment 4
# author: Ricardo Esquivel
# date: 11/30/2020
# file: cipher.py is a program that ciphers a code back into readable or unreadable
# input: files that contain unreadable or readable text
# output: converted files that have been ciphered or unciphered

# read text from a file and return text as a string
def readfile():
   file1 = str(input("\nPlease enter a file for reading:"))
   try:
      file1 = open(f"{file1}",'r')
      lines = file1.readlines()
      message = to_string(lines)
   except IOError:
      print("\nFile cannot be opened.")
   else:
      file1.close
   return message

# write a string (message) to a file
def writefile(message):
   file2 = str(input("\nPlease enter a file for writing:"))
   try:
      file2 = open(f"{file2}",'w')
      file2.truncate(0)
      message2 = file2.write(f"{message}")
   except IOError:
      print("\nFile cannot be opened.")
   else:
      file2.close
   return message2

# make a list (tuple) of letters in the English alphabet
def make_alphabet():
   alphabet = ()
   for i in range(26):
       char = i + 65
       alphabet += (chr(char),)
   return alphabet

# return a list of encoded symbols
def encode(plaintext):
   plaintext = plaintext.upper()
   shift = 3
   ciphertext = []
   alphabet = make_alphabet()
   length = len(alphabet)
   for char in plaintext:
       found = False
       for i in range(length):
           if char == alphabet[i]:
               letter = alphabet[(i + shift) % length]
               ciphertext.append(letter)
               found = True
               break
       if not found:
           ciphertext.append(char)
   return ciphertext

# return a list of decoded symbols
def decode(ciphertext):
   ciphertext = ciphertext.upper()
   shift = -3
   plaintext = []
   alphabet = make_alphabet()
   length = len(alphabet)
   for char in ciphertext:
       found = False
       for i in range(length):
           if char == alphabet[i]:
               letter = alphabet[(i + shift) % length]
               plaintext.append(letter)
               found = True
               break
       if not found:
           plaintext.append(char)
   return plaintext

# convert a list into a string
def to_string(text):
   s = ""
   for words in text:
      s += words
   return s

#MAINPROGRAM
done = False
while not done:
      choice = input("Would you like to encode or decode the message? \
      \nType E to encode, D to decode, or Q to quit:")
      #ENCODING
      if choice == "E" or choice ==  "e":
         plaintext = readfile() 
         ciphertext_list = encode(plaintext) 
         ciphertext = to_string(ciphertext_list)
         writefile(ciphertext)
         print(f"\nPlaintext:\
         \n{plaintext}")
         print(f"\nCiphertext:\
         \n{ciphertext}")
      #DECODING
      elif choice == "D" or choice == "d":
         ciphertext = readfile()
         plaintext_list = decode(ciphertext)
         plaintext = to_string(plaintext_list)
         writefile(plaintext)
         print(f"\nCiphertext:\
         \n{ciphertext}")
         print(f"\nPlaintext:\
         \n{plaintext}")
      #LEAVING
      elif choice == "Q" or choice == "q":
         print("\nGoodbye!")
         done = True
      #CONTINUE THE LOOP
      else:
         continue

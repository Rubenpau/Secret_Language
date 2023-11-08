import random
import string

print("          MAIN MENU")
print("==================================")
print("         1. CODING ")
print("         2. DECODING ")
print("==================================")
choice = int(input("choose one of them = "))
if (choice == 1):
   
  msg = input("enter a message to encode = ") 
  word = msg.split(" ")  #now msg is become a list
  encword = []
  for i in word:
    if (len(i) < 3):
      encword.append(i[::-1])
    #by using -1 jumpindex it will traverse in reverse order

    else:
      new_word = i[1:] + i[0]

      start = ''.join(random.choice(string.ascii_letters) for _ in range(3))
      end = ''.join(random.choice(string.ascii_letters) for _ in range(3))
  
      final_word =start + new_word + end
      encword.append(final_word)
  print('_____________________________________')
  print('  encoded word = ', encword)
  print('_____________________________________')

else:

  code = input("enter a code to decode = ")
  word = code.split()
  decode_word = []
  for i in word:
    if (len(i) < 3):
      decode_word.append(i[::-1])  #by using -1 jumpindex it will traverse in reverse   order
    
    else:
      substr = i[3:-3]
      decode_word.append(substr[len(substr) - 1] + substr[0:-1])
  print('_____________________________________')
  print('  decoded word = ', decode_word)
  print('_____________________________________')
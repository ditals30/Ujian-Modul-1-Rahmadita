'''Nomer 1'''
num = input('Input your phone number: ')
if num.isnumeric() == True:
    if int(num) < 1 :
        print('Input only positive number')
    elif len(num) < 10 or len(num) > 10:
        print('Digits must be in length of 10, not more or less')
    elif num.isdigit() == False:
        print ('Invalid Input. No Alphabet')
    else:
        print("("+num[:3]+")"+num[3:6]+"-"+num[6:])
else :
    if int(num) < 1 :
        print('Input only positive number')
    else:
        print ('Invalid input. No symbols')
    

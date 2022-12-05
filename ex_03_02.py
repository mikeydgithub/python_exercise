# more conditional statements: multi-way

# x = 11
# if x < 2 :
#     print('small')
# elif x < 10 :
#     print('Medium')
# else : 
#     print('LARGE')
# print('ALL done')

# No Else
# x = 150
# if x < 2 :
#     print('Small')
# elif x < 10 :
#     print('Medium')
# elif x < 20 :
#     print('Big')
# elif x < 40 :
#     print('Large')
# elif x < 100 :
#     print('Huge')
# else :
#     print('Ginormous')
# print('All Done')

# try/ except structure

# in the below block, the try will not compute because the string does not contain any digits. so it cant be turned into an integer. the try code will not run and then the except will run. since istr equals -1, it will print in our print statement.

# astr = 'Hello Bob'
# try:
#     istr = int(astr)
# except:
#     istr = -1
# print('Frist', istr)

# since the string here has digits, it can conver into a string and the try will work and never make it to the except.
# astr = '123'
# try:
#     istr = int(astr)
# except:
#     istr = -1
# print('First', istr)

# rawstr = input('Enter a number: ')
# try:
#     ival = int(rawstr)
# except:
#     ival = -1

# if ival > 0 :
#     print('Nice work')
# else:
#     print('Not a number')
# print('All Done')


# challenge
sh = input("Enter Hours: ")
sr = input("Enter Rate: ")
try:
    fh = float(sh)
    fr = float(sr)
except:
    print("Error, please enter numeric input.")
    quit()

print(fh, fr)
if fh > 40:
    reg = fh * fr
    otp = (fh - 40.0) * (fr * 0.5)
    xp = reg + otp
else:
    xp = fh * fr
print("Pay:", xp)

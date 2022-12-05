# conditional statements
# x = 5
# if x < 10:
#     print('Smaller')
# if x > 20:
#     print('Bigger')

# increase/maintain after if or for decrease to indicate end of block
# x = 5
# if x > 2 :
#     print('Bigger than 2')
#     print('Still bigger')
# print('Done with 2')

# for i in range(5) :
#     print(i)
#     if i > 2 :
#         print ('Bigger than 2')
#     print('Done with i', i)
# print('All Done')

# nested decisions
# x = 42
# if x > 1 :
#     print("More than one")
#     if x < 100 :
#         print('Less than 100')
# print('All Done')

# Two-way decisions if, else, then
# x = 4
# if x > 2 :
#     print('Bigger')
# else :
#     print('Smaller')
# print('All Done')

# x = 0
# y = 10
# if 0 == x :
#     if y == 10 :
#         print("Yes")  
# print('All Done')  

# challenge
sh = input("Enter Hours: ")
sr = input("Enter Rate: ")

fh = float(sh)
fr = float(sr)
print(fh, fr)

if fh > 40:
    # print("Overtime")
    reg = fh * fr
    otp = (fh - 40.0) * (fr * 1.5)
    # print(reg, otp)
    xp = reg + otp
else:
    # print("Regular")
    xp = fh * fr
print("Pay:", xp)
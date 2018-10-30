#Arik Parenteau
#

fullname = input('Enter a full name\n')
namelist = fullname.split()

initial1 = namelist[0][0].upper()
initial2 = namelist[1][0].upper()
initial3 = namelist[2][0].upper()

print('The initials are: %s. %s. %s' % (initial1,initial2,initial3))

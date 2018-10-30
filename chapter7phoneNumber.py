phoneNumber = input('Enter a phone number in the form xxx-xxx-xxxx to translate:\n')
phoneNumber = phoneNumber.upper()
for i in phoneNumber:
	if i in ['A','B','C']:
		phoneNumber = phoneNumber.replace(i,'2')
	elif i in ['D','E','F']:
		phoneNumber = phoneNumber.replace(i,'3')
	elif i in ['G','H','I']:
		phoneNumber = phoneNumber.replace(i,'4')
	elif i in ['J','K','L']:
		phoneNumber = phoneNumber.replace(i,'5')
	elif i in ['M','N','O']:
		phoneNumber = phoneNumber.replace(i,'6')
	elif i in ['P','Q','R','S']:
		phoneNumber = phoneNumber.replace(i,'7')
	elif i in ['T','U','V']:
		phoneNumber = phoneNumber.replace(i,'8')
	elif i in ['W','X','Y','Z']:
		phoneNumber = phoneNumber.replace(i,'9')

		
print('\nTranslated phone number: %s' % phoneNumber)

#Arik Parenteau
#
#9/25/2018
#CIS 1415 Chapter 4 Problem 12

#dictionary with car services provided
services = {'Oil change': 35, 'Tire rotation': 19,
            'Car wash': 7, 'Car wax': 12, '-': 0
}            
#shows a menu of services
print("Davy's auto shop services")
print('Oil change -- $35\n'
      'Tire rotation -- $19\n'
      'Car wash -- $7\n'
      'Car wax -- $12')


service1 = input('\nSelect first service:\n')
service2 = input('Select second service:\n')

print("\nDavy's auto shop invoice")
if service1 == 'Oil change' or service1 == 'Tire rotation' or service1 == 'Car wash' or service1 == 'Car wax':
    print('\nService 1: %s, $%d' % (service1, services[service1]))
else:
    print('\nService 1: No service')

if service2 == 'Oil change' or service2 == 'Tire rotation' or service2 == 'Car wash' or service2 == 'Car wax':
    print('Service 2: %s, $%d' % (service2, services[service2]))
else:
    print('Service 2: No service')
    
total = services[service1] + services[service2]
print('\nTotal: $%d' % total)

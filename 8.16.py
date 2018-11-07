#Arik Parenteau
#Gabe Sorenson
weights = []

def calculateAvg():
    listSum = sum(weights)
    return listSum / len(weights)

def calculateKilo(pounds):
    return pounds / 2.2

def createList():
    for x in range(1,5):
        print('Enter weight %d:' % x)
        weight = float(input())
        weights.append(weight)
    print('Weights:', weights)

def printKilo():
    index = int(input('\nEnter a list index (1 - 4):\n'))
    print('Weight in pounds: %.2f' % weights[index - 1])
    kilo = calculateKilo(weights[index - 1])
    print('Weight in kilograms: %.2f' % kilo)
    

createList()
average = calculateAvg()
maxList = max(weights)
print('\nAverage weight: %.2f' % average)
print('Max weight: %.2f' % maxList)

printKilo()

print()
weights.sort()
print('Sorted list:', weights)

#Arik Parenteau
#Gabe Sorenson

class ItemToPurchase:
    def __init__(self, item_name = 'none', item_price = 0, item_quantity = 0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        
    def print_item_cost(self):
        total = self.item_price * self.item_quantity
        print('%s %d @ $%.0f = $%.0f' % (self.item_name,self.item_quantity,self.item_price,total))


if __name__ == "__main__":
	#Creates a list of objects from the ItemToPurchase class
	instancelist = [ItemToPurchase() for i in range(2)]
	
	for x in range(len(instancelist)):
	    print('Item %d' % (x+1))
	    instancelist[x].item_name = input('Enter the item name:\n')
	    instancelist[x].item_price = float(input('Enter the item price:\n'))
	    instancelist[x].item_quantity = int(input('Enter the item quantity:\n'))
	    print()
		
	print('TOTAL COST')
	total = 0
	for y in range(len(instancelist)):
		instancelist[y].print_item_cost()
		total = total + (instancelist[y].item_price * instancelist[y].item_quantity)
	print('\nTotal: $%.0f' % total)

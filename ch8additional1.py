#Gabe Sorenson
#Arik Parenteau

def main():
    names_of_months = ['January', 'February', 'March', 'April', 'May', 'June',\
                       'July', 'August', 'September', 'October', 'November', 'December']
    total_rainfall_list = []
    total_rainfall_list = get_rainfall_amounts(names_of_months)
    total_rainfall = calc_total_rainfall(total_rainfall_list)
    average_rainfall = calc_avg_monthly_rainfall(total_rainfall, total_rainfall_list)
    highest = highest_rainfall_month(total_rainfall_list, names_of_months)
    lowest = lowest_rainfall_month(total_rainfall_list, names_of_months)
    print_rainfall_stats(total_rainfall_list, names_of_months, total_rainfall,\
                         average_rainfall, highest_rainfall_month,\
                         lowest_rainfall_month)

def get_rainfall_amounts(names_of_months):
    months_in_year = 12
    total_rainfall_list = []

    for index in range (months_in_year):
        monthly_rainfall = float(input('Please enter the rainfall amount for ' +\
              names_of_months[index] + ': '))
        total_rainfall_list.append(monthly_rainfall)

    return total_rainfall_list

def calc_total_rainfall(total_rainfall_list):
    total_rainfall = 0

    for current_monthly_rainfall_index in range (len(total_rainfall_list)):
        total_rainfall = total_rainfall +\
                         total_rainfall_list[current_monthly_rainfall_index]

    return total_rainfall

def calc_avg_monthly_rainfall(total_rainfall, total_rainfall_list):
    number_of_months = len(total_rainfall_list)
    average_rainfall = calc_total_rainfall(total_rainfall_list) / number_of_months

    return average_rainfall

def highest_rainfall_month(total_rainfall_list, names_of_months):
    highest_rainfall_amount = max(total_rainfall_list)
    highest_rainfall_amount_index = total_rainfall_list.index(highest_rainfall_amount)

    return highest_rainfall_amount_index

def lowest_rainfall_month(total_rainfall_list, names_of_months):
    lowest_rainfall_amount = min(total_rainfall_list)
    lowest_rainfall_amount_index = total_rainfall_list.index(lowest_rainfall_amount)

    return lowest_rainfall_amount_index
    
def print_rainfall_stats(total_rainfall_list, names_of_months, total_rainfall,\
                         average_rainfall, highest_rainfall_month,\
                         lowest_rainfall_month):
    print()
    
    for index in range(len(names_of_months)):
        print(names_of_months[index], 'has a rainfall amount of',\
              total_rainfall_list[index])
        
    print('\nTotal rainfall: ', str(total_rainfall),\
          'Average rainfall: ', format(average_rainfall, '.3f'),\
          highest_rainfall_month + " has the highest rainfall",\
          lowest_rainfall_month + " has the lowest rainfall", sep = '\n')

    
main()    
        


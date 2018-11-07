#Gabe Sorenson
#

#This program asks the user to enter 10 numbers, stores the numbers in a list,
and displays the highest number, lowest number, total of the numbers, and the average.

def main():
    number_of_usernums = 10
    user_num_list = []
    
    user_num_list = get_user_num(number_of_usernums)
    lowest_num = find_lowest_num(user_num_list)
    highest_num = find_highest_num(user_num_list)
    total_num = calc_total_num(user_num_list)
    avg_num = calc_avg_num(user_num_list, total_num)
    print_num(user_num_list, lowest_num, highest_num,\
              total_num, avg_num)

    

def get_user_num(number_of_usernums):
    user_num_list = []

    for user_num_index in range (number_of_usernums):
        user_num = int(input('Please enter a number ' +\
                str((user_num_index + 1 )) + ': '))
        user_num_list.append(user_num)

    return user_num_list

def find_lowest_num(user_num_list):
    lowest_num = min(user_num_list)

    return lowest_num

def find_highest_num(user_num_list):
    highest_num = max(user_num_list)

    return highest_num

def calc_total_num(user_num_list):
    total_num = 0
    
    for user_num_index in range(len(user_num_list)):
        total_num = total_num + user_num_list[user_num_index]

    return total_num

def calc_avg_num(user_num_list, total_num):
    number_of_num_list = len(user_num_list)
    avg_num = total_num / number_of_num_list

    return avg_num

def print_num (user_num_list, lowest_num, highest_num,\
               total_num, avg_num):
    print('\nUser numbers provided: ')
    
    for user_num_index in range (len(user_num_list)):
        print(user_num_list[user_num_index])

    print('\nLowest Number: ' + str(lowest_num),\
          'Highest Number: ' + str(highest_num),\
          'Total of Numbers: ' + str(total_num),\
          'Average of Number: ' + str(avg_num), sep = '\n')

main()

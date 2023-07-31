if __name__ == '__main__':
    import random

    length_of_password = int(input('Enter Number Of Characters: '))
    
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    
    capital_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 
                       'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    
    small_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                     'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
                     'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    special_characters = ['@', '#', '$', '%', '=', ':', '?', 
                      '.', '/', '|', '~', '>', '*', '(', ')', '<']
    
    combined_list = digits + capital_letters + small_letters + special_characters
    
    temp_password = random.sample(combined_list,length_of_password)
    
    password = ''.join(temp_password)

    print(password)
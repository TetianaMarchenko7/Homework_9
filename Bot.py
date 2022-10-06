import re
from pprint import pprint

dict_users = {}

def input_error(handler):
    def wrapper(*args, **kwargs):
        try:
            return handler(*args, **kwargs)
        
        except ValueError as e:
            return e.args[0]
            
    return wrapper


@input_error
def new_user():
    user = input("Enter new user name and phone number (example: Tetiana +380959998877): " )
    
    list_user = user.split (" ")

    if len(list_user)!=2:
        raise ValueError(print("Data is not correct, try again"))
            
    elif list_user[0] in dict_users:
        raise ValueError(print("User exists"))
    
    else:
        check_name = re.search(r"[A-Z][a-z]*", list_user[0])
        check_number = re.search(r"\+380(95|50|67|53|93)[0-9]{7}", list_user[1])
        
        if check_name != None and check_number != None:
            check_name1 = check_name.group()
            check_number1 = check_number.group()
        else:
            raise ValueError(print("Data isn't correct, try again"))
                
        if len(check_name1) != len(list_user[0]) or len(check_number1) != len(list_user[1]):
            raise ValueError(print("Data isn't correct"))
            
        dict_users[check_name1] = check_number1

   
@input_error
def change_data():
    user = input("Enter user name and new phone number (example: Tetiana +380959998877): " )
    list_user = user.split (" ")

    if len(list_user) > 2:
        raise ValueError(print("Data isn't correct, try again"))

    if list_user[0] in dict_users:
        check_number = re.search(r"\+380(95|50|67|53|93)[0-9]{7}", list_user[1])
        
        if check_number != None:
            check_number1 = check_number.group()
        else:
            raise ValueError(print("Data isn't correct, try again"))

        if len(check_number1) == len(list_user[1]):
            dict_users[list_user[0]] = list_user[1]
        else:
            raise ValueError (print("Data isn't correct, try again"))
    
    else:
        raise ValueError (print("User's name isn't in the list"))
    

@input_error   
def user_phone():
    
    name= input("Enter user's name: ")

    if name in dict_users:
        print(dict_users[name])
    else:
        raise ValueError (print("User isn't in the list"))


@input_error    
def user_list():

    pprint(dict_users)    

@input_error
def answer_hello():
    return print('How can I help you?')

@input_error
def answer_exit():
    print("Good bye!")
    quit()
    

commands={  
    "hello" : answer_hello, 
    "add" : new_user, 
    "change" : change_data, 
    "phone" : user_phone, 
    "show all" : user_list, 
    "good bye" : answer_exit, 
    "close" : answer_exit, 
    "exit" : answer_exit
}

   
def main():

    while True:
    
        command = input("Input command: ")
    
        if command in commands:
            commands[command]()
        else:
            print("Unknown command")


if __name__ == "__main__":
    main()
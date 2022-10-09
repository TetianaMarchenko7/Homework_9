import re
from pprint import pprint

users_dict = {}


def input_error(handler):
    
    def wrapper(*args, **kwargs):
        
        try:
            return handler(*args, **kwargs)
        except KeyError:
            return 'Wrong name'
        except ValueError as exception:
            return exception.args[0]
        except IndexError:
            return 'Pls print: name and number'
        except TypeError:
            return 'Wrong command'
        
    return wrapper


@input_error
def new_user(param):

    name, phone = change_input_user_data(param)

    if name in users_dict:
        raise ValueError('This contact already exist')
    
    users_dict[name] = phone
    
    return f'You added new contact: {name} with this {phone}'
    
   
@input_error
def change_data(param):

    name, phone = change_input_user_data(param)

    if name in users_dict:
        users_dict[name] = phone
        return f'You changed number to {phone} for {name}'
    return 'Use add command plz.'


@input_error   
def user_phone(param):

    if param.strip() not in users_dict:
        raise ValueError('This contact does not exist')
    return users_dict.get(param.strip())
    

@input_error    
def user_list():

    return (pprint(users_dict))    

@input_error
def answer_hello():
    return 'How can I help you?'

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


def action(user_input):
    
        command = input("Input command: ")
    
    return reaction_func(input_command)()


def reaction_func(reaction):
    return commands.get(reaction, break_func)

def break_func():
    return 'Wrong enter'


def change_input_user_data(input_user_data):

    user = input_user_data.strip().split(" ")

    if len(user)!=2:

        raise IndexError

    name = re.search(r"[A-Z][a-z]*", user[0])
    phone = re.search(r"\+380(95|50|67|53|93)[0-9]{7}", user[1])
        
    if name != None and phone != None:
        name1 = name.group()
        phone1 = phone.group()
    else:
        raise ValueError("Data isn't correct, try again")
                
    if len(name1) != len(user[0]) or len(phone1) != len(user[1]):
        raise ValueError("Data isn't correct")
            
    return name1, phone1
  
def main():

    print ("Bot takes data in the format as in the example: Tetiana +380959998877")

    while True:

        user_input = input("Input command for bot: ")
        result = action(user_input)
        print(result)
           

if __name__ == "__main__":
    main()
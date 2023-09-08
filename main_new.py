

def input_error(func):

    def wrapper(*args, **kwargs):
        print(f'Wrapper: func - {func.__name__}, args - {args}')

        func(*args, **kwargs)
    
    return wrapper


def add_phone(name, phone):
    """
    "add ..."
    За цією командою бот зберігає у пам'яті (у словнику наприклад) новий контакт. 
    Замість ... користувач вводить ім'я та номер телефону, обов'язково через пробіл.
    """
    DICT_PHONES[name] = phone


def change_phone(name, phone):
    """
    "change ..."
    За цією командою бот зберігає в пам'яті новий номер телефону існуючого контакту. 
    Замість ... користувач вводить ім'я та номер телефону, обов'язково через пробіл.
    """
    DICT_PHONES[name] = phone


def good_bye():
    """
    "good bye", 
    "close", 
    "exit" 
    По будь-якій з цих команд бот завершує свою роботу після того, як виведе у консоль "Good bye!".
    """

    print('Good Bye!')
    return False


def hello():
    """
    "hello"
    Відповідає у консоль "How can I help you?"
    """
    print('How can I help you?')


def parsing_command(user_input):

    user_data = user_input.split()

    command = user_data.pop(0)
    name = None
    phone = None

    if len(user_data) == 1:
        name = user_data[0]
    else:
        name = user_data[0]
        phone = user_data[1]


    return command, name, phone


def get_phone(name):
    """
    "phone ...."
    За цією командою бот виводить у консоль номер телефону для зазначеного контакту. 
    Замість ... користувач вводить ім'я контакту, чий номер треба показати.
    """

    print(f'Name: {name:<15}; Phone number: {DICT_PHONES[name]}')


def show_all():
    """
    "show all"
    За цією командою бот виводить всі збереженні контакти з номерами телефонів у консоль.
    """

    for name, phone in DICT_PHONES.items():
        print(f'Name: {name:<15}; Phone number: {phone}')




def main():

    is_work = True
    cycle = 0
    while is_work:

        cycle += 1
        print(f'\n{is_work = }; {cycle = }')

        user_input = input('>>> ')

        if '.' in user_input:
            break
        elif 'good bye' in user_input or 'close' in user_input or 'exit' in user_input:
            is_work = good_bye()
        elif 'hello' in user_input:
            hello()
        elif 'show all' in user_input:
            show_all()
        else:
            command, name, phone = parsing_command(user_input)

            if command == 'add':
                add_phone(name, phone)
            elif command == 'change':
                change_phone(name, phone)
            elif command == 'phone':
                get_phone(name)




    
    




if __name__ == '__main__':

    # COMMANDS = {
    #     'hello': hello,
    #     'add' : add,
    #     'change' : change,
    #     'phone' : phone,
    #     'show all' : show_all,
    #     'good bye' : goodbye,
    #     'close' : goodbye,
    #     'exit' : goodbye,
    # }

    DICT_PHONES = {
        'Vitalii': '0637609640',
        'Oleg': '0637546853'
    }

    main()
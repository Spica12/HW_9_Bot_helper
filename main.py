def input_error(func):
    """
    Всі помилки введення користувача повинні оброблятися за допомогою декоратора input_error. 
    Цей декоратор відповідає за повернення користувачеві повідомлень виду 
        "Enter user name", 
        "Give me name and phone please" і т.п. 
    Декоратор input_error повинен обробляти винятки, що виникають у функціях-handler 
    (KeyError, ValueError, IndexError) та повертати відповідну відповідь користувачеві.
    """

    def wrapper(args):
        print(f'Wrapper: func - {func.__name__}, args - {args}')

        if not is_work:
            return goodbye(args)
        if '.' in args:
            print("You entered '.'. Bot is finishing his work.")
            is_work = False
            return is_work
            
        return func(args)


    return wrapper


@input_error
def add(args):
    """
    "add ..."
    За цією командою бот зберігає у пам'яті (у словнику наприклад) новий контакт. 
    Замість ... користувач вводить ім'я та номер телефону, обов'язково через пробіл.
    """
    DICT_PHONES[args[0]] = args[1]


@input_error
def get_commands(command):
    return COMMANDS[command]


@input_error
def goodbye(args):
    """
    "good bye", 
    "close", 
    "exit" 
    По будь-якій з цих команд бот завершує свою роботу після того, як виведе у консоль "Good bye!".
    """
    global is_work
    print('Good Bye!')
    is_work = False
    

@input_error
def change(args):
    """
    "change ..."
    За цією командою бот зберігає в пам'яті новий номер телефону існуючого контакту. 
    Замість ... користувач вводить ім'я та номер телефону, обов'язково через пробіл.
    """
    DICT_PHONES[args[0]] = args[1]


@input_error
def phone(args):
    """
    "phone ...."
    За цією командою бот виводить у консоль номер телефону для зазначеного контакту. 
    Замість ... користувач вводить ім'я контакту, чий номер треба показати.
    """

    print(DICT_PHONES[args[0]])


@input_error
def show_all(args):
    """
    "show all"
    За цією командою бот виводить всі збереженні контакти з номерами телефонів у консоль.
    """
    count = 0
    for name, phone in DICT_PHONES.items():
        count += 1
        print(f'{count:<2} {name:<15} {phone}')


@input_error
def hello(args):
    """
    "hello"
    Відповідає у консоль "How can I help you?"
    """
    print('How can I help you?')


def input_from_user():

    user_data = list()

    user_input = input('>>> ').split()
    # print(f'input_from_user: {user_input = }')

    len_command = len(user_input)
    if len_command == 1:
        command = user_input[0]
    elif len_command == 2 and user_input[0] != 'phone':
        command = ' '.join(user_input)
    else: 
        command = user_input[0]
        user_data.extend(user_input[1:])
        print('Command Error: too musch arguments. Try again!')     
    
    return command.lower(), user_data


def main(): 

    cycle = 0
    while is_work:
        cycle += 1
        print(f'{is_work = }; {cycle = }')

        # Type of requests:
        #   hello
        #   add Vitalii 0637609640
        #   change Vitalii 0984520
        #   phone Vitalii
        #   show all
        #   good bye
        #   close
        #   exit    
        
        command, args = input_from_user()

        request = get_commands(command)
        request(args)
    


if __name__ == '__main__':

    COMMANDS = {
        'hello': hello,
        'add' : add,
        'change' : change,
        'phone' : phone,
        'show all' : show_all,
        'good bye' : goodbye,
        'close' : goodbye,
        'exit' : goodbye,
    }

    DICT_PHONES = {
        'Vitalii': '0637609640',
        'Oleg': '0637546853'
    }

    is_work = True
    main()
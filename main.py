def input_error(func):
    """
    Всі помилки введення користувача повинні оброблятися за допомогою декоратора input_error. 
    Цей декоратор відповідає за повернення користувачеві повідомлень виду 
        "Enter user name", 
        "Give me name and phone please" і т.п. 
    Декоратор input_error повинен обробляти винятки, що виникають у функціях-handler 
    (KeyError, ValueError, IndexError) та повертати відповідну відповідь користувачеві.
    """

    def wrapper(*args, **kwargs):
        
        if DEBUG:
            print(f'Wrapper: func - {func.__name__}, args - {args}')
        
        try:
            return func(*args, **kwargs)

        except TypeError:

            if func.__name__ == 'phone':
                return 'Enter user name. Try again'
            else:
                return 'Give me name and phone please. Try again'
            
        except KeyError:
            return 'You entered a wrong command. Try again!'
        
    return wrapper


@input_error
def add(name, phone_number):
    """
    "add ..."
    За цією командою бот зберігає у пам'яті (у словнику наприклад) новий контакт. 
    Замість ... користувач вводить ім'я та номер телефону, обов'язково через пробіл.
    """
    DICT_PHONES[name] = phone_number

    return f'Added the new contact: {name = }; {phone_number}'


@input_error
def change(name, phone_number):
    """
    "change ..."
    За цією командою бот зберігає в пам'яті новий номер телефону існуючого контакту. 
    Замість ... користувач вводить ім'я та номер телефону, обов'язково через пробіл.
    """
    DICT_PHONES[name] = phone_number

    return f'The contact: {name = } was changed phone number to {phone_number}'


def goodbye():
    """
    "good bye", 
    "close", 
    "exit" 
    По будь-якій з цих команд бот завершує свою роботу після того, як виведе у консоль "Good bye!".
    """
    return 'Good Bye!'


def hello():
    """
    "hello"
    Відповідає у консоль "How can I help you?"
    """
    return 'How can I help you?'


@input_error
def phone(name):
    """
    "phone ...."
    За цією командою бот виводить у консоль номер телефону для зазначеного контакту. 
    Замість ... користувач вводить ім'я контакту, чий номер треба показати.
    """
    if name in DICT_PHONES:
        result = 'The phone dictionary has next contact:\n'
        result += f'   {name:<15} {DICT_PHONES[name]}'
    else:
        result = 'No results. The phone dictionary hasn\'t contact with this name'

    return result


def show_all():
    """
    "show all"
    За цією командою бот виводить всі збереженні контакти з номерами телефонів у консоль.
    """
    if not DICT_PHONES:

        return 'The phone dictionary is empty'
    
    result = 'The phone dictionary has next contacts:\n'

    for count, (name, phone) in enumerate(DICT_PHONES.items()):

        result += f'{count+1:<2} {name:<15} {phone}\n'

    return result


def parse_input(user_input):

    user_input = user_input.split()

    request = list()

    len_command = len(user_input)

    if len_command == 1:
        request.append(user_input[0])
    elif len_command == 2 and user_input[0].lower() == 'show':
        request.append(' '.join(user_input))
    elif len_command == 2:
        request.append(user_input[0])
        request.append(user_input[1])
    else:
        request.append(user_input[0])
        request.append(user_input[1])
        request.append(user_input[2])

    request[0] = request[0].lower()

    return request


@input_error
def get_handler(command):
    return COMMANDS[command]





def main():

    cycle = 0
    while True:

        if DEBUG:
            cycle += 1
            print(f'\n{cycle = }')

        # Type of requests:
        # +  hello
        # +  add Vitalii 0637609640
        # +  change Vitalii 0984520
        # +  phone Vitalii
        # +  show all
        # +  good bye
        # +  close
        # +  exit    

        user_input = input('>>> ')

        request = parse_input(user_input)

        handler = get_handler(request.pop(0))
        
        if not isinstance(handler, str):

            if request:
                result = handler(*request)
            else:
                result = handler()

        else:
            result = handler

        print(result)

        if result == 'Good Bye!':
            break

    
DEBUG = False

if __name__ == '__main__':

    COMMANDS = {
        'hello': hello,
        'good bye' : goodbye,
        'close' : goodbye,
        'exit' : goodbye,
        'show all' : show_all,
        'phone' : phone,
        'add' : add,
        'change' : change
    }

    DICT_PHONES = {
        'Vitalii': '0637609640',
        'Oleg': '0637546853'
    }

    main()
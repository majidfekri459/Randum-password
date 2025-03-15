import random ,string ,os
settings={'upper': True,#حروف بزرگ
    'lower': True,#حروف کوچک
    "number": True,#کارکتور عدد
    'symbol': False, #کارکتور خارج از عدد و حروف
    'space': False,#فاصله
    "persian": False, #حروف فارسی
    'length': 8 #طول تعداد کارکتور
}

PW_MIN_LENGHT=4
PW_MAX_LENGTH=30

def get_os():
    os.system("cls")

def yes_or_no(option,default):
    while True:
        user_input=input(f'Include {option:8}? default is {str(default):6}'
                        ' (y: yes, n: no, enter: default ) ')
        user_input=user_input.lower()
        if user_input=='':
            return default
        if user_input in ['y','n']:
            return user_input=='y'
        print("Invalid input. please try again." )

def passeord_length(option,default,pw_min_length=PW_MIN_LENGHT,pw_max_length=PW_MAX_LENGTH):
    while True:
        user_input=input(f'enter password length. (default is {default}) (enter: default) ')
        if user_input=="":
            return default
        if user_input.isdigit():
            if PW_MIN_LENGHT<= int(user_input) <=PW_MAX_LENGTH:
                return (user_input)
            print('Invalit input.')
            print(f'Password length should be between {pw_min_length} and {pw_max_length}')
        else:
            print('Invalid input. You should enter a number.')
        print('please try again.')

def loop_settings(settings):
    while True:
        mad=chr(10003)
        list_true=[]
        for option,default in settings.items():
            if option !='length':
                user_input=yes_or_no(option,default)
                list_true.append(user_input)
                settings[option]=user_input
        if any(list_true):
            print('_'*5)
            break
        else:
            print("_"*5)
            print(f"Be sure to be (True {mad} y) ")
            print("_"*5)
    user_password_length=passeord_length(option,default)
    settings[option]=user_password_length

def get_random_upper_case():
    return random.choice(string.ascii_uppercase)
def get_random_lower_case():
    return random.choice(string.ascii_lowercase)
def get_random_number_case():
    return random.choice('0123456789')
def get_random_symbol_case():
    return (random.choice("""!@#$%^&*(<=-+_>)/\'"`~:;,[{|}]"""))
def get_random_persian_case():
    return random.choice('آابپتجچحخدذرزژسشصضعغفقکگلمنوهی')

def generate_random_char(chouces):
    choice= random.choice(chouces)
    if choice== 'upper':
        return get_random_upper_case()
    if choice== 'lower':
        return get_random_lower_case()
    if choice == 'number':
        return get_random_number_case()
    if choice== 'symbol':
        return get_random_symbol_case()
    if choice=='persian':
        return get_random_persian_case()
    if choice=='space':
        return ''

def password_generator(settings):
    final_password=''
    password_length=settings['length']
    # print('number',type(password_length))
    choice=list(filter(lambda x: settings[x],['upper','lower','number','space','symbol','persian']))
    # print(choice)
    for m in range(int(password_length)):
        final_password+= generate_random_char(choice)
    return final_password

def chech_another():
    while True:
            user_another=input('regenerate? (y: yes, n: no, enetr: yes): ')
            user_another=user_another.lower()
            if user_another in ['y','n','']:
                if user_another== 'n':
                    return False
                return True
            else:
                print('Invalid input. (y: yes, n: no, enetr: yes): ')
                print('please try again.')
                print('_'*5)

def password_generator_loop(settings):
    while True:
        print('_'*20)
        print( f'Generator password: {password_generator(settings)}')
        print('_'*5)
        if chech_another()==False:
            break

def ask_if_change_settings(settings):
    while True:
        print((settings))
        print()
        user_answer=input('Do you want to change default setiings? (y: yes, n: no, enter: yes: ) ')
        user_answer=user_answer.lower()
        if user_answer in ['y','','n']:
            if user_answer in ['','y']:
                print()
                print('_'*5, 'Change settings','_'*5,sep=' ')
                print('_'*5)
                loop_settings(settings)
            break
        else:
            print('Invalid input.')
            print('please try again')
            print('_'*5)

def run():
    get_os()
    ask_if_change_settings(settings)
    password_generator_loop(settings)
    print("_"*5)
    print('Thank you for choice us.')
    print('_'*5)
run()



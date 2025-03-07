from random import randint


def attack(char_name, char_class):
    if char_class == 'warrior':
        attack = 5 + randint(3, 5)
        return (f'{char_name} нанёс урон противнику равный {attack}')
    if char_class == 'mage':
        attack = 5 + randint(5, 10)
        return (f'{char_name} нанёс урон противнику равный {attack}')
    if char_class == 'healer':
        attack = 5 + randint(-3, -1)
        return (f'{char_name} нанёс урон противнику равный {attack}')
    return f'{char_name} do not attack'


def defence(char_name, char_class):
    if char_class == 'warrior':
        defence = 10 + randint(5, 10)
        return (f'{char_name} блокировал {defence} урона')
    if char_class == 'mage':
        defence = 10 + randint(-2, 2)
        return (f'{char_name} блокировал {defence} урона')
    if char_class == 'healer':
        defence = 10 + randint(2, 5)
        return (f'{char_name} блокировал {defence} урона')
    return f'{char_name} do not defence'


def special(char_name, char_class):
    if char_class == 'warrior':
        special = 80 + 25
        text = 'применил специальное умение «Выносливость'
        return (f'{char_name} {text} {special}»')
    if char_class == 'mage':
        special = 5 + 40
        return (f'{char_name} применил специальное умение «Атака {special}»')
    if char_class == 'healer':
        special = 10 + 30
        return (f'{char_name} применил специальное умение «Защита {special}»')
    return f'{char_name} do not cast'


def start_training(char_name, char_class):
    if char_class == 'warrior':
        print(f'{char_name}, ты Воитель — отличный боец ближнего боя.')
    elif char_class == 'mage':
        print(f'{char_name}, ты Маг — превосходный укротитель стихий.')
    if char_class == 'healer':
        print(f'{char_name}, ты Лекарь — чародей, способный исцелять раны.')
    print('Потренируйся управлять своими навыками.')
    print('Введи одну из команд: attack — чтобы атаковать противника, '
          'defence — чтобы блокировать атаку противника или special — чтобы '
          'использовать свою суперсилу.')
    print('Если не хочешь тренироваться, введи команду skip.')

    cmd = None

    while cmd != 'skip':
        cmd = input('Введи команду: ')
        if cmd == 'attack':
            print(attack(char_name, char_class))
        if cmd == 'defence':
            print(defence(char_name, char_class))
        if cmd == 'special':
            print(special(char_name, char_class))
    return 'Тренировка окончена.'


def choice_char_class():
    approve_choice = None
    char_class = None
    while approve_choice != 'y':
        char_class = input('Введи название персонажа, за которого хочешь '
                           'играть: Воитель — warrior, Маг — mage, Лекарь — '
                           'healer: ')
        if char_class == 'warrior':
            print('Воитель — дерзкий воин ближнего боя. Сильный, '
                  'выносливый и отважный.')
        if char_class == 'mage':
            print('Маг — находчивый воин дальнего боя. Обладает высоким '
                  'интеллектом.')
        if char_class == 'healer':
            print('Лекарь — могущественный заклинатель. Черпает силы из '
                  'природы, веры и духов.')
        approve_choice = input('Нажми (Y), чтобы подтвердить выбор, или '
                               'любую другую кнопку, чтобы выбрать другого '
                               'персонажа ').lower()
    return char_class


def main():
    print('Приветствую тебя, искатель приключений!')
    print('Прежде чем начать игру...')
    char_name = input('...назови себя: ')
    print(f'Здравствуй, {char_name}! '
          f'Сейчас твоя выносливость — 80, атака — 5 и защита — 10.')
    print('Ты можешь выбрать один из трёх путей силы:')
    print('Воитель, Маг, Лекарь')
    char_class = choice_char_class()
    print(start_training(char_name, char_class))


main()

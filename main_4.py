import random as rnd


class Game:
    pass


class Character:
    pass


class Character:
    __firstNamesHeroes = ['Застенчивый', 'Сокрушительный', 'Невероятный', 'Странный', 'Угрюмый', 'Невыносимый',
                          'Глупый', 'Чванливый', 'Милый', 'Жёсткий', 'Непобедимый', 'Беспечный', 'Осмелевший']
    __lastNamesHeroes = ['Гном', 'Проказник', 'Дурак', 'Шутник', 'Ездок', 'Лгун',
                         'Сокрушитель', 'Орк', 'Трус', 'Рыболов', 'Воришка', 'Бандит']
    __presentation = ['по прозвищу', 'зовущийся', 'которого кличут', 'по кличке', 'наречённый']
    __Class = "Неизвестный"
    __firstNamesBoses = ['Гигант', 'Титан', 'Медведь', 'Злыдень', 'Потрошитель', 'Повергающий в ужас']
    __lastNamesBoses = ['Убийца', 'Захватчик', 'Маньяк', 'Кровопийца', 'Уничтожитель']
    __lastWords = ['Как пройти в библиотеку?', 'Я ещё вернусь!', 'Утюг забыл выключить...', 'Отомстите за меня!',
                   '(_#@*!!!', 'Встретимся в АДУ!', 'Теперь отдохну...']
    __bodyParts = ['по ноге', 'по голове', 'в руку', 'в колено', 'в живот']

    def __init__(self, hp: int, damage: int):
        self.__about = "Это пример описания."
        self.__hp = hp
        self.__damage = damage
        self.__hitChance = rnd.randint(50, 100)
        self.__weaponLevel = rnd.randint(1, 100)
        self.__name = "Неизвестный"
        self.__isDead = False

    def take_damage(self, damage):
        print(f'{self.Class} {self.name} получает урон в {int(damage)} HP.')
        self.__hp -= damage
        if self.__hp < 0:
            self.__hp = 0

    def super_ability(self, *args):
        pass

    def hint(self, enemy: Character, level):
        print(f"{self.Class} {self.name} бьёт {enemy.Class} {enemy.name} ", end='')
        if rnd.randint(1, 100) <= self.__hitChance:
            print(f"и попадает ему {rnd.choice(Character.__bodyParts)}.")
            enemy.take_damage(self.__damage)
            return True
        else:
            isSelfDamage = 0
            print(f'но промахивается', end='')
            if rnd.randint(1, 100) >= self.__weaponLevel:
                print(f' и попадает себе {rnd.choice(Character.__bodyParts)}', end='')
                isSelfDamage = 1
            print('...')
            if isSelfDamage == 1:
                self.take_damage(int(self.__damage * rnd.random()))
            return False

    def info(self):
        return f"{self.Class} {self.name} Здоровье: {int(self.hp)}, " \
               f"Урон: {int(self.damage)}"

    def isAlive(self):
        if self.__hp > 0:
            return True
        else:
            return False

    @staticmethod
    def hero_name_generator():
        return rnd.choice(Character.__firstNamesHeroes) + ' ' + rnd.choice(Character.__lastNamesHeroes)

    @staticmethod
    def boss_name_generator():
        return rnd.choice(Character.__firstNamesBoses) + ' ' + rnd.choice(Character.__lastNamesBoses)

    @property
    def weaponLevel(self):
        return self.__weaponLevel

    @property
    def bodyParts(self):
        return self.__bodyParts

    @property
    def Class(self):
        return self.__Class

    @Class.setter
    def Class(self, Class):
        self.__Class = Class

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def hitChance(self):
        return self.__hitChance

    @hitChance.setter
    def hitChance(self, hitChance: int):
        self.__hitChance = hitChance

    @property
    def hp(self):
        return self.__hp

    @hp.setter
    def hp(self, hp: int):
        self.__hp = hp

    @property
    def damage(self):
        return self.__damage

    @damage.setter
    def damage(self, damage):
        self.__damage = damage

    @property
    def isDead(self):
        return self.__isDead

    @isDead.setter
    def isDead(self, isDead):
        self.__isDead = isDead

    @property
    def presentation(self):
        return self.__presentation

    @property
    def about(self):
        return self.__about

    @about.setter
    def about(self, about):
        self.__about = about

    def death(self):
        print(f'{self.Class} {self.name} УМИРАЕТ со словами: "{rnd.choice(self.__lastWords)}"')
        self.__isDead = True

    def __str__(self):
        return f"{self.Class} {rnd.choice(Character.__presentation)} {self.name} Здоровье: {int(self.hp)}, " \
               f"Урон: {int(self.damage)}, Шанс успешной атаки: {int(self.hitChance)}, Владение оружием: {int(self.__weaponLevel)}\n" \
               f"Способность: {self.__about}"


class Hero(Character):
    def __init__(self, hp: int, damage: int):
        super().__init__(hp, damage)
        self.name = '"' + Character.hero_name_generator() + '"'


class Boss(Character):
    def __init__(self, hp: int, damage: int):
        self.Class = "Босс"
        super().__init__(hp, damage)
        self.name = '"' + Character.boss_name_generator() + '"'
        self.__deafLevel = -1
        self.__enterDamage = self.damage

    def get_deafness(self, level):
        self.__deafLevel = level + 1

    def __check_deafness(self, level):
        if level == self.__deafLevel:
            return True
        else:
            return False

    def update_damage(self, damadge):
        self.damage = damadge

    def damage_back(self):
        self.damage = self.__enterDamage

    def hint(self, enemy: Character, level):
        if not self.__check_deafness(level):
            super().hint(enemy, level)
        else:
            print(f"{self.Class} {self.name} хотел бы ударить {enemy.Class} {enemy.name} но он оглушен...")

    def __str__(self):
        return f"{self.Class} {rnd.choice(self.presentation)} {self.name} Здоровье: {int(self.hp)}, " \
               f"Урон: {int(self.damage)}, Шанс успешной атаки: {int(self.hitChance)}, Владение оружием: {int(self.weaponLevel)}"


class Berserk(Hero):

    def __init__(self, hp: int, damage: int):
        self.Class = "Берсерк"
        super().__init__(hp, damage)
        self.__agregateDamage = 0
        self.__enterDamage = self.damage
        self.about = f"Накапливает полученный урон и возвращает его Боссу со своими ударами."

    def take_damage(self, damage):
        self.__agregateDamage += damage
        super().take_damage(damage)

    def hint(self, enemy: Character, level):
        plusDamage = int(self.__agregateDamage * rnd.random())
        self.__agregateDamage -= plusDamage
        if plusDamage > 0:
            print(f"{self.Class} {self.name} долго терпел и добавил к своему урону {plusDamage}!")
        self.damage += plusDamage
        super().hint(enemy, level)
        self.damage = self.__enterDamage


class Thor(Hero):

    def __init__(self, hp: int, damage: int):
        self.Class = "Тор"
        super().__init__(hp, damage)
        self.__deafChance = rnd.randint(15, 70)
        self.about = f"С вероятностью в {self.__deafChance}% может оглушить Босса на весь следующий за текущим раунд."

    def hint(self, enemy: Boss, level):
        if rnd.randint(1, 100) <= self.__deafChance:
            print(f"{self.Class} {self.name} бьёт {enemy.Class} {enemy.name} и оглушает его на следующий раунд.")
            enemy.get_deafness(level)
        else:
            super().hint(enemy, level)


class Golem(Hero):

    def __init__(self, hp: int, damage: int):
        self.Class = "Голем"
        super().__init__(hp, damage)
        self.about = f"Пока он жив, он будет защищать стоящих за ним героев, принимая на себя 1/5 всего урона от Босса."

    def super_ability(self, *args):
        if self.isAlive():
            minusDamage = (args[0].damage / 5)
            print(f"{self.Class} {self.name} принимает на себя 1/5 от урона Босса...")
            self.take_damage(minusDamage)
            args[0].update_damage(args[0].damage - minusDamage)


class Witcher(Hero):

    def __init__(self, hp: int, damage: int):
        self.Class = "Ведьмак"
        super().__init__(hp, damage)
        self.__chanceToAlive = 100
        self.about = f"Не бьёт Босса, но может пожертвовать собой для воскрешения умершего члена комманды."

    def hint(self, enemy: Character, level):
        print(f"{self.Class} {self.name} как обячно не бьёт Босса...")

    def super_ability(self, *args):
        if rnd.randint(1, 100) < self.__chanceToAlive:
            for i, x in enumerate(args[1]):
                if not x.isAlive() and x != self:
                    x.hp = 100
                    x.isDead = False
                    self.hp = 0
                    print(f'{self.Class} {self.name} отдаёт свою жизнь {x.Class} {x.name}')
                    self.death()


class Sue(Hero):

    def __init__(self, hp: int, damage: int):
        self.Class = "Сью"
        super().__init__(hp, damage)
        self.__isHidden = False
        self.__hiddenChance = 100
        self.__hiddenRound = 0
        self.__argregateDamage = 0
        self.__enterDamage = self.damage
        self.__hiddenStart = 0
        self.__hiddenEnd = 0
        self.about = f"Может стать невидимой для атаки на два раунда один раз за игру. Урон, полученный в невидимости" \
                     f" накапливается и возвращается Боссу."

    def super_ability(self, *args):
        if self.__hiddenRound != 0:
            if args[2] - self.__hiddenRound <= 2:
                self.__isHidden = True
                if self.__hiddenStart == 0:
                    print(f"{self.Class} {self.name} запускает невидимость!")
                self.__hiddenStart = 1
            else:
                self.__isHidden = False
                if self.__hiddenEnd == 0:
                    print(f"У {self.Class} {self.name} закончилась невидимость!")
                self.__hiddenEnd = 1

        if self.__hiddenRound == 0:
            if rnd.randint(1, 100) < self.__hiddenChance:
                self.__hiddenRound = args[2]

    def take_damage(self, damage):
        if self.__isHidden:
            self.__argregateDamage += damage
            print(f"{self.Class} {self.name} не получает урона, потому что использует невидимость!")
        else:
            super().take_damage(damage)

    def hint(self, enemy: Character, level):
        if not self.__isHidden and self.__argregateDamage > 0:
            print(f"Сейчас {self.Class} {self.name} вернёт весь полученный урон Боссу!")
            self.damage = self.__argregateDamage + self.damage
            super().hint(enemy, level)
            self.damage = self.__enterDamage
            self.__argregateDamage = 0
        else:
            super().hint(enemy, level)


class Hacker(Hero):

    def __init__(self, hp: int, damage: int):
        self.Class = "Хакер"
        super().__init__(hp, damage)
        self.__stolenPercent = rnd.randint(5, 60)
        self.__round = rnd.randint(0, 1)
        self.about = f"Не умеет драться, зато умеет взламывать защиту Босса. Через один раунд будет воровать у Босса" \
                     f" {self.__stolenPercent}% HP и отдавать кому-то из героев."

    def hint(self, enemy: Character, level):
        print(f"{self.Class} {self.name} не бьёт Босса, потому что не умеет...")

    def super_ability(self, *args):
        if self.__round + 2 == args[2]:
            self.__round = args[2]
            stole = int((args[0].hp / 100) * self.__stolenPercent)
            print(f"{self.Class} {self.name} взламывает Босса и переводит {stole} HP ", end='')
            args[0].hp -= stole
            heroes = []
            for x, i in enumerate(args[1]):
                if i.isAlive() and i != self:
                    heroes.append(x)
            choice = rnd.choice(heroes)
            args[1][choice].hp += stole
            print(f"{args[1][choice].Class} {args[1][choice].name}!")


class AntMen(Hero):

    def __init__(self, hp: int, damage: int):
        self.Class = "Человек-Муравей"
        super().__init__(hp, damage)
        self.__enterHp = self.hp
        self.__enterDamage = self.damage
        self.__N = rnd.randint(10, 70)
        self.__lastPercent = 0
        self.about = f"В каждом раунде может увеличиться или уменьшиться величину до {self.__N}%. " \
                     f"На эту же величину изменяются его жизни и урон."

    def super_ability(self, *args):
        if self.__lastPercent > 0:
            self.hp += (self.hp / 100) * -self.__lastPercent
            self.damage += (self.damage / 100) * -self.__lastPercent
        if self.__lastPercent < 0:
            self.hp += (self.hp / 100) * abs(self.__lastPercent)
            self.damage += (self.damage / 100) * abs(self.__lastPercent)

        percent = rnd.randint(-self.__N, self.__N)
        self.__lastPercent = percent
        self.hp += (self.hp / 100) * percent
        self.damage += (self.damage / 100) * percent
        if percent < 0:
            print(f'{self.Class} {self.name} уменьшился на {abs(percent)}%')
        if percent > 0:
            print(f'{self.Class} {self.name} увеличился на {abs(percent)}%')


class Game:

    def __init__(self):
        self.re_generate()
        self.__heroes = ()
        self.__bossCount = 0
        self.__heroesCount = 0

    def __isGameInProcess(self):
        if self.__isBossAlive() and self.__isHeroesAlive():
            return 0
        elif self.__isBossAlive():
            return 1
        elif self.__isHeroesAlive():
            return 2
        else:
            return 3

    def __isBossAlive(self):
        if self.__boss.isAlive():
            return True
        else:
            return False

    def __isHeroesAlive(self):
        for i in self.__heroes:
            if i.isAlive():
                return True
        return False

    def info(self):
        print("Boss:")
        print(self.__boss)
        print("Heroes:")
        for i in self.__allHeroes:
            print(i)

    def menu(self):
        while True:
            self.re_generate()
            command = []
            numbers = []
            print(f"____________________________ Счёт: ________________________________\n"
                  f"                      Боссы: {self.__bossCount} Герои: {self.__heroesCount}")
            print("____________________________________________________________________\n"
                  "                Сейчас вам предстоит сразиться с:")
            print(self.__boss)
            print("____________________________________________________________________\n"
                  "Вы можете выбрать только ТРЁХ героев для сражения! Выбирайте с умом:\n")
            for i, x in enumerate(self.__allHeroes):
                print(f"{i + 1}: {x}")
                numbers.append(i + 1)
            while len(command) < 3:
                choice = input("\n"
                               "Введите номер героя для добавления в команду> ")
                if choice.isdigit() and int(choice) in numbers:
                    num = int(choice) - 1
                    if num in command:
                        print("Вы уже выбрали этого героя...")
                    else:
                        command.append(num)
                        print(f'{self.__allHeroes[num].Class} {self.__allHeroes[num].name} добавлен!')
            self.__heroes = (self.__allHeroes[command[0]], self.__allHeroes[command[1]], self.__allHeroes[command[2]])
            print("Команда собрана!")
            input("Нажмите ENTER чтобы начать сражение> ")
            self.__fight()

    def re_generate(self):
        self.__boss = Boss(rnd.randint(400, 600), rnd.randint(20, 30))
        berserk = Berserk(rnd.randint(90, 120), rnd.randint(10, 15))
        tor = Thor(rnd.randint(80, 100), rnd.randint(8, 15))
        golem = Golem(rnd.randint(120, 200), rnd.randint(10, 15))
        witcher = Witcher(rnd.randint(100, 120), rnd.randint(1, 1))
        sue = Sue(rnd.randint(90, 110), rnd.randint(10, 15))
        hacker = Hacker(rnd.randint(60, 120), rnd.randint(1, 1))
        antmen = AntMen(rnd.randint(100, 100), rnd.randint(10, 15))
        self.__allHeroes = (berserk, tor, golem, witcher, sue, hacker, antmen)

    def __fight(self):
        rounds = 1
        while not self.__isGameInProcess():
            print(f'-------------------------------------------------------------------------------')
            print(f'                               Раунд {rounds}')
            print(f'-------------------------------------------------------------------------------')
            for i in self.__heroes:
                if self.__boss.isAlive() and i.isAlive():
                    self.__boss.hint(i, rounds)
                if not i.isAlive() and not i.isDead:
                    i.death()
                if self.__boss.isAlive() and i.isAlive():
                    i.hint(self.__boss, rounds)
                if not self.__boss.isAlive() and not self.__boss.isDead:
                    self.__boss.death()
                if i.isAlive():
                    i.super_ability(self.__boss, self.__heroes, rounds)
            self.__boss.damage_back()
            rounds += 1
            print(f'-------------------------------------------------------------------------------')
            print(f'                               Статистика:')
            print(f'-------------------------------------------------------------------------------')
            print(self.__boss.info())
            for i in self.__heroes:
                print(i.info())
        if self.__isGameInProcess() == 1:
            self.__bossCount += 1
            print(f"\n****************************** ПОРАЖЕНИЕ **************************************")
            print(f"                  {self.__boss.Class} {self.__boss.name} победил героев!")
            print(f"*******************************************************************************")
        elif self.__isGameInProcess() == 2:
            self.__heroesCount += 1
            print(f"\n******************************** ПОБЕДА **************************************")
            print(f"                  Герои победили {self.__boss.Class} {self.__boss.name}!")
            print(f"*******************************************************************************")
        else:
            print(f"\n********************************* НИЧЬЯ **************************************")
            print(f"                         В этот раз никто не победил...")
            print(f"*******************************************************************************")
        choice = 0
        while choice not in ['Y', 'y', 'N', 'n']:
            choice = input("Хотите сыграть ещё раз? Y/N> ")
        if choice == 'N' or choice == 'n':
            exit()


game = Game()
game.menu()

# '''
# Значение термина «инкапсуляция» расплывчато и отличается от источника к _name
# источнику. Принято считать, что инкапсуляция — один из основополагающих
# принципов ООП, хотя некоторые научные статьи вовсе упускают инкапсуляцию
# из списка. К примеру, Джон Митчелл в книге «Концепты в языках
# программирования» при перечислении основных концептов в ООП упоминает
# только абстракцию — термин который принято считать близким к
# инкапсуляции по значению, но все-же более обширным и высокоуровневым. С
# другой стороны, Роберт Мартин в его книге «Чистая архитектура» явно говорит о том, что инкапсуляция, наследование и полиморфизм считается
# фундаментом ООП.

# Разнообразие определений, данных термину «инкапсуляция», сложно привести
# к общему знаменателю. В целом можно выделить два подхода к значению
# этого термина. 
# Инкапсуляция может быть рассмотрена как:

# ● связь данных с методами которые этими данными управляют;
# ● набор инструментов для управления доступом к данным или
# методам которые управляют этими данными.
# '''

# ####    Инкапсуляция как связь    ######

# '''
# Подобного рода трактовка термина «инкапсуляция» очень проста в
# объяснении. В данном случае, любой класс в котором есть хотя бы одна
# переменная и один метод который ею управляет наглядно демонстрирует этот
# принцип.
# '''


# class Phone:
#     number = "111-11-11"

#     def print_number(self):
#         print( "Phone number is: ", self.number )

# my_phone = Phone()
# my_phone.print_number()

# '''
# Можно создать класс, который состоит только из методов (и не содержит
# переменных), что может быть удобно в некоторых языках программирования.
# Также возможно создать класс содержащий только данные, без методов, чего,
# во многих случаях, следует избегать. Обе практики следует применять в случае
# необходимости и их отношение к «объединяющей» инкапсуляции спорно.
# '''

# #####    Инкапсуляция как управление доступом    ######

# '''
# Объяснение концепции ограничения доступа к данным или методам требует
# гораздо большего количества деталей. Прежде всего, в этом контексте термин
# «доступ» следует понимать как способность видеть и / или изменять
# внутреннее содержимое класса. Существует несколько уровней доступа,
# предоставляемых большинством ООП языков. Обобщая можно сказать что
# данные объекта могут быть:

# ● публичными (public) — данные доступны всем;

# ● приватными (private) — данные доступны только объекту/классу
# которому они принадлежат;
# защищенный  (protected)


# #####    Python 3 предоставляет 3 уровня доступа к данным:   ######


# - публичный (public, нет особого синтаксиса, publicBanana);

# - защищенный (protected, одно нижнее подчеркивание в начале
# названия, _protectedBanana);

# - приватный (private, два нижних подчеркивания в начала названия,
# __privateBanana).

# '''
# Для краткости и простоты, только два базовых уровня (приватный и публичный)
# освещены в примере.
# '''

# class Phone:
#     username = "Kate" # public variable
#     __how_many_times_turned_on = 0 # private variable

#     def call(self): # public method
#         print( "Ring-ring!" )

#     def __turn_on(self): # private method
#         self.__how_many_times_turned_on += 1
#         print("Times was turned on: ", self.__how_many_times_turned_on)

# my_phone = Phone()
# my_phone.call()
# print("The username is:", my_phone.username)
# # my_phone.turn_on()
# print(dir(my_phone))
# # my_phone.__turn_on()
# print("Turned on:", my_phone.__how_many_times_turned_on)
# print( "Turned on: ", my_phone.how_many_times_turned_on)
# will produce an error



# #####   Нарушение инкапсуляции    ######

# '''
# Сам язык предоставляет программисту синтаксический инструмент, который
# может обойти инкапсуляцию. Читать и изменять частные переменные и
# вызывать частные функции все же возможно.
# '''

# class Phone:
#     username = "Kate" # public variable
#     __serial_number = "11.22.33" # private variable
#     __how_many_times_turned_on = 0 # private variable

#     def call(self): # public method
#         print( "Ring-ring!" )
    
#     def __turn_on(self): # private method
#         self.__how_many_times_turned_on += 1
#         print( "Times was turned on: ", self.__how_many_times_turned_on)


# my_phone = Phone()
# my_phone._Phone__turn_on()
# my_phone._Phone__serial_number = "44.55.66"
# print( "New serial number is ", my_phone._Phone__serial_number )


# '''

# Касательно инкапсуляции непосредственно в языке программирования Python скрыть атрибуты класса можно сделав их приватными или закрытыми и ограничив доступ к ним через специальные методы, которые еще называются свойствами.

# А попытка получить его значение приведет к ошибке выполнения:
# '''

class Human():
    # __private - переменная
    __privateVar = "this is __private variable"

    def __init__(self):
        self.className = "Human class constructor"
        self.__privateVar = "this is redefined __private variable"

    # public - доступен везде
    def showName(self, name):
        self.name = name
        return self.__privateVar + " " + name

    # __private - Доступен только в базовом классе
    def __privateMethod(self):
        return "Private method"

    # _protected - Доступен в классах - наследниках
    def _protectedMethod(self):
        return "Protected method"

    # __private - Доступен ТОЛЬКО из базового класса
    def showPrivate(self):
        return self.__privateMethod()

    def showProtecded(self):
        return self._protectedMethod()


class Male(Human):
    def showClassName(self):
        return "Male"

    # def showPrivate(self):
    #     return self.__privateMethod()

    def showProtected(self):
        return self._protectedMethod()


class Female(Human):
    def showClassName(self):
        return "Female"

    def showPrivate(self):
        return self.__privateMethod()

    def showProtected(self):
        return self._protectedMethod()


h = Human()
print(h.className)
print(h.showName("Vasya"))
print(h.showPrivate())
print(h.showProtecded())
# print(h.__privateMethod())
print(h._protectedMethod())
print("\n")

m = Male()
print(m.className)
print(m.showClassName())
print(m.showPrivate())
print(m.showProtected())
print("\n")

f = Female()
print(f.className)
print(f.showClassName())
print(f.showProtected())
print("\n")
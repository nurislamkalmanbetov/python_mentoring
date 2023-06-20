# Полиморфизм


# def a(c: float, d:int):
#     return c*d

# print(a(3.5, 6))
# print(a(6))

# Термин полиморфизм буквально означает наличие нескольких форм. В контексте
# объектно-ориентированного программирования, полиморфизм означает способность 
# объекта вести себя по-разному.

# Полиморфизм в программировании реализуется через перегрузку метода, либо 
# через его переопределение.



# Перегрузка метода
# Перегрузка метода относится к свойству метода вести себя по-разному, в
# зависимости от количества или типа параметров. Взглянем на очень простой пример перегрузки метода. Выполним следующий скрипт:


# class Car:  
#    def start(self, a, b=None):
#         if b is not None: # == 
#             print (a + b)
#         else:
#             print (a)

# car_a = Car()  
# car_a.start(10)
# car_a.start(10, 20)

a = 5672384961321412
b = a

c = [1, 3]
d = c

print(id(a))
print(id(b))
print(id(c))
print(id(d))
print(a == b)
print(a is b)
print(c == d)
print(c is d)


# Переопределение метода

# Переопределение метода относится к наличию метода с одинаковым названием в дочернем и родительском классах. Определение метода отличается в родительском и дочернем классах, но название остается тем же. Давайте посмотрим на простой пример переопределения метода в Python.


class Country:
  def capital(self):
    pass
  
  def language(self):
    pass
  
  def type_():
    pass


class India(Country): 
    def capital(self): 
        print("New Delhi is the capital of India.") 
  
    def language(self): 
        print("Hindi the primary language of India.") 
  
    def type_(self): 
        print("India is a developing country.") 
  
class USA(Country): 
    def capital(self): 
        print("Washington, D.C. is the capital of USA.") 
  
    def language(self): 
        print("English is the primary language of USA.") 
  
    def type_(self): 
        print("USA is a developed country.") 
  
obj_ind = India() 
obj_usa = USA() 
for country in (obj_ind, obj_usa): 
    country.capital() 
    country.language() 
    country.type_() 


# # example 2

# class Person:
#     def __init__(self, name):    # Constructor of the class
#         self.name = name

#     def talk(self):              # Abstract method, defined by convention only
#         raise NotImplementedError("Subclass must implement abstract method")

# class American(Person):
#     def talk(self):
#         return 'Hello, Do you speak English?'

# class Russian(Person):
#     def talk(self):
#         return 'Привет, а ты говоришь по русский?'


# tourists = [American('Martin'),
#           Russian('Григорий')]

# for tourist in tourists:
#     print(tourist.name + ':  ' + tourist.talk())



# example 3

# class Parrot:
#     def fly(self):
#         print("Parrot can fly")
    
#     def swim(self):
#         print("Parrot can't swim")

# class Penguin:

#     def fly(self):
#         print("Penguin can't fly")
    
#     def swim(self):
#         print("Penguin can swim")

# # common interface
# def flying_test(bird):
#     bird.fly()

# #instantiate objects
# blu = Parrot()
# peggy = Penguin()

# # passing the object
# flying_test(blu)
# flying_test(peggy)




# class Shark():

#     def swim(self):
#         print("The shark is swimming.")

#     def swim_backwards(self):
#         print("The shark cannot swim backwards, but can sink backwards.")

#     def skeleton(self):
#         print("The shark's skeleton is made of cartilage.")

# class Clownfish():

#     def swim(self):
#         print("The clownfish is swimming.")
    
#     def swim_backwards(self):
#         print("The clownfish can swim backwards.")
    
#     def skeleton(self):
#         print("The clownfish's skeleton is made of bone.")



# wally = Shark()
# wally.skeleton()
# casey = Clownfish()
# casey.skeleton()

# for fish in (wally, casey):
#     fish.swim()
#     fish.swim_backwards()
#     fish.skeleton()



# def in_the_pacific(fish):
#     fish.swim()


# in_the_pacific(wally)
# in_the_pacific(casey)



# class Shape:
#     """
#     This is a parent class that is intended to be inherited by other classes
#     """

#     def calculate_area(self):
#         """
#         This method is intended to be overridden in subclasses.
#         If a subclass doesn't implement it but it is called, NotImplemented will be raised.

#         """
#         raise NotImplemented

# class Square(Shape):
#     """
#     This is a subclass of the Shape class, and represents a square
#     """
#     side_length = 2     # in this example, the sides are 2 units long

#     def calculate_area(self):
#         """
#         This method overrides Shape.calculate_area(). When an object of type
#         Square has its calculate_area() method called, this is the method that
#         will be called, rather than the parent class' version.

#         It performs the calculation necessary for this shape, a square, and
#         returns the result.
#         """
#         return self.side_length * 2

# class Triangle(Shape):
#     """
#     This is also a subclass of the Shape class, and it represents a triangle
#     """
#     base_length = 4
#     height = 3

#     def calculate_area(self):
#         """
#         This method also overrides Shape.calculate_area() and performs the area
#         calculation for a triangle, returning the result.
#         """

#         return 0.5 * self.base_length * self.height

# def get_area(input_obj):
#     """
#     This function accepts an input object, and will call that object's
#     calculate_area() method. Note that the object type is not specified. It
#     could be a Square, Triangle, or Shape object.
#     """

#     print(input_obj.calculate_area())

# # Create one object of each class
# shape_obj = Shape()
# square_obj = Square()
# triangle_obj = Triangle()

# # Now pass each object, one at a time, to the get_area() function and see the
# # result.
# get_area(shape_obj)
# get_area(square_obj)
# get_area(triangle_obj)
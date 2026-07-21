# Python မှာ OOP (Object-Oriented Programming) ဆိုတာ Script တွေကို အစီအစဉ်တကျ ပရိုဂရမ်ရေးတဲ့ 
# စတိုင်တစ်ခုဖြစ်ပြီး၊ ပြင်ပကမ္ဘာက အရာဝတ္ထုတွေ (Objects) ရဲ့ သဘောတရားကို ယူပြီး Code တွေကို စနစ်တကျ 
# ပြန်စုစည်းရေးသားတာဖြစ်ပါတယ်။

# ရှုပ်ထွေးတဲ့ Program တွေကို ထိန်းသိမ်းရလွယ်အောင်နဲ့ Code တွေကို ထပ်ခါထပ်ခါ ပြန်သုံးလို့ရအောင် OOP က 
# အများကြီး ကူညီပေးပါတယ်။

# ၁။ OOP ရဲ့ အခြေခံ သဘောတရား (၂) ခု
# OOP ကို နားလည်ဖို့ Class နဲ့ Object ဆိုတဲ့ သဘောတရားနှစ်ခုကို မဖြစ်မနေ သိထားရပါမယ်။

# Class (အောက်ပုံစံ/စက်ပုံစံ): Object တစ်ခုမှာ ဘာတွေပါမလဲဆိုတာကို သတ်မှတ်ထားတဲ့ 
# Blueprint (အိမ်ပုံစံကြမ်း သို့မဟုတ် မုန့်လုပ်တဲ့ ပုံစံခွက်) ဖြစ်ပါတယ်။

# Object (အကောင်အထည်): Class ပုံစံခွက်အတိုင်း အကောင်အထည်ဖော်လိုက်တဲ့ သီးသန့် 
# အရာဝတ္ထု (ပုံစံခွက်နဲ့ ရိုက်ထုတ်လိုက်တဲ့ မုန့် သို့မဟုတ် အိမ်) ဖြစ်ပါတယ်။

# Class တစ်ခု ဆောက်ခြင်း
class Car:
    def __init__(self, brand, color):
        self.brand = brand  # Property (Attribute)
        self.color = color

    def drive(self):         # Method (Function inside Class)
        print(f"{self.color} ရောင် {self.brand} ကား လမ်းထွက်မောင်းနေပြီ။")

# Object များ အကောင်အထည်ဖော်ခြင်း (Instantiation)
car1 = Car("Toyota", "အနီ")
car2 = Car("Honda", "အနက်")

car1.drive()  # output: အနီ ရောင် Toyota ကား လမ်းထွက်မောင်းနေပြီ။
car2.drive()  # output: အနက် ရောင် Honda ကား လမ်းထွက်မောင်းနေပြီ။

# ၂။ OOP ရဲ့ ဒေါက်တိုင်ကြီး (၄) ခု (The 4 Pillars)
# OOP ကို စွမ်းအားထက်မြက်စေတာ ဒီအချက် (၄) ချက်ကြောင့်ပါပဲ -

# ၁. Encapsulation (အချက်အလက်များကို ထုပ်ပိုးသိမ်းဆည်းခြင်း)
# Data တွေနဲ​ Function တွေကို Class တစ်ခုထဲမှာ စုစည်းထားပြီး ပြင်ပကနေ မလိုလားဘဲ 
# တိုက်ရိုက် ပြင်ဆင်တာမျိုးမရှိအောင် ကာကွယ်ပေးတာပါ။ 
# Python မှာ Variable အရှေ့မှာ __ (Underscore နှစ်ခု) ခံပြီး Private လုပ်လို့ရပါတယ်။

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private Attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def get_balance(self):
        return self.__balance
    
# ၂. Inheritance (အမွေဆက်ခံခြင်း)
# ရှိပြီးသား Class တစ်ခုရဲ့ Feature တွေကို Class အသစ်တစ်ခုက ပြန်လည်ယူသုံး (Extend) တာ ဖြစ်ပါတယ်။ 
# Code တွေ ထပ်ရေးစရာမလိုတော့ပါဘူး။

# Parent Class
class Animal:
    def eat(self):
        print("အစာစားနေသည်။")

# Child Class (Animal ကို အမွေဆက်ခံသည်)
class Dog(Animal):
    def bark(self):
        print("ဟောင်နေသည်။")

my_dog = Dog()
my_dog.eat()   # Parent ထံမှ ပါလာသော Function
my_dog.bark()  # မိမိကိုယ်ပိုင် Function

# ၃. Polymorphism (ပုံစံအမျိုးမျိုး ပြောင်းလဲနိုင်ခြင်း)
# Class မတူပေမယ့် Function နာမည်တူတစ်ခုတည်းကို သုံးပြီး မတူညီတဲ့ 
# ရလဒ်တွေ ထွက်လာအောင် လုပ်ဆောင်ခြင်းဖြစ်ပါတယ်။

class Dog:
    def sound(self):
        return "ဝုတ် ဝုတ်!"

class Cat:
    def sound(self):
        return "မြောင်..."

# အမည်တူ sound() ကို ခေါ်ယူသော်လည်း Class အလိုက် အလုပ်မတူပါ
for animal in [Dog(), Cat()]:
    print(animal.sound())

# ၄. Abstraction (ရှုပ်ထွေးမှုများကို ဖုံးကွယ်ထားခြင်း)
# အသုံးပြုသူကို အရေးကြီးတဲ့ ရလဒ်ပဲ ပြပြီး နောက်ကွယ်က ရှုပ်ထွေးတဲ့ အလုပ်လုပ်ပုံတွေကို ဖုံးကွယ်ထားတာ ဖြစ်ပါတယ်။ 
# (ဥပမာ - ကားစတက်နှိုးလိုက်ရင် စက်နိုးသွားတာပဲ သိရပြီး အင်ဂျင်ထဲမှာ ဘာတွေ အလုပ်လုပ်သွားလဲ မသိနိုင်သလိုမျိုးပါ)။ 
# Python မှာ abc module ကို သုံးပြီး ရေးသားနိုင်ပါတယ်။

# ဘာလို့ OOP ကို သုံးသင့်တာလဲ?
# Reusability: စာကြောင်းပေါင်းများစွာ ရေးထားတဲ့ Code တွေကို အဆင်သင့် ပြန်သုံးနိုင်တယ်။

# Maintainability: Code စနစ်ကျတဲ့အတွက် Bug ရှာရတာ၊ ပြင်ဆင်ရတာ လွယ်ကူတယ်။

# Scalability: Project ကြီးလာတာနဲ့အမျှ အသစ်တွေ ထပ်တိုးရတာ ပိုမိုအဆင်ပြေတယ်။
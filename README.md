# Python OOP --- Homework Assignment

**Mavzu:** Python Object-Oriented Programming (OOP)\
**Daraja:** Beginner → Intermediate → Advanced\
**Maqsad:** Class va object bilan ishlash, method turlari, attributes,
inheritance va polymorphism konsepsiyalarini amaliy vazifalar orqali
mustahkamlash.

------------------------------------------------------------------------

## Umumiy topshiriq qoidalari

Har bir vazifani quyidagi tartibda bajaring:

1.  Masalani diqqat bilan o'qing va kerakli class'larni aniqlang.
2.  Har bir attribute class-level yoki instance-level bo'lishini
    belgilang.
3.  Metodlarni mas'uliyatiga qarab ajrating.
4.  Kamida 3 ta object yaratib, metodlarni sinab ko'ring.
5.  Normal holatlar bilan birga edge case'larni ham tekshiring.
6.  Kodni PEP 8 talablariga muvofiq yozing.
7.  Har bir task uchun qisqa test ssenariylari yozing.

**Cheklov:** Dastlabki 12 ta taskni tashqi kutubxonalarsiz, faqat Python
built-in imkoniyatlari bilan bajaring. Tayyor yechimni ko'chirmang;
vazifalarni mustaqil ishlab chiqing.

------------------------------------------------------------------------

# Part 1. Beginner --- Class va Attributes

## Task 01. Student Management

`Student` nomli class yarating.

### Talablar

-   Class attribute: `university = "Tashkent University"`
-   Instance attributes: `name`, `age`, `student_id`
-   `get_info()` --- student ma'lumotlarini qaytarsin.
-   `is_adult()` --- student 18 yosh yoki undan katta ekanini
    tekshirsin.

### Tekshirish namunasi

``` python
student1 = Student("Ali", 22, 101)
student2 = Student("Vali", 17, 102)

print(student1.get_info())
# Name: Ali, Age: 22, ID: 101

print(student2.is_adult())
# False
```

### Qo'shimcha challenge

-   `university` qiymatini bitta object orqali o'zgartiring va boshqa
    object'larga ta'sirini kuzating.
-   Keyin `student1.university` orqali alohida qiymat biriktirib,
    natijani tahlil qiling.

------------------------------------------------------------------------

## Task 02. Bank Account

`BankAccount` class yarating.

### Talablar

-   Class attribute: `bank_name = "National Bank"`
-   Instance attributes: `owner`, `balance`, `account_number`
-   `deposit(amount)` --- hisobga pul qo'shsin.
-   `withdraw(amount)` --- hisobdan pul yechsin.
-   `get_balance()` --- joriy balansni qaytarsin.

### Business rules

-   Deposit summasi musbat bo'lishi kerak.
-   Withdraw summasi musbat bo'lishi kerak.
-   Balansdan ortiq pul yechishga ruxsat berilmasin.
-   Noto'g'ri operatsiya bajarilmasa, tushunarli xatolik qaytarilsin
    yoki exception ko'tarilsin.

### Qo'shimcha challenge

`transfer(amount, target_account)` metodini qo'shing. Pul yuborish
muvaffaqiyatsiz bo'lsa, ikkala hisob balansi ham o'zgarmasligi kerak.

------------------------------------------------------------------------

## Task 03. Employee Counter

`Employee` class yarating.

### Talablar

-   Class attribute: `employee_count = 0`
-   Instance attributes: `name`, `position`, `salary`
-   Har bir yangi object yaratilganda employee soni bittaga oshsin.
-   `get_info()` --- employee ma'lumotlarini qaytarsin.
-   `get_employee_count()` --- jami employee sonini qaytarsin.

### Muhim

`get_employee_count()` metodini `@classmethod` bilan yozing va `cls`
parametridan foydalaning.

### Qo'shimcha challenge

Employee o'chirilganda counter kamayishi kerakmi? Bu talabni qanday
ishonchli amalga oshirish mumkinligini izohlang. `__del__` ishlatishning
xavflarini ham ko'rib chiqing.

------------------------------------------------------------------------

## Task 04. Temperature Converter

`Temperature` class yarating.

### Talablar

-   Instance attribute: `celsius`
-   `to_fahrenheit()` --- object qiymatini Fahrenheit'ga o'girsin.
-   `celsius_to_fahrenheit(celsius)` --- static method.
-   `fahrenheit_to_celsius(fahrenheit)` --- static method.

Formulalar:

-   Fahrenheit = Celsius × 9 / 5 + 32
-   Celsius = (Fahrenheit − 32) × 5 / 9

### Tekshirish namunasi

``` python
temperature = Temperature(25)

print(temperature.to_fahrenheit())
# 77.0

print(Temperature.celsius_to_fahrenheit(0))
# 32.0
```

### Qo'shimcha challenge

Nega konvertatsiya formulalari uchun `staticmethod` mos kelishini,
`classmethod` yoki oddiy instance method emasligini tushuntiring.

------------------------------------------------------------------------

## Task 05. Product Management

`Product` class yarating.

### Talablar

-   Class attribute: `tax_rate = 0.12`
-   Instance attributes: `name`, `price`, `quantity`
-   `total_price()` --- quantity bo'yicha umumiy narxni hisoblasin.
-   `apply_discount(percent)` --- chegirma qo'llasin.
-   `price_with_tax()` --- soliq qo'shilgan narxni hisoblasin.
-   `change_tax_rate(rate)` --- class method orqali umumiy soliq
    stavkasini o'zgartirsin.
-   `is_valid_price(price)` --- static method orqali narx musbatligini
    tekshirsin.

### Business rules

-   Narx manfiy bo'lmasin.
-   Quantity manfiy bo'lmasin.
-   Discount 0 dan 100 gacha bo'lsin.
-   Tax rate manfiy bo'lmasin.

------------------------------------------------------------------------

# Part 2. Intermediate --- Method turlari va Inheritance

## Task 06. User Registration System

`User` class yarating.

### Talablar

-   Class attribute: `user_count`
-   Instance attributes: `username`, `email`, `password`
-   `get_profile()` --- profil ma'lumotlarini qaytarsin.
-   `get_user_count()` --- class method.
-   `validate_email(email)` --- static method.
-   `create_user(data)` --- dictionary'dan object yaratadigan class
    method.

### Tekshirish namunasi

``` python
user = User.create_user({
    "username": "ali",
    "email": "ali@example.com",
    "password": "strong-password"
})
```

### Business rules

-   Username bo'sh bo'lmasin.
-   Email formatini kamida sodda tekshiruv bilan validatsiya qiling.
-   Password'ni `get_profile()` natijasida hech qachon ko'rsatmang.

------------------------------------------------------------------------

## Task 07. Employee Inheritance

Quyidagi class hierarchy'ni yarating:

``` text
             Employee
            /    |    \
     Developer Designer Manager
```

### Parent class: `Employee`

-   `name`
-   `salary`
-   `get_info()`

### `Developer`

-   Qo'shimcha attribute: `programming_language`
-   `write_code()` metodi

### `Designer`

-   Qo'shimcha attribute: `design_tool`
-   `create_design()` metodi

### `Manager`

-   Qo'shimcha attribute: `team_size`
-   `manage_team()` metodi

### Talablar

-   Child class'lar parent class'dan inheritance olsin.
-   Constructor ichida `super().__init__()` ishlatilsin.
-   Har bir child class o'ziga xos metodga ega bo'lsin.
-   `get_info()` metodini child class'larda kengaytirib override qiling.

------------------------------------------------------------------------

## Task 08. Vehicle System

Quyidagi hierarchy'ni yarating:

``` text
             Vehicle
            /   |   \
          Car Motorcycle Truck
```

### Parent class: `Vehicle`

-   `brand`
-   `model`
-   `speed`
-   `start()`
-   `stop()`

### Child class'lar

**Car** - `number_of_doors`

**Motorcycle** - `has_sidecar`

**Truck** - `load_capacity`

### Talablar

-   `super()` yordamida parent constructor'ni chaqiring.
-   Har bir child class uchun tegishli qo'shimcha validatsiya yozing.
-   `get_info()` metodini override qiling.

### Qo'shimcha challenge

Vehicle tezligini oshirish va kamaytirish metodlarini qo'shing. Tezlik
manfiy qiymatga tushib ketmasin.

------------------------------------------------------------------------

## Task 09. Library Management

Quyidagi class'larni yarating:

-   `Book`
-   `Library`
-   `Member`

### `Book`

-   `title`
-   `author`
-   `is_available`

### `Library`

-   `books` --- library'ga tegishli kitoblar ro'yxati.
-   `add_book(book)`
-   `remove_book(book)`
-   `search_book(title)`

### `Member`

-   `name`
-   `borrowed_books`
-   `borrow_book(book)`
-   `return_book(book)`

### Business rules

-   Mavjud bo'lmagan kitobni borrow qilib bo'lmaydi.
-   Bir kitobni bir vaqtning o'zida ikki member ololmaydi.
-   Kitob qaytarilganda availability yangilanishi kerak.
-   Borrow qilinmagan kitobni return qilib bo'lmasin.

### Qo'shimcha challenge

`Library` va `Member` o'rtasidagi munosabatni composition/association
nuqtayi nazaridan izohlang.

------------------------------------------------------------------------

# Part 3. Advanced --- Polymorphism

## Task 10. Payment System

Quyidagi hierarchy'ni yarating:

``` text
                 Payment
               /    |     \
       CreditCard  PayPal  Cash
```

### Talablar

-   Parent class: `Payment`
-   Har bir child class'da `pay(amount)` metodi bo'lsin.
-   Har bir payment turi o'ziga xos to'lov jarayonini amalga oshirsin.
-   Noto'g'ri yoki manfiy summa qabul qilinmasin.

### Tekshirish namunasi

``` python
payments = [
    CreditCardPayment(),
    PayPalPayment(),
    CashPayment()
]

for payment in payments:
    payment.pay(100)
```

### Maqsad

Method overriding va polymorphism'ni amalda qo'llash. Bir xil interfeys
orqali turli implementatsiyalarni ishga tushiring.

------------------------------------------------------------------------

## Task 11. Notification System

Quyidagi class'larni yarating:

-   `Notification`
-   `EmailNotification`
-   `SMSNotification`
-   `PushNotification`

### Talablar

Har bir class quyidagi metodni implement qilsin:

``` python
send(message)
```

Barcha notification object'larini bitta list ichida saqlang va bitta
loop orqali yuborish jarayonini ishga tushiring.

### Qo'shimcha challenge

-   `Notification`ni abstract base class sifatida qayta yozing.
-   `send()` metodini `@abstractmethod` bilan belgilang.
-   Abstract class'dan to'g'ridan-to'g'ri object yaratib bo'lmasligini
    tekshiring.

------------------------------------------------------------------------

## Task 12. Shape Calculator

Quyidagi hierarchy'ni yarating:

``` text
             Shape
           /   |    \
       Circle Rectangle Triangle
```

### Talablar

Har bir class'da `calculate_area()` metodi bo'lsin.

Formulalar:

-   Circle: S = π × r²
-   Rectangle: S = a × b
-   Triangle: S = (b × h) / 2

### Qo'shimcha talablar

-   `Shape` parent class'da umumiy interfeys belgilang.
-   Child class'larda `calculate_area()` metodini override qiling.
-   Barcha shape object'larini bitta list ichida saqlang.
-   Bitta loop orqali har bir shakl yuzasini hisoblang.
-   Noto'g'ri o'lchamlar uchun validatsiya yozing.

------------------------------------------------------------------------

# Part 4. Expert --- Real-world OOP Projects

## Task 13. E-commerce System

Kichik e-commerce tizimini loyihalang.

### Tavsiya etiladigan class'lar

``` text
User
 |
 |--- Customer
 |--- Admin

Product
Order
OrderItem
ShoppingCart
Payment
```

### Functional requirements

1.  Customer mahsulotlarni cart'ga qo'sha olsin.
2.  Cart umumiy narxni hisoblashi kerak.
3.  Customer order yarata olsin.
4.  Admin mahsulot qo'sha va o'chira olsin.
5.  Payment polymorphism orqali ishlasin.
6.  Har bir order o'zining `OrderItem` object'lariga ega bo'lsin.
7.  Mahsulot quantity'si order yaratilganda tekshirilsin.
8.  Order bekor qilinsa, inventory qayta tiklansin.

### Qo'shimcha challenge

-   Discount system qo'shing.
-   Order status'larini boshqaring.
-   Noto'g'ri holatdagi status transition'larni taqiqlang.
-   Bir nechta payment provider'ni qo'llab-quvvatlang.

------------------------------------------------------------------------

## Task 14. University Management System

Quyidagi hierarchy'ni yarating:

``` text
              Person
            /   |    \
       Student Teacher Admin
```

### Functional requirements

-   Student kurslarga yozilsin.
-   Teacher kurslarga biriktirilsin.
-   Admin student va teacher'larni boshqarsin.
-   Har bir student uchun GPA hisoblansin.
-   Teacher student'ga baho qo'ya olsin.
-   Class attribute orqali jami studentlar soni yuritilsin.
-   Student yaratish uchun `classmethod` asosidagi alternative
    constructor yozilsin.

### Qo'shimcha challenge

-   `Course`, `Enrollment` va `Grade` class'larini ajrating.
-   Bir student bir kursga ikki marta yozilmasin.
-   GPA hisoblashda baholar va kreditlarni hisobga oling.
-   Domain logic'ni `print()` bilan aralashtirmang; metodlar qiymat
    qaytarsin.

------------------------------------------------------------------------

## Task 15. Ride Sharing System

Uber yoki Yandex Go'ga o'xshash kichik tizim yarating.

### Tavsiya etiladigan class'lar

``` text
User
 |
 |--- Driver
 |--- Passenger

Vehicle
 |
 |--- EconomyCar
 |--- ComfortCar
 |--- BusinessCar

Ride
Payment
```

### Functional requirements

1.  Passenger ride buyurtma qila olsin.
2.  Driver ride'ni qabul qila olsin.
3.  Ride narxi vehicle turiga qarab hisoblansin.
4.  Har bir vehicle turi o'z pricing algoritmiga ega bo'lsin.
5.  Payment turli usullarda amalga oshirilsin.
6.  Ride status quyidagi tartibda o'zgarsin:

``` text
PENDING
   |
   v
ACCEPTED
   |
   v
IN_PROGRESS
   |
   v
COMPLETED
```

7.  Bitta driver bir vaqtning o'zida bir nechta active ride qabul qila
    olmasin.
8.  Bekor qilingan ride uchun alohida status va qoidalar bo'lsin.

### Qo'shimcha challenge

-   Fare calculation uchun Strategy pattern'dan foydalaning.
-   Ride status transition'larini alohida metodlar orqali boshqaring.
-   Driver availability'ni kuzating.
-   Bir nechta passenger va driver bilan test ssenariylarini yozing.

------------------------------------------------------------------------

# OOP Concepts --- Coverage Checklist

  Concept                     Amaliyot qilinadigan task'lar
  --------------------------- -------------------------------
  Class attributes            1, 2, 3, 5, 6
  Object attributes           1--15
  Object methods              1--15
  Class methods               3, 5, 6, 14
  Static methods              4, 5, 6
  Inheritance                 7, 8, 10, 11, 12
  `super()`                   7, 8
  Method overriding           7, 8, 10, 11, 12
  Polymorphism                10, 11, 12, 13, 15
  Composition / Association   9, 13, 14, 15
  Abstract base class         11, 12
  Encapsulation               2, 5, 6, 13, 15

------------------------------------------------------------------------

# Submission Requirements

Har bir task uchun quyidagilar topshirilishi kerak:

-   [ ] Ishlaydigan Python kodi.
-   [ ] Kamida 3 ta object bilan tekshiruv.
-   [ ] Kamida 3 ta test case.
-   [ ] Edge case'lar uchun tekshiruv.
-   [ ] Class va method'lar uchun tushunarli naming.
-   [ ] PEP 8 ga mos formatlash.

## Code Review mezonlari

  Mezon                                     Baholash
  --------------------------------------- ----------
  OOP konsepsiyalarini to'g'ri qo'llash          30%
  Business logic va edge case'lar                25%
  Code quality va readability                    20%
  Test coverage                                  15%
  Naming va PEP 8                                10%
  **Jami**                                  **100%**

## Tavsiya etilgan ish tartibi

1.  Task 01--05: class, object, attributes va method turlari.
2.  Task 06--09: class method, inheritance va object'lar o'rtasidagi
    munosabatlar.
3.  Task 10--12: overriding, polymorphism va abstract class.
4.  Task 13--15: bir nechta class hamkorlik qiladigan real-world
    tizimlar.

**Muhim:** Har bir taskni mustaqil bajaring. Avval ishlaydigan sodda
yechim yozing, keyin uni refactor qiling. Murakkab pattern'larni faqat
real ehtiyoj bo'lganda qo'llang.

------------------------------------------------------------------------

## Final Challenge

15 ta task tugagach, quyidagi savollarga kod misollari bilan javob
bering:

1.  `@classmethod` va `@staticmethod` o'rtasidagi asosiy farq nima?
2.  Class attribute va instance attribute qidirilish tartibi qanday?
3.  Instance orqali class attribute'ga qiymat biriktirilsa, nima sodir
    bo'ladi?
4.  `super()` qanday ishlaydi va MRO nima?
5.  Method overriding va method overloading o'rtasida qanday farq bor?
6.  Polymorphism'ni inheritance'siz ham amalga oshirish mumkinmi?
7.  Qachon inheritance o'rniga composition tanlash kerak?
8.  Abstract class va oddiy parent class o'rtasidagi farq nima?
9.  Python'da encapsulation qanday amalga oshiriladi?
10. OOP kodini unit test qilishda qanday yondashuv ma'qul?

**Yakuniy maqsad:** OOP sintaksisini bilish bilan cheklanmasdan,
mas'uliyatlari aniq ajratilgan, kengaytiriladigan va test qilish oson
bo'lgan class-based tizimlar ishlab chiqish.

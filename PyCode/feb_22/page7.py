def function1():
    product = (1000, 'product1', 10.0, 'nice product')
    print('title: {}'.format(product[0]))
    print('price: {}'.format(product[1]))
    print('quantities: {}'.format(product[2]))
    print('description: {}'.format(product[3]))

# function1()

def function2():
    product = {
        'quantities': 1000,
        'title': 'product1',
        'price': 10.0,
        'description': 'nice product'
    }

    print('title: {}'.format(product['title']))

    mobile = {
        'model': 'iPhone XS Max 512 GB',
        'company': 'Apple',
        'price':  1.45
    }

    print('model: {}'.format(mobile['model']))

# function2()

def function3():
    person = {
        'name': 'steve jobs',
        'email': 'steve@apple.com',
        'phone': '+1343554'
    }

    # print('name: {}'.format(person['name']))

    for info in person:
        print('{} = {}'.format(info, person[info]))


# function3()

def function4():
    persons = [
        {
            'name': 'steve jobs',
            'email': 'steve@apple.com',
            'phone': '+1343554',
            'company': 'Apple'
        },
        {
            'name': 'bill gates',
            'email': 'bill@ms.com',
            'phone': '+11242342',
            'company': ''
        },
        {
            'name': 'sundar pichchai',
            'email': 'sundar@google.com',
            'email': 'sundar@hotmail.com',
            'phone': '+134672',
            'company': ''
        }
    ]

    # for person in persons:
    #     print('name = {}'.format(person['name']))
    #     print('email = {}'.format(person['email']))
    #     print('phone = {}'.format(person['phone']))
    #     print('company = {}'.format(person['company']))

    # for person in persons:
    #     for key in person:
    #         print('{} = {}'.format(key, person[key]))

    # for person in persons:
    #     for (key, value) in person:
    #         print('{} = {}'.format(key, value))

# function4()

def function5():
    cars = [
        ('i20', 'hyundai', 7.5),
        ('i10', 'hyundai', 5.5),
        ('Fortuner', 'toyota', 37),
        ('nano', 'tata', 1.5),
    ]

    # for car in cars:
    #     print(type(car))
    #     print(car)
    #     print('model: {}'.format(car[0]))
    #     print('company: {}'.format(car[1]))
    #     print('price: {}'.format(car[2]))

    for (model, company, price) in cars:
        print('model: {}'.format(model))
        print('company: {}'.format(company))
        print('price: {}'.format(price))

# function5()

def function6():
    persons = [
        ('steve jobs', 'steve@apple.com', '+12343445'), # 0
        ('bill gates', 'bill@ms.com', '+188888')        # 1
    ]

    persons.append(('guido rossum', 'guido@python.org', '+123424'))

    print('email address of bill gates: {}'.format(persons[1][1]))
    persons[1][1] = 'bill@sunbeaminfo.com'
    persons[1][2] = '+913453345'

    # for person in persons:
    #     print('name = {}'.format(person[0]))
    #     print('email = {}'.format(person[1]))
    #     print('phone = {}'.format(person[2]))

    # for (name, email, phone) in persons:
    #     print('name: {}'.format(name))
    #     print('email: {}'.format(email))
    #     print('phone: {}'.format(phone))

# function6()

def function7():
    person = {
        'name': 'sundar pichchai',
        'email': 'sundar1@google.com, sundar2@google.com',
        'phone': '+134672',
        'company': ''
    }
    print(person)

function7()
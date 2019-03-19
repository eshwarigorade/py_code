def outer():
    print('inside outer')

    # local variable outer
    num1 = 100
    print('before inner() num1: {}'.format(num1))

    def inner():
        print('inside inner')
        nonlocal num1
        print('before modifying num1: {}'.format(num1))
        # local num1
        num1 = 200
        print('after modifying num1: {}'.format(num1))

    inner()
    print('after inner() num1: {}'.format(num1))

outer()

def divide1(p1, p2):
    try:
        result = p1 / p2
        print('result: {}'.format(result))
    except:
        print('exception occurred')
        try:
            raise ZeroDivisionError()
        except:
            print('exception handled again')
            raise ZeroDivisionError()

# try:
#     divide1(10, 0)
# except:
#     print('exception handled again in main')


def divide2(p1, p2):
    try:
        result = p1 / p2
        print('result: {}'.format(result))
    except ZeroDivisionError:
        print('zero division error')
    except: # generic except block
        print('exception occurred')
    else:
        print('no exception occurred')
    finally:
        print('file closed')

divide2(10, 10)
divide2(10, 0)
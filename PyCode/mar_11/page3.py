import matplotlib.pyplot as plt

categories = ['gadgets', 'fuel', 'clothing', 'education', 'cosmetics']
values = [10, 5, 2, 8, 1]

def function1():
    plt.title('Expenses')
    plt.pie(values, labels=categories, autopct='%0.2f%%', explode=[0, 0.1, 0, 0, 0])
    plt.savefig('/tmp/pie1.png')
    plt.show()

function1()

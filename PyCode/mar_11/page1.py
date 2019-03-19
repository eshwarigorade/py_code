import matplotlib.pyplot as plt

days = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
temperatures = [30, 35, 32, 28, 27, 30, 26, 29, 30, 25]
avgTemperatures = [28, 30, 31, 27, 25, 28, 29, 30, 20, 24]

def function1():
    plt.title('Weather')
    plt.xlabel('Days')
    plt.ylabel('Temperatures')
    plt.plot(days, temperatures)
    plt.show()

# function1()

def function2():
    plt.title('Weather')
    plt.xlabel('Days')
    plt.ylabel('Temperatures')
    plt.plot(days, temperatures, color='brown', linestyle=':', marker="*", markersize=10)
    plt.show()

# function2()


def function3():
    plt.title('Weather')
    plt.xlabel('Days')
    plt.ylabel('Temperatures')
    plt.plot(days, temperatures, label='Temperature at 8', color='red')
    # plt.plot(days, avgTemperatures, color='green', label='Avg Temperature')
    plt.plot(days, avgTemperatures, '-.D', label='Avg Temperature')
    plt.legend(loc='best', shadow=True)
    plt.grid()
    plt.show()


# function3()

def function4():
    plt.title('Weather')
    plt.xlabel('Days')
    plt.ylabel('Temperatures')
    plt.bar(days, temperatures, label='Temerature')
    plt.legend()
    plt.show()

# function4()

















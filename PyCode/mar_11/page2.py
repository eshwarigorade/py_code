import matplotlib.pyplot as plt
import numpy as np

companies = ['Apple', 'Google', 'Microsoft', 'Amazon', 'Oracle', 'Intel']
revenues = [815, 796, 847, 796, 300, 350]
profits = [300, 150, 350, 180, 90, 85]

def function1():
    plt.title('Company Revenues')
    plt.xlabel('Companies')
    plt.ylabel('Share Price')
    plt.plot(companies, revenues, 'D--')
    plt.show()

# function1()

def function2():
    plt.title('Company Revenues')
    plt.xlabel('Companies')
    plt.ylabel('Share Price')
    xPositions = np.arange(len(companies))
    # xPositions = list(range(len(companies)))
    # print(xPositions + 0.2)
    plt.xticks(xPositions, companies)
    plt.bar(xPositions - 0.2, revenues, width=0.4, label='Revenue')
    plt.bar(xPositions + 0.2, profits, width=0.4, label='Profit')
    plt.legend()
    # plt.grid()
    plt.savefig('/tmp/bars.png')
    plt.show()

function2()


def function3():
    plt.title('Company Revenues')
    plt.xlabel('Companies')
    plt.ylabel('Share Price')
    xPositions = np.arange(len(companies))
    # xPositions = list(range(len(companies)))
    # print(xPositions + 0.2)
    plt.yticks(xPositions, companies)
    plt.barh(xPositions, revenues, label='Revenue')
    plt.barh(xPositions, profits, label='Profit')
    plt.legend()
    # plt.grid()
    plt.show()

# function3()







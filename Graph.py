import matplotlib.pyplot as plt
n = input("Give me a number: ")

def collatz(number):

    if number % 2 == 0:
        return number // 2

    elif number % 2 == 1:
        result = 3 * number + 1
        return result

i = 1
while n != 1:
    n = collatz(int(n))
    plt.scatter(i, n)
    i+=1
plt.title("Collatz Conjecture")
plt.show()

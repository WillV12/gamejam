import matplotlib.pyplot as plt


def graph(respect_list, day_list):
    plt.plot(day_list, respect_list, color="red")
    plt.ylabel("Respect level (%)")
    plt.xlabel("Day")
    plt.ylim(0 , 100)
    plt.title("Respect level")
    plt.show()

graph([50, 66, 72, 45, 50], [1,2,3,4,5])
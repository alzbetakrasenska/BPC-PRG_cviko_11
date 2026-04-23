import random
import matplotlib.pyplot as plt

def random_numbers(count, low=0, high=100):
    return [random.randint(low, high) for _ in range(count)]




if __name__ == "__main__":
    nums = random_numbers(10)
    print(nums)


def selection_sort(nums):
    num_copy = nums.copy()
    for i in range(len(num_copy)):
        min = i
        for j in range(i+1, len(num_copy)):
            if num_copy[j] < num_copy[min]:
                min = j
        num_copy[min], num_copy[i] = num_copy[i], num_copy[min]
    return num_copy

plt.ion()
plt.show()
def bubble_sort(nums):
    num_copy = nums.copy()
    sorted = 0
    while sorted <= len(num_copy):
        for i in range(1, len(num_copy)):
            if num_copy[i-1] > num_copy[i]:
                num_copy[i-1], num_copy[i] = num_copy[i], num_copy[i-1]
            index_highlight1 = i - 1
            index_highlight2 = i
            colors = ["steelblue"] * len(num_copy)
            colors[index_highlight1] = "tomato"
            colors[index_highlight2] = "tomato"
            plt.clf()
            plt.bar(range(len(num_copy)), num_copy, color=colors)
            plt.title("Bubble Sort")
            plt.pause(0.1)

        sorted += 1
    plt.ioff()
    plt.show()
    return num_copy

print(bubble_sort(nums))
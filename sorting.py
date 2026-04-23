import random

def random_numbers(count, low=0, high=100):
    return [random.randint(low, high) for _ in range(count)]




if __name__ == "__main__":
    nums = random_numbers(10)
    print(nums)



def selection_sort(nums):
    for i in range(len(nums)):
        min = i
        for j in range(i+1, len(nums)):
            if nums[j] < nums[min]:
                min = j
        nums[min], nums[i] = nums[i], nums[min]
    return nums

print(selection_sort(nums))


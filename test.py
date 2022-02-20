
def square_numbers(nums):
    return list(map(lambda x: x**4, nums))

if __name__ == "__main__":
    print(square_numbers([1,2,3,4,5]))
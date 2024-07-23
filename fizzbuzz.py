# add your code here
def fizzbuzz_if_else(n):
    nums = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            nums.append("FizzBuzz")
        elif i % 3 == 0:
            nums.append("Fizz")
        elif i % 5 == 0:
            nums.append("Buzz")
        else:
            nums.append(i)
    return "\n".join(map(str, nums))
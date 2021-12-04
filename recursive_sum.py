def sum(numbers):
    if not numbers:
        return 0
    remaining_sum = sum(numbers[1:])
    return numbers[0] + remaining_sum

numbers = [2,1,55,3,6,15,23,9]
print(sum(numbers))
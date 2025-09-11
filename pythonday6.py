def make_list():
    nth_number = int(input("Till what end do i need to create numbers? "))
    numbers = []
    i = 0
    while i < nth_number + 1:
        numbers.append(i)
        i += 1
    return numbers
def print_list(numbers):
    for num in numbers:
        print(num)


nums = make_list()
print_list(nums)
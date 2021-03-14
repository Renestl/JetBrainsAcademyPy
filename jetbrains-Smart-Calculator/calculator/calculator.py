# write your code here
class Calculator:

    def addition(num_a, num_b):
        print(int(num_a) + int(num_b))

    while True:
        nums = input()
        input_len = len(nums.split())

        if nums == '/exit':
            print('Bye!')
            quit()
        elif input_len == 0:
            pass
        elif input_len == 1:
            print(int(nums))
        elif input_len == 2:
            a, b = nums.split(" ")
            addition(a, b)


if __name__ == '__main__':
    calculator = Calculator()

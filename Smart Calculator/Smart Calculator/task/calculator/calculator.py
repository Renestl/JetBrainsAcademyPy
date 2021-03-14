# write your code here
class Calculator:
    def __init__(self):
        self.nums = None
        self.viable = None
        self.help = 'This program calculates the sum of numbers\n' \
                    '"/exit" will quit the program\n' \
                    '"/help" brings up this text.\n'

    def main(self):
        while True:
            self.viable = True
            self.nums = input()

            if '/' in self.nums:
                if self.nums == '/help':
                    print(self.help)
                    self.viable = False
                    continue
                elif self.nums == '/exit':
                    print('Bye!')
                    quit()
                else:
                    print('Invalid entry')

            if self.nums == '':
                continue

            # Verify that user only enters numbers, not text
            try:
                self.determine_sign()
                # if " " in self.nums and not ("+" in self.nums or '-' in self.nums):
                #     raise ValueError
                #
                # if self.nums.endswith('+') or self.nums.endswith('-'):
                #     raise ValueError
                #
                # while '--' in self.nums or '+' in self.nums:
                #     self.nums = self.nums.replace('--', '')

            except ValueError: ## If text is entered, returns error
                pass
                # print('Please enter numbers only.')
                #     print()
                #     self.viable = False

    def clean_expression(self):
        pass


    def determine_sign(self):
        print(self.nums.split())


if __name__ == '__main__':
    calculator = Calculator()
    calculator.main()

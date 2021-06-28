#Let's create RemainderCheck class to implement tests
class MultiCheck:
    # create method return the remainder as a result of division
    def remainder(self, num1, num2):
        return num1 % num2

    #create a method to calculate the percentage of second number is of the first number
    def percentage(self, num1, num2):
        return (num2 / num1) * 100

    # create a method to return the True if positive integer
    def positivity(self, num1):
        return num1 >= 0
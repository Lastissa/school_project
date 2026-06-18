import math
import time
from calculator import *

for_faster_clipping = lambda number: Utility().clipLenght(Utility().tryFloatToInt(number), 3)
x2_clip = for_faster_clipping(-2)  # String
x_clip = for_faster_clipping(7)    # String
c_clip = for_faster_clipping(-5)   # String

class CustomMth:
    def __init__(self, *args, **kwargs):
        self.divisors_purpose = "For getting all the possible numbers that can divide a number e.g dvisor of 4 is [1,2,4]"
        self.quad_factorization_equ_prod_sum_purpose = "return and/or print the possible two nmbers that can be the product and sum of a quadratic expressiom e.g prod of x,y = 2 and sum = 3, x,y = [2,1]"
      
    def divisors(self, number: int, only_positive_number=False, display=True):
        divisors = []
        for i in range(1, number + 1):
            if number % i == 0:
                # Check repeat
                if number % i not in divisors:
                    divisors.append(i)  # +ve value
                    if only_positive_number == False:
                        divisors.append(i * -1)  # -ve value
        if display == True:
            print(f" all the possbile values are: {divisors}-\thint: set display as false to stop the default printing")
        return divisors
        
    def quad_factorization_equ_prod_sum(self, x2_coef, x_coef, c_coef, all_possible_values=False):
        # check if the product is decimal
        product = float(x2_coef) * float(c_coef)
        is_decimal = product != int(product)
      
        # its a decimal, terminate
        if is_decimal:
            return TypeError("only integer are allowed")
      
        product_abs = abs(int(product))
        divisors = self.divisors(product_abs, display=False)
        two_number_whoose_prod_and_sum_matters = []  # [x, y]
        all_possible_products = []
        
        for i in divisors:
            for j in divisors:
                to_add = [i, j]
                to_add.sort()
                if to_add not in all_possible_products:
                    all_possible_products.append(to_add)
                
                    # check if to_add values sum and add match with the product and x_coeficient
                    multiply_works = to_add[0] * to_add[1] == product
                    sum_works = to_add[0] + to_add[1] == float(x_coef) 
                    
                    if multiply_works == True and sum_works == True:
                        two_number_whoose_prod_and_sum_matters = to_add
                    
        if all_possible_values == True:
            all_possible_products.sort()
            for i in all_possible_products:
                print(i)
            return all_possible_products
        
        return two_number_whoose_prod_and_sum_matters  # a list

    def quad_factorization_method_solution(self, x2, x, c):
        middle_coeficents = self.quad_factorization_equ_prod_sum(x2, x, c)
        
        # if anything is wrong with this list, just raise some error
        if type(middle_coeficents) != type([]) or len(middle_coeficents) != 2: print("No possible values exist, try other method")
        else:
            mid_coef_1 = middle_coeficents[0]
            mid_coef_2 = middle_coeficents[1]
            
            mid_coef_1_symbol = "-" if mid_coef_1 < 0 else "+"
            mid_coef_1_value = abs(mid_coef_1)
            
            mid_coef_2_symbol = "-" if mid_coef_2 < 0 else "+"
            mid_coef_2_value = abs(mid_coef_2)
            
            x2_symbol = "-" if float(x2) < 0 else "+"
            x2_value = Utility().tryFloatToInt(abs(float(x2)))
            
            x_symbol = "-" if float(x) < 0 else "+"
            x_value = Utility().tryFloatToInt(abs(float(x)))
            
            c_symbol = "-" if float(c) < 0 else "+"
            c_value = Utility().tryFloatToInt(abs(float(c)))
            
            result = f"""
    USING MY FAV; FACTORIZATION METHOD.

    {x2}x² {x_symbol}{x_value}x {c_symbol}{c_value} 
    product of two number = x² coef * c coef = {int(float(x2) * float(c))}
    sum of same two num = x coef = {x}
    best fit two numbers = {mid_coef_1} & {mid_coef_2}
    replace {x}x with {mid_coef_1}x {mid_coef_2_symbol} {mid_coef_2_value}x
    => {x2}x² {mid_coef_1_symbol} {mid_coef_1_value}x {mid_coef_2_symbol} {mid_coef_2_value}x {c_symbol}{c_value}
    From here , group it and factorize it.
            """
            return result
            # testing_output = [Utility().tryFloatToInt(x2), mid_coef_1_value, mid_coef_2_value, c_value]
            # print(testing_output)

print(CustomMth().quad_factorization_method_solution(x2_clip, x_clip,c_clip))
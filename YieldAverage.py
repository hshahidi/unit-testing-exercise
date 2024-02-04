def wafer_yield_sum(list):
    total = 0

    for i in list:
        if i is None or isinstance(i, str):
            continue
        else:
            if i > 100:
                raise ValueError("Error: Values out of range. Please enter wafer yield as a decimal between 0 and 1.")
                break
            elif i < 0:
                raise ValueError("Error: Values out of range. Please enter wafer yield as a decimal between 0 and 1.")
                break
            else:
                #converting percents into their decimal equivalents
                if i > 1:
                    i = i / 100
                    total += i
                else:
                    total += i 
                    
    return round(total, 4)          
    

def wafer_yield_count(list):
    #return count
    pass


def divide(numerator, denominator):
    return numerator/denominator


def lot_yield_average(list):
    return divide(wafer_yield_sum(list), wafer_yield_count(list))
 




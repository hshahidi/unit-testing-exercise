def wafer_yield_sum(list):
    total = 0
    for i in list:
        total += i
    return total

  
def wafer_yield_count(list):
    count = 0
    for i in list:
        count += 1
    return count


def lot_yield_average(list):
    average_list = wafer_yield_sum(list) / wafer_yield_count(list)
    return average_list




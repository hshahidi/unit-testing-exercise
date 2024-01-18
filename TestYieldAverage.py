import pytest
import YieldAverage
from YieldAverage import lot_yield_average


"""
Wafer Lot 1:
Expected result should round down to four decimal places.
Wafer lot contains decimals that are four decimal places in length.
"""
wafer_lot_1 = [0.9234, 0.8678, 0.8456, 0.9876, 0.7321, 0.8789, 0.8432, 0.8765, 0.1098, 0.9765,
0.7321, 0.5345, 0.5678, 0.8765, 0.9876, 0.9456, 0.7890, 0.7987, 0.6543, 0.6123,
0.8765, 0.9456, 0.7890, 0.7567, 0.8901]
def test_lot_avg_1():
    expected_result = lot_yield_average(wafer_lot_1)
    assert expected_result == 0.5559

"""
Wafer Lot 2:
Expected result should round up to four decimal places.
Wafer lot contains decimals that are five decimal places in length.
"""
#Expected result should round up to four decimal places
wafer_lot_2 = [0.92346, 0.86784, 0.84568, 0.98764, 0.73213, 0.87893, 0.84329, 0.87653, 0.1098, 0.97654,
0.73212, 0.53453, 0.56786, 0.87654, 0.98765, 0.94567, 0.78905, 0.79878, 0.65437, 0.61233,
0.87655, 0.94563, 0.78904, 0.75673, 0.89012]
def test_lot_avg_2():
    expected_result = lot_yield_average(wafer_lot_2)
    assert expected_result == 0.7920

"""
Wafer Lot 3:
Expected result should round up to four decimal places.
Wafer lot contains varying lengths of decimals, valid input is between 0 and 1 inclusive.
"""
wafer_lot_3 = [0.34, 0.5678, 0.3456, 0.987, 0.4321, 0.6789, 0.5432, 0.876, 0.1098, 0.8765,
0.41, 0.2345, 0.5678, 0.8765, 1, 0.6, 0.70, 0.0987, 0.6543, 0.0123,
0.870, 0, 0.7890, 0.4500, 0.8901]
def test_lot_avg_3():
    expected_result = lot_yield_average(wafer_lot_3)
    assert expected_result == 0.5564

"""
Wafer Lot 4:
Expected result should average all valid inputs and ignore blank wafer inputs.
Wafer lot contains decimals between 0 and 1 inclusive and blank wafer inputs.
"""
wafer_lot_4 = [0.1234, 0.5678, 0.3456, 0.9876, 0.4321, None, 0.5432, 0.0002, 0.1098, 0.125,
0.4321, None, 0.5678, 0.365, None, None, 0.2386, 0.156, 0.6543, 0.0123,
0.3356, 0.3456, 0.219, 0.4567, 0.1898]
def test_lot_avg_4():
    expected_result = lot_yield_average(wafer_lot_4)
    assert expected_result == 0.3432


"""
Wafer Lot 5:
Expected result shoud average all valid inputs.
Wafer lot contains less than 25 inputs.
"""
wafer_lot_5 = [0.1234, 0.5678, 0.3456, 0.9876, 0.4321, 0.6789, 0.5432, 0.8765, 0.1098, 0.8765,
0.4321, 0.2345, 0.5678, 0.8765, 0.9876, 0.3456]
def test_lot_avg_5():
    expected_result = lot_yield_average(wafer_lot_5)
    assert expected_result == 0.5616


"""
Wafer Lot 6:
Expected result should throw error for exceeding lot limit.
Wafer lot contains more than 25 inputs.
"""
wafer_lot_6 = [0.1234, 0.5678, 0.3456, 0.9876, 0.4321, 0.6789, 0.5432, 0.8765, 0.1098, 0.8765,
0.4321, 0.2345, 0.5678, 0.8765, 0.9876, 0.3456, 0.7890, 0.0987, 0.6543, 0.0123,
0.8765, 0.3456, 0.7890, 0.4567, 0.8901, 0.2345, 0.5678, 0.8765, 0.9876, 0.3456]
def test_lot_avg_6():
    expected_result = lot_yield_average(wafer_lot_6)
    assert expected_result == "Error: Lot exceeds limit of 25 wafers."


"""
Wafer Lot 7:
Expected result should average all original and converted inputs. 
Wafer lot contains some percent inputs, convert these percents into their decimal equivalent.
"""
wafer_lot_7 = [37.2, 12, 64.38, 18, 53, .777, 29, 42, 91, 10, 5, 68.01, 83, 25.312, 49, 36, 20, 1.5678, 57, 71, 13, 97, 45, 60, 14]
def test_lot_avg_7():
    expected_result = lot_yield_average(wafer_lot_7)
    assert expected_result == 0.4317


"""
Wafer Lot 8:
Expected result should average all the inputs that are in decimal format.
Wafer lot contains some input strings that should be ignored.
"""
wafer_lot_8 = [0.9234, 0.8678, 0.8456, 0.9876, 0.7321, 0.8789, 0.8432, 0.8765, 0.1098, 0.9765,
0.7321, 0.5345, 0.5678, 0.8765, "0.9876", 0.9456, 0.7890, 0.7987, 0.6543, 0.6123,
0.8765, "0.9456", "0.7890", 0.7567, 0.8901]
def test_lot_avg_8():
    expected_result = lot_yield_average(wafer_lot_8)
    assert expected_result == 0.7762

"""
Wafer Lot 9:
Expected result should throw an error statement.
Wafer lot contains out of range inputs.
"""
wafer_lot_9 = [-1.2345, 2.5678, -0.7890, 3.4567, 0.1234, 4.5678, 5.4321, 6.7890, 7.8901, 8.7654, 9.0123, 
10.1112, 11.1314, 12.1516, 13.1618, 14.1719, 15.1820, 16.1921, 17.2022, 18.2123, 19.2224, 20.2325, 21.2426, 22.2527]
def test_lot_avg_9():
    expected_result = lot_yield_average(wafer_lot_9)
    assert expected_result == "Error: Values out of range. Please enter wafer yield as a decimal between 0 and 1."


"""
Wafer Lot 10:
Expected result should throw error statement.
Wafer lot contains inputs greater than 100.
"""
wafer_lot_10 = [112.45, 117.89, 124.00, 130, 145.11, 150, 162, 175, 180, 192, 205, 210,
225, 230, 242, 256, 267, 275, 280, 298, 305, 312, 327.34, 335, 349.45]
def test_lot_avg_10():
    expected_result = lot_yield_average(wafer_lot_10)
    assert expected_result == "Error: Values out of range. Please enter wafer yield as a decimal between 0 and 1."

"""
Wafer Lot 11:
Expected result should throw error statement.
Wafer lot contains inputs that are less than 0. 
"""
wafer_lot_11 = [-0.9234, -0.8678, -0.8456, -0.9876, -0.7321, -0.8789, -0.8432, -0.8765, -0.1098, -0.9765,
-0.7321, -0.5345, -0.5678, -0.8765, -0.9876, -0.9456, -0.7890, -0.7987, -0.6543, -0.6123,
-0.8765, -0.9456, -0.7890, -0.7567, -0.8901]
def test_lot_avg_11():
    expected_result = lot_yield_average(wafer_lot_11)
    assert expected_result == "Error: Values out of range. Please enter wafer yield as a decimal between 0 and 1."
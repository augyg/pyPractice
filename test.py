

price_per_unit = 3.5

units = 16

total_cost_to_be_billed = units * price_per_unit
print(total_cost_to_be_billed)
copy = total_cost_to_be_billed

#sums to units 
usage = [2, 8, 4, 2]

bills = [] 
for monthUsage in usage:
    # compute bill
      # percentage of total cost

    fractionOfUsageUsed = monthUsage / units
    print('fracUsage', fractionOfUsageUsed)

    bill_this_month = total_cost_to_be_billed * fractionOfUsageUsed
    bills.append(bill_this_month) 
    print('btm', bill_this_month)
    # still need to update state

    units -= monthUsage
    total_cost_to_be_billed -= bill_this_month
    print(units, total_cost_to_be_billed)


print(bills)
print('sum', sum(bills))
print(sum(bills) == copy)
    
    
    





# xs = [1,1,1,1,1,1,1,1,1,2] 

# def computeLengthOfSubset(arr):
#     count = 0 
#     for i in arr:
#         if i == 1:
#             count += 1
#         else:
#             break 

#     return count


#     # len(xs) - 1 == computeLengthOfSubset(xs)


# print(len(xs) - 1)
# print(computeLengthOfSubset(xs) == len(xs) - 1)

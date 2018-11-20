# Unpacking variables into separated variables
date, name, price = ["September 1", "LED light", 149.99]
print(name)
print(date)
print(price)

# Avg calculator
def drop_first_last(grades):
    # *middle = everything in middle      (Python 3)
    first, *middle, last = grades
    avg = sum(middle) / len(middle)
    print(avg)

drop_first_last([1,2,3,4,5,6])
drop_first_last([100,222,444,666,777,888,777,444])

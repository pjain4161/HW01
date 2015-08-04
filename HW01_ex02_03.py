# HW01_ex02_03
# NOTE: You do not run this script.
# #
# Practice using the Python interpreter as a calculator:

# 1 The volume of a sphere with radius r is 4/3 pi r3. 
# What is the volume of a sphere with radius 5? (Hint: 392.7 is wrong!)
# volume: 523.5987755982989

# 2. Suppose the cover price of a book is $24.95, but bookstores get a 
# 40% discount. Shipping costs $3 for the first copy and 75 cents for 
# each additional copy. What is the total wholesale cost for 60 copies?
# total wholesale cost:

Discount = .40
price = 24.95
cost_after_discount = price - (Discount* price)
price_first_book = cost_after_discount + 3
price_remaining_books = (cost_after_discount + .75) *59
total = price_first_book + price_remaining_books
print "total price = " + str(total)

# 3. If I leave my house at 6:52 am and run 1 mile at an easy pace 
# (8:15 per mile), then 3 miles at tempo (7:12 per mile) and 1 mile at easy 
# pace again, what time do I get home for breakfast?
# time: 7:30:06

time = 8.25 + (7.2*3) + 8.25
#print "total time in minutes = " + str(time)

print "time to reach = 7:30:6"

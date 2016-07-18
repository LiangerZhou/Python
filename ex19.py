#-*- coding:utf-8 -*-
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheeses!" % cheese_count
	print "You have %d boxes of crackers!" % boxes_of_crackers
	print "Man that's enough for a party!"
	print "Get a blanket.\n"
	

print "We can just give the function numbers directly:"
#调用函数传入数值参数
cheese_and_crackers(20, 30)


print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50
#调用函数，传入参数变量
cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print "We can even do math inside too:"
#调用函数，传入参数（参数由数值相加得到）
cheese_and_crackers(10+20, 5+6)


print "And we can combine the two, variables and math:"
#调用函数，传递参数（参数由变量和数值相加得来）
cheese_and_crackers(amount_of_cheese+10, amount_of_crackers+1000)
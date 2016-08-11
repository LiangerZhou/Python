# -*- encoding:utf-8 -*-
class Parent(object):
	
	def override(self):
		print "PARENT override()"
	# 隐式覆写
	def implicit(self):
		print "PARENT implicit()"
		
	def altered(self):
		print "PARENT altered()"
		
class Child(Parent):
	#显式覆写
	def override(self):
		print "CHILD override()"
		
	def altered(self):
		print "CHILD, BEFORE PARENT altered()"
		super(Child, self).altered()#调用父类方法
		print "CHILD, AFTER PARENT altered()"
		
dad = Parent()
son = Child()

dad.implicit()
son.implicit()

dad.override()
son.override()

dad.altered()
son.altered()
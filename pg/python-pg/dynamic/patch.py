import monk


#Create monkey patch function
def monkey_f(self):
    print('monkey_f() is being called')


#Apply monkey patch function replacing address of "func" with "monkey_f"
monk.A.func = monkey_f
obj = monk.A()

#call function "func" whose address got replaced with function "monkey_f()"
obj.func()

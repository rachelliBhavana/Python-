# A python program to calculate the gross salary and net salary of an employee.

def da(basic):
	'''da is 80 % of basic salary'''
	da = basic * 80/100
	return da

def hra(basic):
    '''hra is 15 % of basic salary'''
    hra = basic * 15/100
    return hra

def pf(basic):
    '''pf is 12 % of basic salary'''
    pf = basic * 12/100
    return pf

def itax(gross):
    '''tax is calculated at 10 % on gross'''
    tax = gross * 0.1
    return tax

basic = float(input("Enter basic salary: "))

gross = basic+da(basic)+hra(basic)
print("your gross salary: {:10.2f}".format(gross))

net = gross - pf(basic)-itax(gross)
print("your net salary: {:10.2f}".format(net))
#!/usr/bin/env python
#  Copyright (c) 2007, Enthought, Inc.
#  License: BSD Style.

'''ex01: practise how to create Traits and create notifications

Follow the instructions in comments to complete this exercise
'''

#--<Imports>--------------------------------------------------------------------

from traits.api import *

#--[Employee Class]-------------------------------------------------------------

'''Task1:
    1. add default value to 'name'('Employee') and 'sick_days' (0)
    2. add a trait 'wages' to Employee class. 
        type: float, default value: 1000.0
    3. create a method 'changeSickDays()', this method will be called when 
        self.sick_days changes and modify the 'wages' by wages = 1000 - 10 * 
        sick_days. And print out the changes
    4. create a notification, using on_trait_change() method, when
        self.sick_days changes, call method changeSickDays()
'''
class Employee ( HasTraits ):

    # FIXME: The name of the employee, add default value by providing 'default'
    # key value, see online doc for syntax
    name = Str

    # FIXME: The number of sick days they have taken this year, add default
    # value by providing 'default' key value, see online doc for syntax
    sick_days = Int
    
    # FIXME: Add definition of wages here
    wages = Float
    
    def __init__(self, **kwargs):
        ''' init employee information
        '''
        super(Employee, self).__init__(**kwargs)
        #FIXME: add self.on_trait_change() here, see online doc for syntax
        
        return
    
    def changeSickDays(self, new):
        '''change self.sick_days to sick_days
        new is the new value of the trait
        '''
        #FIXME: your code
        
        return
    

#--[Department Class]-----------------------------------------------------------

'''Task2:
    1. add default value to 'name'('Department') and 'employees' ([])
    2. create a method 'addEmployee(name)', when call this method, add a 
        employee (Employee instance) to employees list with its name equal 
        to 'name'.
    3. create a notification, using _traitname_changed(), when self.employees 
        changed, print out the changes
    4. create a notification, using using on_trait_change() method, when
        self.employees changed, print out the chagnes
'''
class Department ( HasTraits ):

    # FIXME: add default value, The name of the department:
    name = Str

    # FIXME: add default value, The employees in the department:
    employees = List( Employee )
    
    def __init__(self, **kwargs):
        ''' init employee information
        '''
        super(Department, self).__init__(**kwargs)
        #FIXME: add self.on_trait_change() here, see online doc for syntax
        self.on_trait_change(self.employeesListChange, 'employees_items')
        return
    
    def addEmployee(self, name):
        '''add a employee to self.employees, employee's name is 'name'
        '''
        #FIXME: your code
        return
    
    #FIXME: change traitname to name of trait you want to create notification on.
    def _traitname_changed(self):
        '''print out new employees
        '''
        #FIXME: change
        
        return
    
    # FIXME: this method will be called differently compare to 
    # self._employees_changed(), so add different print out message
    def employeesListChange(self):
        '''print out different messages
        '''
        return
    
    '''
    3 and 4 are different. using _employees_changed, method will be called when
    the list is replaced (or new list assigned to this trait), using
    on_trait_change() and add '_items' to the name of list, method will be
    called when the items in list is changed (for example, append new item to
    the list)
    '''

#--[Corporation Class]----------------------------------------------------------

'''Task3:
    1. add default value to 'name'('Corporation') and 'departments' ([])
    2. create a notification, using @on_trait_change('extended_trait_name') 
        decorator, when self.name changed, call this method and print the new 
        name
'''
class Corporation ( HasTraits ):

    # FIXME: add default value, The name of the corporation:
    name = Str

    # FIXME: add default value, The departments within the corporation:
    departments = List( Department )
    
    # FIXME: chagne extended_trait_name to name of trait
    @on_trait_change('extended_trait_name')
    def anyMethodName(self):
        '''print new name of corporation
        '''
        #FIXME: your code
        return

#--[Example*]-------------------------------------------------------------------

# Create some sample employees:
millie   = Employee( name = 'Millie',   sick_days = 2 )
ralph    = Employee( name = 'Ralph',    sick_days = 3 )
tom      = Employee( name = 'Tom',      sick_days = 1 )
slick    = Employee( name = 'Slick',    sick_days = 16 )
marcelle = Employee( name = 'Marcelle', sick_days = 7 )
reggie   = Employee( name = 'Reggie',   sick_days = 11 )
dave     = Employee( name = 'Dave',     sick_days = 0 )
bob      = Employee( name = 'Bob',      sick_days = 1 )
alphonse = Employee( name = 'Alphonse', sick_days = 5 )

# Create some sample departments:
print '''
create departments, your program should print out the changes of employees as 
you assign new list to department.employees
'''

accounting = Department( name      = 'accounting',
                         employees = [ millie, ralph, tom ] )

sales = Department( name      = 'Sales',
                    employees = [ slick, marcelle, reggie ] )

development = Department( name      = 'Development',
                          employees = [ dave, bob, alphonse ] )

# Create a sample corporation:
acme = Corporation( name        = 'Acme, Inc.',
                    departments = [ accounting, sales, development ] )

# Now let's try it out:
print '''change sick_days of employee, your program should print out the changes
'''
slick.sick_days  += 1
reggie.sick_days += 1

print '''append a new employee to sales.employees, employeesListChange() should
be called here
'''
sales.addEmployee('new employee')

print '''assign an empty list to sales, _employees_changed() should be called here
'''
sales.employees = []
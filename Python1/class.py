class Parent: # define parent class
   
   def __init__(self):
      print "Calling parent constructor"

   def parentMethod(self):
      if m.maleMethod:
          print 'Male'
      else:
          print 'Female'

class Male(Parent): # define child class
   def __init__(self):
      print "Calling Male constructor"

   def maleMethod(self):
      print 'Calling male method'
class Female(Parent):
    def __init__(self):
        print "Calling Female Constructor"

    def femaleMethod(self):
        print 'Calling Female method'

m = Male() # instance of child
m.maleMethod() # child calls its method
m.parentMethod() # calls parent's method


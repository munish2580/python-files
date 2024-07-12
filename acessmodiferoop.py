# # public modifer
# class abc:
#     def _init_(self):
#         self.public_attribute=None  #this ids public attributes


#     def public_function(): #this is a public function
#         pass



# obj1=abc()
# obj1.public_attribute
# obj1.public_function()       

# private modifier
class abc:
    def _init_(self):
        self._private_attributes

    def _private_attributes():
        pass



obj=abc()
print(obj._private_function())        

# protected modifier
class abc:
    def _init_(self):
        self._protected_attributes=10

    def _protected_function():
        pass

class student:
    def set_name(self,name):
        self.name=name

    def get_name(self):
        return self.name
    
student1=student()
student1.set_name("shivam")
print(student1.get_name())    

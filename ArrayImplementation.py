#Create an Array class as list
class MyArray:
    def __init__(self,data):
        self.length=0
        self.data=data
        self.items=list()
        self.items.append(data)
        if len(self.items) > self.length:
            self.length+=1


    def get(self,index):
        return self.items[index]

    #Add a push function to insert element at the end of array

    def push(self,value):
        self.items.append(value)
        self.length+=1
        return self.items

    # Add a pop function to remove elements from the end of Array

    def pop(self):
        del self.items[-1]
        self.length-=1

    # Add a function to delete an element t a specific index in the array    

    def deleteatIndex(self,index):
        del self.items[index]
        self.length-=1
        #self.unshift(index)
        return self.items

    
        
my_array = MyArray(1)
my_array.push(2)
my_array.push(3)
my_array.push(4)
print(my_array.items)
my_array.pop()
print(my_array.items)
my_array.deleteatIndex(1)
print(my_array.items)
print(my_array.length)

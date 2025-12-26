class even:
    def __init__(self):
        self.st=int(input("Enter start range:"))
        self.en=int(input("Enter ending range:"))
        self.step=int(input("Enter ending range:"))

    def __iter__(self):
        self.i=self.st
        return self

    def __next__(self):
        if self.step>0:
            if self.i<self.en:
                res=self.i
                self.i+=self.step
                return res            
            raise StopIteration

        else:
            if self.i>self.en:
                res=self.i
                self.i+=self.step
                return res            
        raise StopIteration
obj=even()
print(list(obj))

#zip function
print()
print("ZIP FUNCTION")
for i,j,k,l in zip('abc',[1,2,3],'xyz','pqr'):
    print(i,j,k,l)
print()
for i,j in 'ab',[1,2]:
    print(i,j)


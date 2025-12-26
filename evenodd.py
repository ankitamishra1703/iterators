class even:
    def __init__(self):
        self.st=int(input("Enter start range:"))
        self.en=int(input("Enter ending range:"))

    def __iter__(self):
        self.i=self.st
        return self

    def __next__(self):
        if self.i<self.en:
            res=self.i
            self.i+=1
            if res%2==0:
                res=[res,res*res]
                return res
            else:
                res=[res,res*res*res]
                return res
        raise StopIteration
obj=even()
print(list(obj))

class ranking:
    def __init__(self,name,rank):
        self.name=name
        self.__rank=rank

    def show_rank(self):   #getter
        return self.__rank

    def update_rank(self,rank):  #setter
       self.__rank=rank
       return self.__rank
    
yashu=ranking("yashu",25000)
print(yashu.name)
print(yashu.show_rank())
yashu.update_rank(24500)
print("Updated rank : ",yashu.show_rank())
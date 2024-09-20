#Book class
class Book:
    def __init__(self,id,title,price,copies) -> None:
        self.id = id
        self.title = title
        self.price = price
        self.copies = copies
    def __str__(self) -> str:
        return f'[id={self.id},name={self.title},price={self.price},copies={self.copies}]'
    def __repr__(self) -> str:
        return self.__str__
    

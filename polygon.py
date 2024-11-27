

class Polygon:
    """We use the special method __init__ to initialize values in the class"""
    def __init__(self,nameP,sidesP):
        self.name=nameP
        self.sides=sidesP
        
    """This is the getter/accessor function for self.name"""
    def get_name(self):
        return self.name
    
    """This is the setter/mutator function for self.name"""
    def set_name(self,new):
        self.name=new
        
    """This is the getter/accessor function for self.sides"""
    def get_sides(self):
        return self.sides
    
    """This is the setter/mutator function for self.sides"""
    def set_sides(self,new):
        self.sides=new

        
    """Checking for equality using special method __eq__"""
    def __eq__(self,other):
        if type(self)==type(other):
            return self.name==other.name and self.sides==other.sides
        else:
            return False
        
    """Checking for inequality using special method __ne__"""
    def __ne__(self,other):
        return not self.__eq__(other)
    
    """Returning a string using special method __str__"""
    def __str__(self):
        return f"{self.name} with sides: {self.sides}"
    

    """This function calculates the circumference of the polygon"""
    def calculate_circumference(self):
        sum=0
        for i in range(len(self.sides)):
            sum+=self.sides[i]
        return sum
    
def main():
    """Three instances of the same class is initialized with different values"""
    Triangle=Polygon("Triangle",[3,3,3])
    Square=Polygon("Square",[4,4,4,4])
    Hexagon=Polygon("Hexagon",[2,2,2,2,2,2])
    """Print the list of length of sides of polygon using __str__ special method in class. This is repeated for each instance"""
    print(Triangle)
    """Print the calculated circumference. This is repeated for each instance"""
    print("Calulated circumference:",Triangle.calculate_circumference())
    print(Square)
    print("Calulated circumference:",Square.calculate_circumference())
    print(Hexagon)
    print("Calulated circumference:",Hexagon.calculate_circumference())

if __name__=="__main__":
    main()
    
        

    



import pytest
from polygon import Polygon

def test_polygon_initialization():
    """This function tests the initialization by using getters and setters"""
    test1=Polygon("Triangle",[3,5,3])
    print(test1.get_name())
    print(test1.get_sides())
    test1.set_name("Square")
    test1.set_sides([2,6,3])
    print(test1.get_name())
    print(test1.get_sides())
#test_polygon_initialization()

def test_polygon_equality():
    """This function tests the equality of both attributes initialized in the two instances"""
    poly1=Polygon("Triangle",[3,3,3])
    poly2=Polygon("Triangle",[3,3,3])
    print(poly1==poly2)

#test_polygon_equality()

def test_polygon_inequality():
    """This function tests the inequality of the two attributes initialized in both instances"""
    poly1=Polygon("Square",[3,1,3])
    poly2=Polygon("Triangle",[3,3,3])
    print(poly1!=poly2)

#test_polygon_inequality()

def test_polygon_str():
    """This function prints what is returned from the special method __str__ in the Polygon class"""
    test1=Polygon("Triangle",[4,3,1])
    print(test1)

#test_polygon_str()

def test_calculate_circumference():
    """This function tests if the appropriate circumference is calculated"""
    poly1 = Polygon("Square", [2.1, 6.3, 7])
    assert poly1.calculate_circumference() == pytest.approx(15.4)  

    poly2 = Polygon("Triangle", [3, 4, 5])
    assert poly2.calculate_circumference() == pytest.approx(12.0)

#test_calculate_circumference
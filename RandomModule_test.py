from RandomModule import RandomModule

def test_adder():
    assert RandomModule.adder(1,5) == 6
    assert RandomModule.adder("Hello ", "there!")== "Hello there!"

def test_that_fails():
    assert True
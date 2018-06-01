from RandomModule import RandomModule

def test_adder():
    assert RandomModule.adder(1,5) == 6

def test_that_fails():
    assert False
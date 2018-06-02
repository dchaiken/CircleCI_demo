from RandomModule import RandomModule

def test_adder():
    assert RandomModule.adder(1,5) == 6
    assert RandomModule.adder("Hello ", "there!")== "Hello there!"

def test_that_fails():
    assert True

def test_read_file():
    f = open('/tmp/workspace/testfile.test', 'r')
    assert f.readline() == "I am a file"
    f.close()
if __name__ == "__main__":
    f = open('testfile.test', 'w')
    f.write("I am a file")
    f.close()
    print("wrote to file")
def main():
    fl = open("posData.txt", "r")
    #print(fl.readline())

    for i in range(linesFile("posData.txt")):
        print(i)
        print(fl.readline())
        #print(fl.read(1) + "," + fl.read(1))
        #print("\n")

def linesFile(name):
    i = 0
    f = open(name, "r")
    for line in f:
        i+=1
    return i;
main()

import hashlib
import sys

default_fileName = 'rockyou.txt'
default_message = "a2099f4c2c2de141afb474dfe4b765ce83448100e77f4359314d94807b00862d53316c03963fc60cbdbd7bc6915778f1830f0f4fd9364a4bc71a09c5e83a0a67"

def getFromFile(fileName):
    try:
        with open(fileName, encoding="latin-1") as file:
            return "".join(file.readlines())
    except Exception as e:
        #return "Not able to read file"
        return "Error: {}".format(e) 
    
def findReverseHash(message, fileName):
    try:
        with open(fileName, encoding="latin-1") as file:
            count = 0
            for word in file:
                hashed = hashlib.sha3_512(word.strip().encode()).hexdigest()
                if (message == hashed):
                    return word
                if (count%1000 == 0):
                    print("{}...".format(count))
                count += 1
            return "Result not found in word list."
    except Exception as e:
        return "Error: {}".format(e)

if __name__ == "__main__":
    if (len(sys.argv) == 3):
        message = getFromFile(sys.argv[1])
        fileName = sys.argv[2]
        print(findReverseHash(message, fileName))
    elif (len(sys.argv) == 2):
        message = getFromFile(sys.argv[1])
        print(findReverseHash(message, default_fileName))
    else:
        print(findReverseHash(default_message, default_fileName))

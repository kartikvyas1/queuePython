# queue management system 1.0

class QueueMnt:
    
    primary = []
    secondry = []
    lenOfPrimary = 0
    
    #topQ = 0
    #postopq = 0
    
    #bottomQ = 0
    #posbottomq = 0

    def getLen(self):
        return self.lenOfPrimary

    def decrementLen(self):
        self.lenOfPrimary = self.lenOfPrimary-1

    def incrementLen(self):
        self.lenOfPrimary = self.lenOfPrimary+1

    def popQ(self,primaryList):
        if self.getLen() == 0:
            return False
        self.decrementLen()
        temp = primaryList[0]
        for i in range(self.getLen()):
            primaryList[i] = primaryList[i+1]
        return temp

    def resetQ(self,lenSecondry):
        remainingLen = (self.getLen() - lenSecondry) -1
        for i in range(remainingLen):
            temp = self.popQ(self.primary)
            self.secondry.append(temp)
        self.primary = self.secondry
        self.secondry = []

    def findInQ(self,userA):
        # returns position of element
        flag = 0
        tempPos=0
        for i in range(self.getLen()):
           tempTop = self.popQ(self.primary)
           self.secondry.append(tempTop)
           if userA==tempTop:
               tempPos = i
               flag = 1
               break
        if flag == 0:
            self.primary = self.secondry
            self.secondry = []
            return False
        else:
            self.resetQ(tempPos)
            return tempPos

    def addQ(self,userA, pos=None):
        if pos == None:
            checkif = self.findInQ(userA)
            if checkif != False :
                return checkif
            else:
                self.primary.append(userA)
                self.incrementLen()
                return self.getLen()
        else:
            pos = pos-1
            if pos >= 0:
                for i in range(pos) :
                    temp = self.popQ(self.primary)
                    self.secondry.append(temp)
                self.secondry.append(userA)
                self.resetQ(pos+1)
                self.incrementLen()
                return self.getLen()
            else:
                return 0

    def removeByUser(self,userA):
        checkif = self.findInQ(userA)
        if checkif != False:
            return self.removeByPosition(checkif)
        else:
            return False

    def removeByPosition(self,posA):
        if self.getLen() >= posA:
            posA -=1
            if posA >= 0:
                for i in range(posA) :
                    temp = self.popQ(self.primary)
                    self.secondry.append(temp)
                temp = self.popQ(self.primary)
                self.decrementLen()
                self.resetQ(pos)
                return temp
        else:
            return False

    def moveQ(self,fromA, toB):
        if fromA>0 and toB>0:
            if fromA <= self.getLen() and toB <= self.getLen():
                if FromA == toB: 
                    return True
                else:
                    userAtA = self.removeByPosition(fromA)
                    addQ(userAtA, toB)
                    return True
        else: 
            return False

    # swap users between fromA and toB
    def swapQ(self,fromA, toB):
        if fromA>0 and toB>0:
            if fromA <= self.getLen() and toB <= self.getLen():
                if FromA == toB: 
                    return True
                elif fromA > toB : 
                    userAtA = removeByPosition(formA)
                    userAtB = removeByPosition(toB)

                    self.addQ(userAtA, toB)
                    self.addQ(userAtB, fromA)
                else:
                    userAtB = removeByPosition(toB)
                    userAtA = removeByPosition(formA)

                    self.addQ(userAtB, fromA)
                    self.addQ(userAtA, toB)
                return True
        else:
            return False

    def reverseQ(self):
        initLen = self.getLen()
        for j in range(initLen):
            for i in range(self.getLen()):
                temp = self.popQ(self.primary)
                self.addQ(temp)
            temp = self.popQ(self.primary)
            self.secondry.append(temp)
        self.primary = self.secondry
        self.secondry = []
        self.lenOfPrimary = initLen

    def printQ(self):
        initLen = self.getLen()
        for j in range(initLen):
            temp = self.popQ(self.primary)
            print(temp)
            self.secondry.append(temp)
        self.primary = self.secondry
        self.secondry = []
        self.lenOfPrimary = initLen


def main():

    first = QueueMnt()
    first.addQ(1)
    first.addQ(2)
    print(first.getLen())
    first.printQ()
    first.reverseQ()
    first.printQ()

main()

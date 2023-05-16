#Task 1
class GetFileAdress:

    def __init__(self,adress:str):
        self.adress=adress


    def calculateFreqs(self):
        pass

#Task 2
class ListCount(GetFileAdress):

    #Helpers
    def __fileOpen(self):
        f = open(self.adress,encoding='utf-8')
        return f

    def __getFile__(self):
        return self.__fileOpen()

    # Task 3
    def calculateFreqs(self):
        letterList = list()
        for i in self.__getFile__().read().split():
            for j in i:
                letterList.append(j)

        uniqueLettersInList = set(letterList)

        print("\nUnique Letters in List")
        for i in uniqueLettersInList:
            print(i)

        resultlist=[]
        for unique in uniqueLettersInList:
            count = letterList.count(unique)
            resultlist.append((unique,count))

        print("\nResult List: ")
        for i in resultlist:
            print(i[0],"=",i[1])







#Task 2
class DictCount(GetFileAdress):

    #Helpers
    def __fileOpen(self):
        f = open(self.adress,encoding='utf-8')
        return f

    def __getFile__(self):
        return self.__fileOpen()

    #Task 4
    def calculateFreqs(self):
        letterList = list()
        for i in self.__getFile__().read().split():
            for j in i:
                letterList.append(j)

        uniqueLettersInList = set(letterList)

        uniqueLettersInDict = {}
        for letter in uniqueLettersInList:
            uniqueLettersInDict[letter] = 0

        print("\nInitially Frequencies Of Letters in Dict")
        print(uniqueLettersInDict)

        resultDict={}
        for letter in uniqueLettersInList:
            resultDict[letter] = letterList.count(letter)

        print("\nUpdated Dict: ")
        print(resultDict)





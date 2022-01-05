import json
import csv

class FileOperations:
    def __init__(self, path, fields='', *args, **kwargs):
        self.path = path
        self.fields = fields

    def search(self, keyword): # keyword = fileOps.search(keyword)
        """
        This function for searching on csv file by keyword
        """
        with open(self.path, 'r') as file:
            return [(i+1, r.replace('\n', '')) for i,r in enumerate(file.readlines()[1:]) if keyword.lower() in r.lower()]

    def __deleteByKeyword(self, deleteKey): # fileOps.delete(keyword)
        """
        deletes row by keyword. Can delete multiple rows
        """
        with open(self.path, 'r') as file:
            header = file.readline()
            data = [row for row in file.readlines() if deleteKey.lower() not in row.lower()]
        with open(self.path, 'w') as file:
            file.write(header)
            file.writelines(data)

    def __deleteByIndex(self, deleteKey): # fileOps.delete([5,7,9,10,11,22,2,3,4], by='index')
        """
        deletes row by index. Can delete multiple indexes
        """
        with open(self.path, 'r') as file:
            header = file.readline()
            data = [row for i, row in enumerate(file.readlines()) if i not in deleteKey]
        with open(self.path, 'w') as file:
            file.write(header)
            file.writelines(data)

    def delete(self, deleteKey, by='keyword'):
        """
        used for call deleteBy functions.
        """
        if by == 'keyword':
            self.__deleteByKeyword(deleteKey)
        if by == 'index':
            self.__deleteByIndex(deleteKey)

    def appendRow(self, row = '', delimeter = ','):
        """
        Adding row to csv file
        """
        if row == '':
            with open(self.path, 'r') as file:
                header = file.readline()
                keyList = header.replace('\n', '').split(delimeter)
                row = ''
                for i,key in enumerate(keyList):
                    if i == len(keyList)-1:
                        row += input(f'Enter {key}: ') + '\n'
                    else: row += input(f'Enter {key}: ') + delimeter

        with open(self.path, 'a') as file:
            file.write(row)

    def update(self, oldKeyword, newKeyword):
        """
        Updating csv file by words
        """
        with open(self.path, 'r') as file:
            header = file.readline()
            data = [row.replace(oldKeyword, newKeyword) for row in file.readlines()]
        with open(self.path, 'w') as file:
            file.write(header)
            file.writelines(data)

    def __getKeyword(self, word = ''):
        return input(f'Enter {word}Keyword: ')

    def __getIndexes(self):
        return list(map(int, input('Enter Indexes : ').split())) # 2 3 4 5 

    def showRowJson(self, indexes, delimeter=','):
        """
        Show csv line like Json 
        """
        with open(self.path, 'r') as file:
            header = file.readline()
            keyList = header.replace('\n', '').split(delimeter)
            data = list(csv.reader(file, delimiter=',', quotechar='"'))

            rowList = []
            for index in indexes:
                row = {}
                for i, column in enumerate(data[index]):
                    row[keyList[i]] = column

                rowList.append(row)

            print(json.dumps(rowList, indent=2))

    def mergeCsv(self, newPath):
        """
        Merges main csv with other csv
        """
        with open(self.path, 'a') as file:
            with open(newPath, 'r') as newFile:
                newFile.readline()
                file.writelines([line for line in newFile.readlines()])
                
    def menu(self):
        """
        Terminal menu for file operations
        """
        print(f'Selected CSV: {self.path}')
        print(f'Operations\n(1) Search\n(2) Delete\n(3) Update\n(4) Add Row\n(5) Show Row Like Json\n(6) Merge CSV\n(0) Exit ', end=':')
        selection = int(input())
        if selection == 1:
            for row in self.search(self.__getKeyword()):
                print(row)
        elif selection == 2:
            print(f'By\n(1) Keyword\n(2) Index', end=':')
            by = int(input())
            if by == 1:
                self.__deleteByKeyword(self.__getKeyword())
            elif by == 2:
                self.__deleteByIndex(self.__getIndexes())
        elif selection == 3:
            self.update(self.__getKeyword('Old '), self.__getKeyword('New '))
        elif selection == 4:
            self.appendRow()
        elif selection == 5:
            self.showRowJson(self.__getIndexes())
        elif selection == 6:
            self.mergeCsv(input('Enter path: '))
        elif selection == 0:
            pass

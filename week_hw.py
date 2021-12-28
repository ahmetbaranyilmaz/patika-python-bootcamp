# Bir metnin uzunluğunu hesaplamak için bir Python programı yazınız. ipucu Len fonksiyonu


from typing import no_type_check


def calcLength(text): # Len fonksiyonu
    return len(text)

def calcLengthManuel(text): # Manuel olarak
    counter = 0
    for i in text:
        counter+=1
    return counter

def printLength():
    print(calcLengthManuel('afyonkarahisarlilastiramadiklarimizdanmisiniz'))

# printLength()

###################################################################################################


# Kullanıcı tarafından girilen bir metnin ilk iki ve 
# son iki karakterini ekrana yazdıran Python programını yazınız.

def getText():
    return input('Enter text:')

def getFirstLetters(text, count =2 ):
    return text[: count]

def getLastLetters(text, count = 2):
    return text[len(text) - count: len(text)]


def printLetters():
    text = getText()
    print(f'First 2 letter: {getFirstLetters(text)}')
    print(f'Last 2 letter: {getLastLetters(text)}')

# printLetters()

###################################################################################################

# Kullanıcıdan değişecek metin ve eski harf ve yeni harf bilgisini alarak 
# girilen metin üzerinden değişikliği yapıp sonucu ekrana yazdıran Python programını yazınız.


def replaceText(text, oldLetter, newLetter):
    return text.replace(oldLetter, newLetter)

def showNewText():
    text = getText()
    oldLetter = input('Enter old letter:')
    newLetter = input('Enter new letter')
    print(replaceText(text, oldLetter, newLetter))

# showNewText()

###################################################################################################

def multiReplaceWithDict(): # Birden fazla harfi dict ile alsak nasil olurdu diye dusundum :D
    letterMatchs = {
        'a': 'z',
        'h': 'b',
    }

    text = 'holywooda'

    newText = ''
    for letter in text:
        if letter in letterMatchs.keys():
            newText += letterMatchs[letter]
        else:
            newText += letter

    print(newText)

# multiReplaceWithDict()

# TODO multi replace with substrings

###################################################################################################

# Kullanıcı tarafından girilen bir kelimenin palindrom olup olmadığını 
# karşılaştırma operatöründen faydalanarak print() fonksiyonu ile ekrana yazdırınız. 

def checkPalindrome(text):
    return True if text == text[::-1] else False

def printPalindrome():
    text = getText()

    if checkPalindrome(text):
        print(f'{text} is palindrome')
    else:
        print(f'{text} is not palindrome {text[::-1]}')


# printPalindrome()

###################################################################################################

# Girilen bir metnin son 2 karakterini 4 defa çoğaltarak ekrana yazan Python programını yazınız.
#  `*` aritmetik operatöründen faydalanabilirsiniz.

def multiplyLastLetter():
    text = getText()
    print(getLastLetters(text, 2) * 4)

# multiplyLastLetter()

###################################################################################################

# 5 elemanlı bir liste oluşturunuz. Bu liste içerisindeki 2. elemanı 100 ile değiştiren python kodu yazınız.

def changeListItem():
    myList = [1,2,3,4,5]
    print(*myList)
    myList[1] = 100
    print(*myList)

# changeListItem()

###################################################################################################

def mergeLists():
    list1 = [1,2,3]
    list2 = [4,5,6]

    newList = list1 + list2
    print(newList)

    # Burdan sonraki iki yolu cok begenmedim :(
    # TODO Alttaki yontemler nasil iyi olabilir

    newList = list1.copy()
    newList.extend(list2)

    print(newList)

    newList = list1.copy()

    for e in list2:
        newList.append(e)

    print(newList)

# mergeLists()

###################################################################################################

# Oluşturduğunuz 3 elemanlı bir liste içerisine ilk sıraya "Elma" kelimesini ekleyiniz.

def addItem():
    shoppingList = ['banana', 'pear', 'watermelon']

    shoppingList.insert(0, 'apple')

    print(shoppingList)

# addItem()

###################################################################################################

# listeden ilk 3 sayısını silip ekrana yazdırınız. 

def deleteFirstChar(item = 3):
    liste = [1,2,3,4,5,6,7,1,3,3,3,2,2,1,23]
    print(liste)
    liste.remove(item)

    print(liste)

# deleteFirstChar()

###################################################################################################

# listenin bir kopyasını alarak 250 sayısını listenin sonuna ekleyiniz,
# her iki listeyi ekrana yazdırınız.

def copyAndAddList():
    liste1 = ["1",1,2,"3"]

    list2 = liste1.copy()
    list2.append(250)

    print(f'liste1: {liste1} - liste2: {list2}')

# copyAndAddList()

###################################################################################################

# Aşağıdaki üç farklı sözlüğü tek sözlükte birleştiren python kodunu yazınız

def mergeDicts(dict1, dict2):
    newDict = dict1.copy()
    newDict.update(dict2)

    return newDict

def dictMerger():
    dict1={1:10, 2:20}
    dict2={3:30, 4:40}
    dict3={5:50,6:60}

    newDict = mergeDicts(mergeDicts(dict1, dict2), dict3)

    print(newDict)

    newDict = {**dict1, **dict2, **dict3} # After 3.5

    print(newDict)

# dictMerger()

###################################################################################################

# Sözlükteki en son elemanı silerek ekrana işlem sonucunu yazdırınız

def removeLastFromDict():
    sozluk ={1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

    print(sozluk.popitem())

# removeLastFromDict()

###################################################################################################

# liste=[1,2,3,4,5]
#   a.Yukarıdaki listeden faydalanarak bir sözlük oluşturun 
#   b.sözlüğün her alamanının karşılığına değer olarak anahtarda bulunan sayısal değerin 10 katını eşitleyin.

def createDict():
    liste = [1,2,3,4,5]

    newDict = {i:0 for i in liste}
    print(f'a. {newDict}')

    newDict = {i:i*10 for i in liste}
    print(f'b. {newDict}')

# createDict()

###################################################################################################

# Sözlük içerisine 6 sayısını anahtar olarak değeri 
# 60 olacak şekilde setdefault fonksiyonunu kullanarak ekleyiniz

def addValueWithSetDefault(key = 6, value = 60):
    sozluk={1:10,2:20,3:30,4:40,5:50}

    sozluk.setdefault(key, value)

    print(sozluk)

# addValueWithSetDefault()

###################################################################################################

# Seven Segment Display 

# Ibrahim Hoca gelmeden once :D
def sevenSegment(number = 0): # TODO baska yontem ne olabilir dusun
    numbers = {
        0: '*****\n' + '*   *\n'*5 + '*****',
        1: '    *\n'*6 + '    *',
        2: '*****\n' + '    *\n'*2 + '*****\n' + '*\n'*2 + '*****',
        3: '*****\n' + '    *\n'*2 + '*****\n' + '    *\n'*2 + '*****',
        4: '*   *\n'*3 + '*****\n' + '    *\n'*2 + '    *',
        5: '*****\n' + '*\n'*2 + '*****\n' + '    *\n'*2 + '*****',
        6: '*****\n' + '*\n'*2 + '*****\n' + '*   *\n'*2 + '*****',
        7: '*****\n' + '    *\n'*5 + '    *',
        8: '*****\n*   *\n*   *\n'*2 + '*****',
        9: '*****\n' + '*   *\n'*2 + '*****\n' + '    *\n'*2 + '*****'
    }

    print(numbers[number])

# sevenSegment(5)

# Ibrahim Hoca geldikten sonra :D

import math

column = 3    
row = 5 
sevenSegment=[]
emptyRow = [" "] * column


for i in range(row):
    sevenSegment.append(emptyRow.copy())

def fillA():
    for i in range(row):
        for j in range(column):
            sevenSegment[i][j] = "*"
        break

def fillB():
    for i in range(math.ceil(row/2)):
        for j in range(column):
            if j==column-1:
                sevenSegment[i][j] = "*"

def fillC():
    for i in range(math.floor(row/2),row):
        for j in range(column):
            if j==column-1:
                sevenSegment[i][j] = "*"

def fillD():
    for i in range(row-1,row):
        for j in range(column):
            sevenSegment[i][j] = "*"
        
def fillE():
    for i in range(math.floor(row/2),row):
        for j in range(column):
            if j==0:
                sevenSegment[i][j] = "*"
    
def fillF():
    for i in range(math.ceil(row/2)):
        for j in range(column):
            if j==0:
                sevenSegment[i][j] = "*"

def fillG():
    for i in range(math.floor(row/2),math.floor(row/2)+1):
        for j in range(column):
            sevenSegment[i][j] = "*"


# Yukaridaki kodlar icin Ilhan'a (@ilhanm) tesekkur ederim. :D

funcList = [fillA, fillB, fillC, fillD, fillE, fillF, fillG]

def getNumber():
    number = int(input('enter number:'))

    numberMatch = {
        0: '1111110',
        1: '0110000',
        2: '1101101',
        3: '1111001',
        4: '0110011',
        5: '1011011',
        6: '1011111',
        7: '1110000',
        8: '1111111',
        9: '1111011'
    }

    return numberMatch[number]


def printsevenSegment():

    number = getNumber()

    for index, value in enumerate(number):
        if int(value):
            funcList[index]()

    for i in range(row):
        for j in range(column):
            print(sevenSegment[i][j],end=" ")
            if(j==column-1):
                print("\n")

# printsevenSegment()

###################################################################################################

# Bir listeyi bir sözlükte sıralamak için bir Python programı yazın

def listSorter():
    num = {'n1': [2, 3, 1], 'n2': [5, 1, 2], 'n3': [3, 2, 4]}

    num = {key: sorted(value) for key,value in num.items()}

    print(num)
    
# listSorter()

###################################################################################################


# ilgili sözlükten anahtar kısımlarında bulunan boşlukları temizleyen python kodu yazınız. 

def stripKeys():
    sozluk = {'S  001': ['Math', 'Science'], 'S    002': ['Math', 'English']}

    sozluk = {key.replace(' ', ''): value for key,value in sozluk.items()}

    print(sozluk)

# stripKeys()

###################################################################################################

# liste=[1,2,3,4,5,6] listesindeki 1. elemanı del komutu ile siliniz?

def delValueWithDel():
    liste = [1,2,3,4,5,6]
    print(liste)
    del liste[0]
    print(liste)

# delValueWithDel()

###################################################################################################

# liste=["elma" , "armut", "çilek"] listesine append komutu ile sona 3 elemanını ekleyiniz?

def addThreetoList():
    liste = ['elma', 'armut', 'cilek']
    liste.append(3)
    print(liste)

# addThreetoList()

###################################################################################################

# Girilen on sayı içerisinden en büyük üç sayıyı bulmak için bir Python fonksiyonu yazınız

def getNumbers():
    inputs = input('enter numbers:') # 5 10 20 gibi bosluklu girilebilir
    return list(map(int, inputs.split()))

def findMaxNumbers(count = 3, numbers = [5,2,6,22,9,12,7,10,8,9]):
    return sorted(set(numbers))[:-(count + 1):-1]

def printMaxNumbers():
    print(findMaxNumbers(3))
    # print(findMaxNumbers(3, getNumbers()))


# printMaxNumbers()

###################################################################################################

# Bir metin içerisindeki büyük ve küçük harflerin listesini yazdıran python programını yazınız.

def countUpperLowerLetters():
    text = 'baran YILMAZ'

    counter = {
        'upper': 0,
        'lower': 0
    }

    # TODO Tek satirda nasil yazilabilir??

    for letter in text:
        if letter.islower():
            counter['lower'] += 1
        elif letter.isupper(): 
            counter['upper'] += 1

    print(counter)

# countUpperLowerLetters()

###################################################################################################

# kullanıcıdan alınan 10 sayının çift ve tek sayıların sayısını 
# ekrana yazdıran programı yazınız.

def countOddEven():
    counter = {
        'oddNumbers': [],
        'evenNumbers': []
    }

    for i in range(10):
        number = int(input('enter number:'))

        counter['evenNumbers'].append(number) if number %2 == 0 else counter['oddNumbers'].append(number)

    print(f'Even Numbers {counter["evenNumbers"]} - {len(counter["evenNumbers"])}')

    print(f'Odd Numbers {counter["oddNumbers"]} - {len(counter["oddNumbers"])}')

# countOddEven()

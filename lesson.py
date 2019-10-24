bookList = ['GAME OF THRONES', 'THE HUNGER GAMES', 'HARRY POTTER']


def showMenu():
    print('''
        Please enter following number to choose functions:
        1. Search a book
        2. Add a book to the list
        3. Exit
    ''')
    index = input('请输入\n')
    checkIndex(index)


def checkIndex(index):
    if index == '1':
        searchByName()
    elif index == '2':
        addBook()
    elif index == '3':
        return
    else:
        showMenu()


def searchByName():
    bookName = input('请输入要查找的书名！(输入exit返回上一级)\n')
    while bookName.lower() != 'exit':
        if bookName.upper() in bookList:
            print('You found ' + bookName.upper())
        elif bookName:
            print('No this book')
        bookName = input('请输入要查找的书名！(输入exit返回上一级)\n')
    else:
        print('Exited')
        showMenu()


def addBook():
    bookName = flag = input('请输入要添加的书名！(批量添加用逗号隔开, 输入exit返回上一级)\n')
    if flag.lower() != 'exit':
        books = bookName.split(',')
        nameString = ''
        for item in books:
            nameString += '《' + item + '》'
        flag = input('您要添加的是' + nameString.upper() + '对吗？ Y/N (输入exit返回上一级)\n')
        if flag.lower() == 'y':
            add(books)
            sum = lambda alist: len(alist)
            print('You have ' + str(sum(bookList)) + ' books in the list!')
            addBook()
        elif flag.lower() == 'exit':
            showMenu()
        else:
            addBook()
    else:
        showMenu()


def add(books):
    for book in books:
        bookList.append(book)


showMenu()

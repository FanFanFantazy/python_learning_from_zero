from catch_face import CatchFace
from load_data import load_dataset
from face_train import faceTrainMain
from rec_my_face import recFace
from clear_folder import clearFolder


def showMenu():
    print('''
    Please enter following number to choose a function:
    1. Train your model
    2. Detect your face
    3. Exit
    ''')
    index = input('Please insert:\n')
    checkIndex(index)


def checkIndex(index):
    if index == '1':
        myName = input('Please insert your name:\n')
        print("Preparing for catching a pos image...")
        CatchFace("Catch A Pos Face", 500, './faceData/posFaceData')
        print("Pos model caught!")
        print("Continue?")
        conFlag = input('Y?:\n')
        if conFlag.upper() == 'Y':
            print("Preparing for catching a neg image...")
            CatchFace("Catch A Neg Face", 500, './faceData/negFaceData')
            print("Neg model caught!")
            print("Image loading, please wait...")
            load_dataset("./faceData")
            print("Data loaded!")
            print("Model crafting, please wait...")
            faceTrainMain(myName)
            clearFolder('./faceData/posFaceData')
            clearFolder('./faceData/negFaceData')
            print("Model Crafted!")
            showMenu()
        else:
            showMenu()
    elif index == '2':
        try:
            recFace()
        finally:
            showMenu()
    elif index == '3':
        print('Thank you for using!')
        exit()
    else:
        showMenu()


if __name__ == '__main__':
    showMenu()

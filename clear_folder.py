import os


def clearFolder(folderPath):
    for i in os.listdir(folderPath):
        path_file = os.path.join(folderPath, i)
        if os.path.isfile(path_file):
            os.remove(path_file)
        else:
            for f in os.listdir(path_file):
                path_file2 = os.path.join(path_file, f)
                if os.path.isfile(path_file2):
                    os.remove(path_file2)
    print("Folder has been cleared")


if __name__ == '__main__':
    clearFolder('./faceData/posFaceData')

import os, sys
import shutil

PATH = os.path.join('D:\\', 'Prenosi')

slovar = {"dokumenti":(".docx", ".pdf", ".epub", ".xlsx"), "slike":(".jpg", ".png", ".svg", ".ai"), "zip":(".zip", ".rar"), "video":(".mp4", ".avi")}


def premakni_datoteke(path_mape, slovar):

    """presortira datoteke glede napodno lokacijo in slovar"""
    
    datoteke = os.listdir(path_mape)
    #print(datoteke)

    for i in slovar:
        path_dir = os.path.join(path_mape, i)
        os.mkdir(path_dir)

    path_ostale = os.path.join(path_mape, "ostale_mape")
    os.mkdir(path_ostale)


    path_razno = os.path.join(path_mape, "razno")
    os.mkdir(path_razno)

    for datoteka in datoteke:
        path_dir = os.path.join(path_mape, datoteka)
        if os.path.isdir(path_dir):
            shutil.move(path_dir, path_ostale)
        elif datoteka.lower().endswith((".igs")):
            os.remove(path_dir)
        else:
            for mapa, koncnice in slovar.items():
                new_path_dir = os.path.join(path_mape, mapa, datoteka)
                if datoteka.lower().endswith(koncnice):
                    shutil.move(path_dir, new_path_dir)
                    print(datoteka, "je premaknjena")
                    break

            else:
                shutil.move(path_dir, path_razno)





#premakni_datoteke(PATH, slovar)
from PIL import Image
import glob
import os

def redimensionne(repertoire, x, y):

    """
    la fonction permet à partir du nom du répertoire (exemeple repertoire = Theme1) de redimensionner toutes
    les images qu'il contient à la taille (x,y) et de lesenregistrer dans un nouveau répertoire appelé
    repertoire_modifié (exemple Theme1_modifié). 
    """
    folder_initial = os.getcwd()

    if f"{repertoire}_modifie" in os.listdir(folder_initial):
        images = os.listdir(f"{repertoire}_modifie")
        os.chdir(f"{repertoire}_modifie")
        for img in images :
             os.remove(img)
        os.chdir(folder_initial)
    else:
        os.mkdir(f"{repertoire}_modifie")

    noms = glob.glob(f"{repertoire}\*.png") #récupère la liste des noms d'image dans le dossier theme repertoire
    n = len(noms)
   
    for i in range(n):
        img_name = noms[i]
        img = Image.open(img_name)
        img_resize = img.resize((x, y)) 
        os.chdir(f"{repertoire}_modifie")
        img_resize.save(f"img_{i}.png")
        os.chdir(folder_initial)


x, y = 113, 170
for i in range(1,4):
    redimensionne(f"test", x, y)

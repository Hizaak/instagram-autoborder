#!/usr/bin/env python
# coding: utf-8
#
# Copyright (c) Alexandre Maurice - 2022
# https://alexandremaurice.fr
#
# This program is provided without warranty and its use is under the sole responsibility of the user.
#

# Ce programme permet d'ajouter une bordure à une image pour ensuite la poster sur Instagram

import sys
import os
from PIL import Image, ImageOps

sys.argv.remove("scriptExportPhotos.py")


def concatener(image,sens,tailleCarre):
    if sens=="Largeur": # On conserve la largeur tailleCarre
        cadre1 = Image.new('RGB', (int((tailleCarre-image.width)/2), tailleCarre), (255, 255, 255))
        cadre2 = Image.new('RGB', (int((tailleCarre-image.width)/2), tailleCarre), (255, 255, 255))
        imageFinale = Image.new('RGB', (tailleCarre, tailleCarre))
        imageFinale.paste(cadre1,(0,0))
        imageFinale.paste(image,(cadre1.width,0))
        imageFinale.paste(cadre2,(cadre1.width+image.width,0))
    if sens=="Hauteur":
        cadre1 = Image.new('RGB', (tailleCarre, int((tailleCarre-image.height)/2)), (255, 255, 255))
        cadre2 = Image.new('RGB', (tailleCarre, int((tailleCarre-image.height)/2)), (255, 255, 255))
        imageFinale = Image.new('RGB', (tailleCarre, tailleCarre))
        imageFinale.paste(cadre1,(0,0))
        imageFinale.paste(image,(0,cadre1.height))
        imageFinale.paste(cadre2,(0,cadre1.height+image.height))
    return imageFinale
    
for path in sys.argv:
    # On vérifie que path finisse en .jpg ou en .png
    if not path.lower().endswith(('.png', '.jpg', '.jpeg')):
        print(path,"n'a pas d'extension valide. Le fichier doit finir par '.png', '.jpg' ou '.jpeg' (insensible à la casse).")
    else:
        baseImage = Image.open(path)
        
        # Créer l'image avec la bordure:
        if baseImage.height>baseImage.width: # Si l'image est plus haute que large
            tailleCarre=baseImage.height # La taille du carré se basera sur la hauteur
        else:
            tailleCarre=baseImage.width
            
        imageAvecBordure = ImageOps.expand(baseImage,border=int(tailleCarre*1.015)-tailleCarre,fill='white')
        if imageAvecBordure.height>imageAvecBordure.width: # Si l'image est plus haute que large
            tailleCarre=imageAvecBordure.height # La taille du carré se basera sur la hauteur
            sensEmpilement="Largeur" # L'empilement sera dans la largeur
        else:
            tailleCarre=imageAvecBordure.width
            sensEmpilement="Hauteur"
            
        imageFinale=concatener(imageAvecBordure,sensEmpilement,tailleCarre)
        
        imageFinale = imageFinale.resize((1080,1080),Image.ANTIALIAS)
        imageFinale.save(os.path.splitext(path)[0]+"_instagram.jpg", 'jpeg', optimize=True, quality=95)

import os
import math

#fonction qui sert à extraire les noms des fichiers
def list_of_files(directory, extension):
    files_names = []
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            files_names.append(filename)
    return files_names

#fonctions qui permet d'extraire les noms des présidents
def extraction():
    d=['1','2','3','4','5','6','7','8','9']
    nom_f = list_of_files("./speeches",".txt")
    for i in range(len(nom_f)):
        nom_f[i] = nom_f[i][11:-4]
        for j in range(len(nom_f[i])):
            if nom_f[i][j] in d:
                nom_f[i] = nom_f[i][:-1]
    return(nom_f)

#fonctions permettant d'eliminer les doublons dans la liste des noms des présidents
def doublon():
    d = extraction()
    s=[]
    for mot in d :
        if mot not in s :
            s.append(mot)
    return s

dico_presidents = {
    'Chirac': 'Jaques',
    'Giscard dEstaing': 'Valérie',
    'Hollande': 'François',
    'Macron': 'Emmanuel',
    'Mitterand': 'François',
    'Sarkozy': 'Nicolas',}

#fonctions qui va faire des nouveaux fichiers à partir des anciennes toute en remplassant les lettre majuscule en minuscule
#et aussi les lettres avec des accents sans accents et en supprimant les ponctuations
def conv_en_minuscule():
    speeches = r'C:\Users\johnn\PycharmProjects\pythonProject2\venv\speeches'
    cleaned = r'C:\Users\johnn\PycharmProjects\pythonProject2\venv\Cleaned'
    a={".", ",", ";", "!", "?", "(", ")", ":", "/"}
    for nom_f in os.listdir(speeches):                   #boucle qui permet d'aller dans les fichiers dans le répértoire "Speeches"
        f_entree = os.path.join(speeches, nom_f)
        with open(f_entree, 'r',encoding='utf-8' ) as f:
            m = ''
            for c in f.read():
                 if 65 <= ord(c) <= 90:
                     m += chr(ord(c) + 32)
                 else:
                    if c in {'é', 'è', 'ê', 'à', 'â', 'î', 'ô', 'û', 'ë', 'ï','ù','ç'}:
                         m += {'é': 'e', 'è': 'e', 'ê': 'e', 'à': 'a', 'â': 'a', 'î': 'i', 'ô': 'o', 'û': 'u','ù':'u' ,'ë': 'e','ï': 'i','ç':'c'}[c]
                    elif c in {"'","-"}:
                        m += " "
                    elif c in a:
                        m += ""
                    else:
                         m += c
            f_sortie = os.path.join(cleaned, nom_f)
            with open(f_sortie, 'w',encoding='utf-8' ) as f1:
                 f1.write(m)




#fonctions qui permet de conter le nombre d'occurences d'un mot dans un texte
def tf(b):
    resultats = {}
    d = 0
    fichiers = [f for f in os.listdir(b) if os.path.isfile(os.path.join(b, f))]
    for fichier in fichiers:
        cf = os.path.join(b, fichier)
        with open(cf, 'r') as f:
            contenu = f.read()
            chaines = contenu.split(" ")
            for mot in chaines:
                if "\n" in mot:
                    mot=mot[:-1]
                if mot in resultats:
                    resultats[mot]+=1
                else:
                    resultats[mot] = 1

    return resultats

#fonctions qui permet de calculer la fréquence d'un mot dans les textes et plus elle est élévée moins elle est fréquente
def idf(A):
    occurences = {}
    total = 0
    for nom_f in os.listdir(A):
        cf = os.path.join(A, nom_f)
        if os.path.isfile(cf):
            total += 1
            with open(cf, 'r') as f:
                mots = f.read().split()
                for mot in set(mots):
                    occurences[mot] = occurences.get(mot, 0) + 1
    idf_scores = {}
    for mot, doc in occurences.items():
        idf_scores[mot] = math.log10(total / ( doc+1))
    return idf_scores




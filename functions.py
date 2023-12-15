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
    speeches = r'C:\pychatbot\speeches'
    cleaned = r'C:\pychatbot\Cleaned'
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
def tf(c):
    z = c.read()
    resultats = {}
    mot = z.split()
    for m in mot :
        if m in resultats :
            resultats[m]+= 1
        else :
            resultats[m] = 1
    return resultats


#fonctions qui permet de calculer la fréquence d'un mot dans les textes et plus elle est élévée moins elle est fréquente

def Idf(d):
    idf_s={}
    for i in d.keys():
       for j in d[i]:
          if j in idf_s:
            idf_s[j]+=1
          else:
            idf_s[j]=1
    for a in idf_s.keys():
            idf_s[a]=math.log10((len(d)/idf_s[a]))
    return idf_s


def TF_IDF(A):
    L=Idf(A)
    Matrice={}
    cleaned = r'C:\pychatbot\Cleaned'
    for mot in L:
        Matrice[mot]=[]
        for file  in list_of_files("./cleaned",".txt" ) :
            with open(cleaned + "/" + file , "r")as f :
                d=tf(f)
            if mot in d:
                Matrice[mot].append(d[mot]*L[mot])
            else:
                Matrice[mot].append(0.0)
    return Matrice


def nn_important(B):
    Liste_de_mot=TF_IDF(B)
    mot_pas_important=[]
    for g,i in Liste_de_mot.items():
            d=0
            for h in i:
                    if h==0.0:
                       d+=1
            if d == 8 :
                mot_pas_important.append(g)
    return mot_pas_important



def m_score_plus_elevé(H):
        Liste_de_mot = TF_IDF(H)
        mot = None
        scoremax = 0.0
        for mots, score in Liste_de_mot.items():
           for d in score :
               if d > scoremax:
                   scoremax = d
                   mot = mots
               elif d == scoremax:
                   mot = mots
        return mot


def Mot_plus_répétés_par_chirac():
    a = r'C:\pychatbot\Cleaned\Nomination_Chirac1.txt'
    b=r'C:\pychatbot\Cleaned\Nomination_Chirac2.txt'
    with open(a, 'r') as f , open(b,'r') as f1 :
        d=tf(f)
        s=tf(f1)
        q={}
        for g,i in d.items():
            for c,v in s.items():
                if g == c :
                    q[g]= i+v
        mot = None
        scoremax = 0
        for mots, score in q.items():
                if score > scoremax:
                    scoremax = score
                    mot = mots
        return mot








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

#fonction pour la matrice TF_IDF
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

# fonction qui permet de renvoyer au mot les moins importants
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


#fonction qui permet de renvoyer le mot avec le plus score idf de tous les fichiers
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

#fonction qui renvoie au mot le plus utiliser par chirac
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

#fonction qui permet de renvoyer tous les noms de présidents qui ont parler de nation et du celui qui en à le plus parler
def Nation():
    a = r'C:\pychatbot\Cleaned'
    d=[]
    for nom_f in os.listdir(a):
        f_entree = os.path.join(a, nom_f)
        with open(f_entree, 'r') as f:
            z=f.read()
            h=z.split()
            for c in h:
                if c == 'nation' or c == 'nations' or c == 'nation/n' or c == 'nation\n':
                    d.append(nom_f)
    g = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

    for i in range(len(d)):
        d[i] = d[i][11:-4]
        for j in range(len(d[i])):
            if d[i][j] in g:
                d[i] = d[i][:-1]

    doublon=[]
    for double in d :
        if double not in doublon :
            doublon.append(double)
    lpu={}
    for i in d :
        if i in lpu:
            lpu[i]+=1
        else:
            lpu[i]=1
    mot = None
    scoremax = 0
    for mots, score in lpu.items():
        if score > scoremax:
            scoremax = score
            mot = mots
    return doublon,mot

#fonction qui permet de renvoyer tous les noms de présidents qui ont parler d'écologie
#fonction repris de nation
def ecolo():
    a = r'C:\pychatbot\Cleaned'
    d = []
    for nom_f in os.listdir(a):
        f_entree = os.path.join(a, nom_f)
        with open(f_entree, 'r') as f:
            z = f.read()
            h = z.split()
            for c in h:
                if c == 'climat' or c == 'ecologie' or c == 'ecologique' or c == 'climatique':
                    d.append(nom_f)
    g = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

    for i in range(len(d)):
        d[i] = d[i][11:-4]
        for j in range(len(d[i])):
            if d[i][j] in g:
                d[i] = d[i][:-1]

    doublon = []
    for double in d:
        if double not in doublon:
            doublon.append(double)

    return doublon








#Partie 2
# fonction qui permet de convertir en minuscule et d'enlever les accents(pas demandé)
def minuscule(texte):
    d=''
    for lettre in texte:
        s=''
        if 65 <= ord(lettre) <= 90:
                s+=chr(ord(lettre)+32)
        elif lettre == 'é' or lettre == 'è' or lettre == 'ê' or lettre == 'ë':
            s += 'e'
        elif lettre == 'à' or lettre == 'â':
            s += 'a'
        elif lettre == 'ù' or lettre == 'û' :
            s += 'u'
        elif lettre == 'ï':
            s += 'i'
        elif lettre == 'ç':
            s += 'c'
        else:
            s+= lettre
        d+=s
    return d




#fonction qui permet de convertir les majuscule , enlever les signes de ponctuation ,enlever les accents et enfin va renvoyer la question dans une liste
def Tokenisation_de_la_Q(question):
    Question=[]
    Question_nettoye=''
    for ponctuation in question :
        if ponctuation in [',','.','?',';',':','!']:
            ponctuation=''
        elif ponctuation in ["'","-"]:
            ponctuation= ' '
        else :
            ponctuation=minuscule(ponctuation)
        Question_nettoye+=ponctuation
    h = Question_nettoye.split()
    for i in h :
             Question.append(i)
    return Question

#fonction qui permet de renvoyer les mots trouvés dans le corpus
def mot_dans_le_corpus(listedemot):
    Mots_dans_corpus=[]
    mot_double=[]
    d=r'C:\pychatbot\Cleaned'
    for mot in os.listdir(d):
        f_entree = os.path.join(d, mot)
        with open(f_entree, 'r') as f:
            texte = f.read()
            mots = texte.split()
            for i in mots :
                if i in listedemot:
                    mot_double.append(i)
            for doublemot in mot_double :
                if doublemot not in Mots_dans_corpus:
                    Mots_dans_corpus.append(doublemot)

    return Mots_dans_corpus






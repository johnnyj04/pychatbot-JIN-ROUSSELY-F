import os
import math


def list_of_files(directory, extension):
    files_names = []
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            files_names.append(filename)
    return files_names


def extraction():
    d=['1','2','3','4','5','6','7','8','9']
    nom_f = list_of_files("./speeches",".txt")
    for i in range(len(nom_f)):
        nom_f[i] = nom_f[i][11:-4]
        for j in range(len(nom_f[i])):
            if nom_f[i][j] in d:
                nom_f[i] = nom_f[i][:-1]
    return(nom_f)


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

def conv_en_minuscule():
    speeches = r'C:\Users\johnn\PycharmProjects\pythonProject2\venv\speeches'
    cleaned = r'C:\Users\johnn\PycharmProjects\pythonProject2\venv\Cleaned'
    a={".", ",", ";", "!", "?", "(", ")", ":", "/"}
    for nom_f in os.listdir(speeches):
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





def tf(dossier):
    resultats = {}
    d = 0
    fichiers = [f for f in os.listdir(dossier) if os.path.isfile(os.path.join(dossier, f))]
    for fichier in fichiers:
        cf = os.path.join(dossier, fichier)
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


def calculer_idf(repertoire_corpus):
    documents_contenant_mot = {}
    total_documents = 0
    for nom_fichier in os.listdir(repertoire_corpus):
        chemin_fichier = os.path.join(repertoire_corpus, nom_fichier)

        # Ignorer les sous-répertoires
        if os.path.isfile(chemin_fichier):
            total_documents += 1

            # Lire le contenu du fichier, diviser en mots
            with open(chemin_fichier, 'r') as fichier:
                mots = fichier.read().split()

                # Mettre à jour le dictionnaire des documents contenant chaque mot
                for mot in set(mots):
                    documents_contenant_mot[mot] = documents_contenant_mot.get(mot, 0) + 1

    # Calculer le score IDF pour chaque mot
    idf_scores = {}
    for mot, documents_contenant in documents_contenant_mot.items():
        idf_scores[mot] = math.log10(total_documents / (1 + documents_contenant))

    # Retourner le dictionnaire des scores IDF
    return idf_scores


    contenu_modifie = contenu_sans_ponctuation.replace("'", ' ').replace('-', ' ')


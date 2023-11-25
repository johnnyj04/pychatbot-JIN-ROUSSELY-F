import os
import math


def list_of_files(directory, extension):
    files_names = []
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            files_names.append(filename)
    return files_names


def extraction():
    nom_f = list_of_files("./speeches",".txt")
    for i in range(len(nom_f)):
        nom_f[i] = nom_f[i][11:-4]
        for j in range(len(nom_f[i])):
            if nom_f[i][j] == '1' or nom_f[i][j] == '2' :
                nom_f[i] = nom_f[i][:-1]
    return(nom_f)

#Association des prénoms au présidents
dico_presidents = {
    'Chirac': 'Jaques',
    'Giscard dEstaing': 'Valérie',
    'Hollande': 'François',
    'Macron': 'Emmanuel',
    'Mitterand': 'François',
    'Sarkozy': 'Nicolas',
}

nom = ['Chirac','Giscard dEstaing','Hollande','Macron','Mitterrand','Sarkozy']

#Affichage des noms des présidents
def p_names ():
   p_names = list_of_files("./speeches", ".txt")
   list_names = []
   for file in p_names :
       name = file[11 : len(file)-4]
       while ord(name[len(name)-1]) >= 48 and ord(name[len(name)-1]) <= 57 :
           name = name[:len(name)-1]
       if name not in list_names :
           list_names.append(name)
   return list_names

import os

def minuscule_accent():

    # Chemin du dossier contenant les fichiers textes
    dossier_entree = r'C:\Users\johnn\PycharmProjects\pythonProject2\venv\speeches'

    # Chemin du dossier de sortie pour les fichiers en minuscules
    dossier_sortie = r'C:\Users\johnn\PycharmProjects\pythonProject2\venv\Cleaned'

    # Parcours de tous les fichiers dans le dossier d'entrée
    for nom_fichier in os.listdir(dossier_entree):
        chemin_fichier_entree = os.path.join(dossier_entree, nom_fichier)

        # Lecture du contenu et transformation en minuscules avec les codes ASCII
        with open(chemin_fichier_entree, 'r',) as fichier_entree:
            contenu_minuscules = ''
            for char in fichier_entree.read():
                if 65 <= ord(char) <= 90:
                    contenu_minuscules += chr(ord(char) + 32)
                else:
                    if char in {'é', 'è', 'ê', 'à', 'â', 'î', 'ô', 'û', 'ë', 'ï'}:
                        contenu_minuscules += {'é': 'e', 'è': 'e', 'ê': 'e', 'à': 'a', 'â': 'a', 'î': 'i', 'ô': 'o', 'û': 'u', 'ë': 'e', 'ï': 'i'}[char]
                    else:
                        contenu_minuscules += char

            # Construction du chemin du fichier de sortie
            chemin_fichier_sortie = os.path.join(dossier_sortie, nom_fichier)

            # Écriture du contenu modifié dans le fichier de sortie
            with open(chemin_fichier_sortie, 'w',) as fichier_sortie:
                fichier_sortie.write(contenu_minuscules)




def sans_ponctuation():
    # Chemin du dossier contenant les fichiers en minuscules
    dossier_entree = r'C:\Users\johnn\PycharmProjects\pythonProject2\venv\Cleaned'

    # Liste des caractères de ponctuation à exclure
    caracteres_ponctuation = set(".,;!?()[]{}<>:;-_+=*&^%$#@!`~\"'/\\|")

    # Parcours de tous les fichiers dans le dossier d'entrée
    for nom_fichier in os.listdir(dossier_entree):
        chemin_fichier_entree = os.path.join(dossier_entree, nom_fichier)

        # Vérification si le chemin correspond à un fichier texte
        if os.path.isfile(chemin_fichier_entree) and nom_fichier.endswith('.txt'):
            # Lecture du contenu et suppression des caractères de ponctuation
            with open(chemin_fichier_entree, 'r') as fichier_entree:
                contenu = fichier_entree.read()
                contenu_sans_ponctuation = ''.join(char if char not in caracteres_ponctuation else '' for char in contenu)

            # Écriture du contenu modifié dans le même fichier
            with open(chemin_fichier_entree, 'w') as fichier_sortie:
                fichier_sortie.write(contenu_sans_ponctuation)

def nombre_de_mot(dossier):
    resultats = {}
    d = 0

    # Obtenez la liste des fichiers dans le dossier
    fichiers = [f for f in os.listdir(dossier) if os.path.isfile(os.path.join(dossier, f))]

    for fichier in fichiers:
        chemin_fichier = os.path.join(dossier, fichier)

        with open(chemin_fichier, 'r') as f:
            contenu = f.read()
            chaines = contenu.split(" ")

            # Créez un sous-dictionnaire pour chaque fichier
            sous_dictionnaire = {}
            for mot in chaines:
                if mot != " ":
                    sous_dictionnaire[d] = mot
                    d += 1

            # Ajoutez l e sous-dictionnaire au dictionnaire principal
            resultats[fichier] = sous_dictionnaire

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


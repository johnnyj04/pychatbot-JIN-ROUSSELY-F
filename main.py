# Call of the function
from functions import*


directory = "./speeches"
files_names = list_of_files(directory, "txt")
print(files_names)
d=extraction()
print(d)
directory = r'C:\Users\johnn\PycharmProjects\pythonProject2\venv\speeches'
files_names = list_of_files(directory, "txt")
minuscule_accent()

sans_ponctuation()

resultat_final = nombre_de_mot(r'C:\Users\johnn\PycharmProjects\pythonProject2\venv\Cleaned')
print(resultat_final)


repertoire_corpus_test = r'C:\Users\johnn\PycharmProjects\pythonProject2\venv\Cleaned'
resultat_idf = calculer_idf(repertoire_corpus_test)
print(resultat_idf)



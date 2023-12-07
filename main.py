from functions import*



s=doublon()
print(s)

conv_en_minuscule()
d=r'C:\Users\johnn\PycharmProjects\pythonProject2\venv\Cleaned'
Grand_tf={}
for nom_f in os.listdir(d):
    f_entree = os.path.join(d, nom_f)
    with open(f_entree, 'r', encoding='utf-8') as f:
         occurence = tf(f)
         Grand_tf[nom_f] = occurence
print(Grand_tf)




resultat_idf = Idf(Grand_tf)
print(resultat_idf)
res=TF_IDF(Grand_tf,resultat_idf)
print(res)


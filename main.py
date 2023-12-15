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
res=TF_IDF(Grand_tf)
print(res)

Mot_pas_important=nn_important(Grand_tf)
print(Mot_pas_important)

Mot_important=m_score_plus_elevé(Grand_tf)
print(Mot_important)

motpourchirac=Mot_plus_répétés_par_chirac()
print(motpourchirac)
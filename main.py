from functions import*

print("Bonjour , bienvenu sur pychatbot ")
print("Appuyer sur 1 pour savoir la liste des mots les moins importants dans le corpus de documents")
print("Appuyer sur 2 pour afficher le(s) mot(s) ayant le score TD-IDF le plus élevé")
print("Appuyer sur 3 pour savoir quel(s) mot(s) le président Chirac a le plus répété")
print("Appuyer sur 4 pour indiquer le(s) nom(s) du (des) président(s) qui a (ont) parlé de la Nation et celui qui l’a répété le plus de fois")
print("Appuyer sur 5 pour indiquer le(s) nom(s) du (des) président(s) qui a (ont) parlé du climat et/ou de l’écologie")

n = int(input("Le numéro que vous voulez choisir :"))

while n >= 6 :
    print("Vous devez choisir entre 1 , 2 , 3 , 4 , 5 ")
    n = int(input("Le numéro que vous voulez choisir :"))

print("Veuillez attendre quelques secondes")

conv_en_minuscule()

d = r'C:\Users\johnn\PycharmProjects\pythonProject2\venv\Cleaned'

Grand_tf = {}

for nom_f in os.listdir(d):
    f_entree = os.path.join(d, nom_f)
    with open(f_entree, 'r', encoding='utf-8') as f:
        occurence = tf(f)
        Grand_tf[nom_f] = occurence

resultat_idf = Idf(Grand_tf)
res = TF_IDF(Grand_tf)
Mot_pas_important = nn_important(Grand_tf)
Mot_important = m_score_plus_elevé(Grand_tf)
motpourchirac = Mot_plus_répétés_par_chirac()
nation, mot = Nation()
Ecologie = ecolo()

if n == 1:
    print("les mots les moins important sont :",Mot_pas_important)

if n == 2:
    print("Le(s) mot(s) le(s) plus important est (sont) :",Mot_important)

if n == 3:
    print("Le(s) mot(s) le(s) plus important prononcé par le président Chirac est (sont) :",motpourchirac)

if n == 4:
    print("Le(s)président(s) qui a (ont) parlé de la Nation est :" ,nation," le président qui l'a répété le plus de fois est  :",mot)

if n == 5:
    print("Le(s)président(s) qui a (ont) parlé de l'ecologie /climat est (sont) :",Ecologie)

r=True

while r==True:

    a=input("Voulez-vous refaire une commance?(oui/non):")

    if a == 'oui':

        n = int(input("Le numéro que vous voulez choisir :"))

        if n == 1:

            print("les mots les moins important sont :", Mot_pas_important)

        if n == 2:

            print("Le(s) mot(s) le(s) plus important est (sont) :", Mot_important)

        if n == 3:

            print("Le(s) mot(s) le(s) plus important prononcé par le président Chirac est (sont) :", motpourchirac)

        if n == 4:

            print("Le(s)président(s) qui a (ont) parlé de la Nation est :", nation, " le président qui l'a répété le plus de fois est  :",mot)

        if n == 5:

            print("Le(s)président(s) qui a (ont) parlé de l'ecologie /climat est (sont) :", Ecologie)

    else :

        r=False


question=input("quelle est votre question ?")
Questions=Tokenisation_de_la_Q(question)
print(Questions)
mot_présent=mot_dans_le_corpus(Questions)
print(mot_présent)
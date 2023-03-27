import pandas as pd

email_perso = ["gmail.com","outlook.com","outlook.fr","yahoo.fr","yahoo.fr","hotmail.fr"]
check=[]

def check_email(df_email):
    for x in range(len(df_email)):
        email = (df_email["dropcontactEmail"][x])
        email = email.split("@")[1]
        print(email)
        if email in email_perso:
            check.append("A supprimer")
        else:
            check.append("")

    df_email["Check_email"] = check
    print(len(df_email))

    df_email = df_email.loc[df_email["Check_email"] != "A supprimer",'linkedinUrl'].values[0]
    df_email.to_csv("resultats.csv")
    print(len(df_email))



def check_email_v2(df):
    import pandas as pd

    termes_a_rechercher = ['gmail.com', 'outlook.com', 'outlook.fr', 'yahoo.fr', 'yahoo.fr', 'hotmail.fr']

    # Créer une fonction pour identifier si un élément doit être supprimé
    def a_supprimer(email):
        for terme in termes_a_rechercher:
            if terme in email:
                return True
        return False

    # Appliquer la fonction 'a_supprimer' à la colonne 'dropcontactEmail' et créer une nouvelle colonne 'A supprimer'
    df['A supprimer'] = df['dropcontactEmail'].apply(a_supprimer)

    # Filtrer le dataframe pour ne garder que les lignes qui ne doivent pas être supprimées
    df_filtré = df[df['A supprimer'] == False]

    df_filtré.to_csv('resultat_filtré.csv', index=False)

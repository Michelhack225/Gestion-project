class tache():
   def __init__(self, titre, termine):
        self.titre = titre
        self.termine = termine

   def marquer_termine(self):
        self.termine = True

   def __str__(self):
       if self.termine:
           result = f"[x] {self.titre}"
           return result
       else:
           return f"[] {self.titre}"

class GestionnnaireTache():
    def __init__(self, liste):
        self.liste = []

    def ajouter_tache(self, titre):
        self.liste.append(tache(titre,False))

    def afficher_tache(self):
        if self.liste == []:
            print("Aucune tache")
        else:
            i = 1
            for tachee in self.liste:
                print(i, tachee)
                i+= 1

    def termine_tache(self, index):
        if 0 <= index < len(self.liste):
            self.liste[index].termine = True
            print(f"Tâche '{self.liste[index].titre}' terminée !")
        else:
            print("Index invalide ! Aucune tâche correspondante.")



def log_execution(fonction):
    def new_execution(*args, **kwargs):
        print("Debut de l'excution ")
        result = fonction(*args, **kwargs)
        print("Fin de l'execution")
        return result
    return new_execution

@log_execution
def font():
    try:
        print("menu en cours ...")

    except Exception as e:
        print("Fin de l'execution", e)

@log_execution
def menu():
    gestionnaire = GestionnnaireTache( liste=[])
    while True :
        print("\n :::: Menu ::::")
        print("1- Ajouter une tâche")
        print("2- Afficher les tâches ")
        print("3- Terminer une tache ")
        print("4- Quitter")
        try:
            choix = int(input("Veillez faire vôtre choix : "))
        except ValueError:
            print("Choix invalide, Veillez saisir un autre nombre  ")
            continue
        if choix == 1:
           ajou = input("Veillez saisir la tache que vous souhaitez ajouter : ")
           gestionnaire.ajouter_tache(ajou)
        elif choix ==2:
            gestionnaire.afficher_tache()
        elif choix ==3:
            gestionnaire.afficher_tache()
            try:
                num = int(input("Veuillez saisir le numéro de la tache à terminer : ")) - 1
                gestionnaire.termine_tache(num)
            except ValueError:
                print("Numéro invalide")

        elif choix ==4:
            print("Fin du programme ")
            break
        else:
            print("Choix invalide")

if __name__ == "__main__":
   menu()



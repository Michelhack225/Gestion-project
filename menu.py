def menu():
    print("1- Ajouter une tâche")
    print("2- Afficher les tâches ")
    print("3- Terminer une tache ")
    print("4- Quitter")

    choix = int(input("Veillez faire vôtre choix : "))
    while(choix != 4):
        if choix ==1:
            print()
        elif choix ==2:
            print()
        elif choix ==3:
            print()
        else:
            print("Fin du programme ")

m = menu()
m.menu()


def log_execution(menu):
    def new_execution():
        print("Debut de l'excution ")
        menu()
        print("Fin de l'execution")

@log_execution
def menu():
    menu()






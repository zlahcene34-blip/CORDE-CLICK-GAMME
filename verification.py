import os

def verifier_structure():
    # Liste des fichiers et dossiers attendus selon le modèle NSI
    attendus = [
        "sources/index.html",
        "docs/documentation.md",
        "Instructions.md",
        "LICENSE",
        "README.md",
        "presentation.md"
    ]
    
    print("--- VÉRIFICATION DU PROJET DUEL DE CLICS ---")
    erreurs = 0
    
    for chemin in attendus:
        if os.path.exists(chemin):
            print(f"[OK] Présent : {chemin}")
        else:
            print(f"[ERREUR] Manquant : {chemin}")
            erreurs += 1
            
    if erreurs == 0:
        print("\nStructure parfaite ! Le projet est prêt pour le concours.")
    else:
        print(f"\nAttention : il manque {erreurs} élément(s).")

if __name__ == "__main__":
    verifier_structure()

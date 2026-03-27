# Documentation Technique - Duel de Clics 🕹️

Ce document présente les choix techniques, les algorithmes et la structure du projet réalisés dans le cadre du concours Trophée NSI.

## 1. Architecture et Technologies
Le projet repose sur les technologies web standards (Front-end) pour garantir une portabilité maximale :
* **HTML5** : Structuration de l'interface et de la borne d'arcade.
* **CSS3** : Mise en forme avec un design "Retro-Arcade" (utilisation de filtres scanlines, animations néons et polices pixelisées).
* **JavaScript (Vanilla)** : Logique métier du jeu, sans bibliothèque externe.
* **Canvas API** : Utilisée pour le rendu graphique haute performance des personnages et de la corde.

## 2. Logique Algorithmique
Le cœur du jeu repose sur plusieurs concepts clés :
* **Gestion d'état (State Management)** : Une variable centrale `pos` (position) définit l'équilibre de la corde. Elle oscille entre deux bornes (`-250` et `250`).
* **Système d'Événements** : Le jeu écoute les pressions de touches (`keydown`) pour déclencher les fonctions de mouvement de manière asynchrone.
* **Boucle de Rendu (Game Loop)** : Utilisation de `requestAnimationFrame` pour assurer une fluidité à 60 images par seconde (FPS).
* **Calcul des Combos** : Un algorithme calcule le temps écoulé entre deux clics pour appliquer un multiplicateur de force, récompensant la vitesse de frappe.

## 3. Structure du Dépôt
Conformément aux standards de développement :
* `/sources` : Contient le code source exécutable (`index.html`).
* `/data` : Dossier réservé aux ressources (images, sons).
* `/tests` : Emplacement pour les futurs scripts de tests unitaires.
* `/docs` : Présente la présente documentation technique.

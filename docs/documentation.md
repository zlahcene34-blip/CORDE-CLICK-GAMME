# Documentation Technique - Duel de Clics 🕹️

Ce document présente les choix techniques et la structure du projet réalisé pour le Trophée NSI.

## 1. Choix des technologies
* **HTML5 / CSS3** : Pour la structure de la borne d'arcade et les effets visuels (scanlines, néons).
* **JavaScript (Vanilla)** : Pour la logique de jeu, la gestion des collisions et les animations.
* **Canvas API** : Utilisée pour dessiner les personnages en pixel art de manière dynamique.

## 2. Algorithmes principaux
* **Gestion du Duel** : Le jeu utilise une variable `pos` qui oscille entre `-250` et `250`. Chaque clic d'un joueur modifie cette valeur.
* **Système de Combo** : Un multiplicateur de vitesse est appliqué si un joueur enchaîne les clics rapidement, augmentant la difficulté.
* **Boucle de rendu** : Utilisation de `requestAnimationFrame` pour assurer une animation fluide à 60 FPS.

## 3. Structure du code
Le code est centralisé dans `sources/index.html` pour faciliter la portabilité, mais séparé logiquement en trois blocs : `style` (visuel), `body` (structure) et `script` (logique).

# 🕹️ Présentation du Projet : Duel de Clics

## 💡 Genèse du projet
L'idée de **Duel de Clics** est née de l'envie de créer un jeu multijoueur local simple mais addictif, inspiré de l'esthétique des bornes d'arcade des années 80. L'objectif technique était de gérer des entrées clavier simultanées et fluides dans un navigateur.

## 🛠️ Concepts NSI utilisés
Ce projet m'a permis de mettre en pratique plusieurs points clés du programme de spécialité :
* **Programmation Événementielle** : Utilisation d'`EventListener` pour capturer les touches `A` et `P` sans latence.
* **Manipulation du DOM** : Mise à jour en temps réel des scores et de la position de la corde sans recharger la page.
* **Gestion du Temps** : Mise en place d'une boucle de jeu (`requestAnimationFrame`) pour assurer une animation fluide à 60 FPS.
* **Algorithmique** : Logique de calcul de la "tension" de la corde et détection de la zone de victoire.

## 🚀 Défis relevés
Le plus gros défi a été de s'assurer que si les deux joueurs appuient en même temps, le jeu traite les deux informations de manière équitable. J'ai aussi travaillé sur l'aspect visuel (CSS "Neon") pour que l'immersion soit totale malgré la simplicité du gameplay.

## 🎯 Conclusion
Ce projet est pour moi une première étape réussie dans le développement de jeux web. Il montre qu'avec des technologies standards (HTML/JS), on peut créer une expérience interactive complète et compétitive.

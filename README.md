# 🕹️ Duel de Clics

![HTML](https://img.shields.io/badge/HTML5-E34F26?style=flat&logo=html5&logoColor=white)
![CSS](https://img.shields.io/badge/CSS3-1572B6?style=flat&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat&logo=javascript&logoColor=black)
![Licence](https://img.shields.io/badge/Licence-GPL%20v3%2B-blue)

---

## 📝 Description

**Duel de Clics** est un jeu de tireuse de corde (*tug of war*) pour deux joueurs sur le même clavier, avec une esthétique **arcade rétro** (style borne des années 80 : scanlines CRT, néons, pixel art, police 8-bit).

L'objectif est simple : appuyer le plus rapidement possible sur sa touche pour tirer le foulard central vers son camp avant l'adversaire. Un système de **combo** récompense les clics rapides en accélérant la vitesse de traction.

Nous avons choisi ce sujet car il combine accessibilité (une seule page web, aucune installation) et richesse technique (rendu canvas, animation frame-by-frame, gestion d'états). Il répond aux critères des Trophées NSI par son **originalité visuelle** et sa **jouabilité immédiate** à deux.

---

## 👥 L'Équipe

| Nom Prénom | Pseudo Git | Responsabilité |
|---|---|---|
| Ferhi Ilyane | @ilyane-ferhi | Logique de jeu & Algorithmes |
| Lahcene Zakaria | @zakaria-lahcene | Interface Graphique & Assets |

---

## 🛠️ Aspects Techniques (Spécificités NSI)

### Langages et technologies
- **HTML5** — structure de la page et élément `<canvas>` pour le pixel art
- **CSS3** — animations (`@keyframes`), variables CSS (`--neon-green`, etc.), effets visuels (scanlines, vignette CRT, grille de perspective)
- **JavaScript (Vanilla)** — logique de jeu complète, sans framework ni bibliothèque externe

### Structures de données
- **Variables d'état** : `pos` (position entière du foulard), `state` (machine à états : `'menu'` / `'game'`), `leftScore` / `rightScore` (compteurs de manches)
- **Tableaux implicites** via la génération dynamique de DOM (les pips de combo sont créés et indexés dans une boucle)
- **Constantes de configuration** : `LIMITE`, `VITESSE`, `MAX_COMBO` — séparation claire des paramètres de gameplay et de la logique

### Concepts mobilisés

**Gestion d'états (automate fini)**
Le jeu passe entre trois états (`menu` → `game` → `menu`) ; chaque appui sur une touche est ignoré si `state !== 'game'`, ce qui sécurise les transitions.

**Animation avec `requestAnimationFrame`**
La boucle `animateSprites()` s'appelle récursivement via `requestAnimationFrame` pour dessiner les sprites pixel art à chaque frame, garantissant une synchronisation avec le rafraîchissement écran.

**Rendu procédural sur Canvas**
Les personnages pixel art sont générés **programmatiquement** (aucune image externe) via l'API `CanvasRenderingContext2D` : rects de couleur, transformation miroir (`ctx.scale(-1,1)`), animation des membres liée au compteur `frame`.

**Système de combo**
`comboLeft` et `comboRight` sont incrémentés à chaque clic du joueur correspondant et décrémentés pour l'adversaire. La vitesse de traction vaut `VITESSE + Math.floor(combo / 3)`, introduisant une **progression non linéaire** récompensant les rafales.

**Manipulation du DOM**
Mise à jour en temps réel du flag (`flag.style.left`), des barres de puissance (`barLeft.style.width`), des scores et des pips de combo à chaque appui.

**Gestion des événements clavier**
L'écouteur `keydown` filtre les répétitions automatiques (`e.repeat`) pour ne compter qu'un clic réel par frappe, garantissant l'équité du jeu.

---

## 🚀 Installation et Utilisation

### Prérequis
- Un navigateur web moderne (Chrome, Firefox, Edge, Safari) — **aucune installation requise**

### Lancement
1. Télécharger ou cloner le dépôt
2. Ouvrir le fichier `index.html` directement dans un navigateur
3. Ou double-cliquer dessus depuis l'explorateur de fichiers

```
git clone https://github.com/<pseudo>/duel-de-clics.git
cd duel-de-clics
# Ouvrir index.html dans votre navigateur
```

### Contrôles

| Action | Joueur 1 (Gauche) | Joueur 2 (Droite) |
|---|---|---|
| Tirer la corde | **a** | **P** |
| Démarrer / Rejouer | **Entrée** | **Entrée** |

> Sur mobile ou tablette, les boutons à l'écran sont également cliquables.

---

## 📊 État d'avancement (Journal de bord)

- [x] **Jalon 1** — Cahier des charges, structure HTML/CSS de base et esthétique arcade
- [x] **Jalon 2** — Logique de jeu complète : position, victoire, scores, système de combo
- [x] **Jalon 3** — Sprites pixel art animés sur Canvas, effets visuels (scanlines, néons, shake)
- [ ] **Jalon 4** — Vidéo de démonstration, tests et optimisations finales

---

## 📸 Captures d'écran

><img width="1876" height="952" alt="image" src="https://github.com/user-attachments/assets/92b1a887-95d5-47ce-a1be-88cad97faad4" />


---

## 📜 Licence

Le code source est placé sous licence libre **GPL v3+**.
Le texte et les ressources graphiques sont placés sous licence **Creative Commons CC By-Sa**.

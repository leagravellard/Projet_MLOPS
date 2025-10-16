# 🧠 Projet_MLOPS

## Introduction

Nous avons initié un dépôt GitHub, nommé **`Projet_MLOPS`**, **initialisé comme un dépôt public** afin de permettre un travail collaboratif sur notre projet.

La **branche principale** du dépôt est **`main`**, qui servira de base commune à l’ensemble du groupe.

Trois **branches de travail** ont été créées à partir de `main` :

- **`léa_work`**
- **`abdoulaye_work`**
- **`fernanda_work`**

Chaque membre du groupe travaillera sur sa propre branche afin de développer, tester et valider ses parties du projet avant de fusionner les modifications sur la branche principale.

Ce dépôt nous servira de **support central pour le développement collaboratif du projet MLOps**.

Nous avons également créé un fichier **`.gitignore`** afin d’exclure notre environnement virtuel du dépôt, car celui-ci est trop volumineux pour être stocké sur GitHub.  
Pour pallier cela, nous avons mis en place un fichier **`requirements.txt`** qui contient l’ensemble des bibliothèques nécessaires à l’exécution du projet.  

Nous avons également intégré un **notebook Jupyter** dans lequel nous avons réalisé notre travail de machine learning et testé **trois algorithmes de classification**.

---

## 1️⃣ Projet ML

Dans le cadre de ce projet, nous avons mis en œuvre une **approche de Machine Learning supervisé** visant à **prédire le risque de défaut de prêt** pour les clients d’une banque.  
L’objectif principal est de déterminer, à partir des caractéristiques d’un emprunteur, s’il existe un risque que celui-ci **ne rembourse pas son prêt**.

### Type de modèle
Nous avons développé un **modèle de classification binaire**, dont la variable cible indique si le client est en **défaut de paiement (`1`)** ou **non (`0`)**.

### Modèles testés
Trois modèles de Machine Learning ont été entraînés et comparés :

1. **Decision Tree Classifier**  
   Un modèle simple mais interprétable, permettant de visualiser la hiérarchie des décisions.

2. **Logistic Regression**  
   Un modèle linéaire de référence, souvent utilisé pour les problèmes de classification binaire.

3. **Random Forest Classifier**  
   Un ensemble d’arbres de décision, plus robuste, combinant plusieurs modèles pour améliorer la performance globale.

### Suivi et traçabilité avec MLflow
Nous avons intégré **MLflow** dans notre workflow afin de :
- **Suivre les expériences** et les paramètres utilisés pour chaque modèle,  
- **Comparer les métriques de performance**,  
- **Sauvegarder les artefacts** (modèles, métriques et visualisations) pour assurer la reproductibilité du projet.

Chaque modèle a été enregistré dans MLflow comme un **experiment distinct**, et chaque exécution comme un **run**, ce qui nous a permis d’analyser précisément les performances.

### Métriques d’évaluation
Pour comparer les trois modèles, nous avons utilisé plusieurs métriques :
- **Accuracy** : proportion de prédictions correctes sur l’ensemble du jeu de test,  
- **Precision** : proportion de prédictions positives réellement correctes,  
- **Recall** : capacité du modèle à détecter les vrais cas de défaut,  
- **F1-score** : moyenne harmonique entre la précision et le rappel,  
- **ROC AUC** : capacité du modèle à distinguer les deux classes.

### Résultats obtenus
Après expérimentation, le modèle **de Régression Logistique (Modèle 2)** s’est révélé être **le plus performant** sur notre jeu de données.  
Voici ses principales métriques :

| Métrique      | Valeur |
|----------------|--------|
| Accuracy       | 0.999  |
| Precision      | 1.000  |
| Recall         | 0.995  |
| F1-score       | 0.997  |
| ROC AUC        | 1.000  |

### ✅ Choix du modèle final
Compte tenu de ses performances élevées et de sa stabilité, le modèle de **Régression Logistique** a été sélectionné comme **modèle final**.  
Ce modèle sera intégré dans une **application MLOps** afin de permettre aux utilisateurs de :
- **saisir les caractéristiques d’un client**,  
- et **obtenir une prédiction instantanée** du risque de défaut de paiement.

Ainsi, l’application permettra de savoir si un emprunteur risque **oui ou non de ne pas rembourser son prêt**.

---

## 2️⃣ Application Flask

### Objectif
Nous avons développé une **application Flask** permettant à un utilisateur (par exemple un conseiller bancaire) de **prédire le risque de défaut de paiement d’un client** à partir de ses informations financières.  
L’application repose directement sur notre **modèle de Régression Logistique**, précédemment entraîné et sauvegardé.

### Fonctionnement
L’interface web propose **six variables d’entrée** correspondant aux caractéristiques principales d’un emprunteur :

- `credit_lines_outstanding`
- `loan_amt_outstanding`
- `total_debt_outstanding`
- `income`
- `years_employed`
- `fico_score`

Après saisie de ces données, l’application utilise le modèle **`model_ML2.pkl`** pour effectuer une prédiction instantanée :
- **⚠️ 1 → Risque de défaut élevé**
- **✅ 0 → Aucun risque détecté**

Le résultat s’affiche directement à l’écran avec un message clair et coloré.

---

## 3️⃣ Conteneurisation avec Docker

### Mise en place
Afin de rendre cette application **portable et facilement déployable**, nous l’avons **conteneurisée avec Docker**.  
Cela permet de garantir une exécution stable sur n’importe quelle machine, sans dépendance manuelle.

Le **Dockerfile** crée une image basée sur `python:3.11-slim`, installe les dépendances listées dans `requirements.txt`, et exécute automatiquement l’application Flask.

### Construction de l’image
L’image Docker a été construite localement avec la commande :

`docker build -t lea_mlops_app .`

Puis lancée via : 
`docker run -p 5000:5000 lea_mlops_app`

L’application est ensuite accessible à l’adresse :
👉 http://127.0.0.1:5000

## Publication sur Docker Hub

L’image finale a été poussée sur Docker Hub afin d’être partagée et réutilisée facilement.
Elle est disponible publiquement sous le nom :

`leaso92/lea_mlops_app`

🔄 Téléchargement et exécution

N’importe quel utilisateur peut la télécharger et la tester en une seule commande :

`docker pull leaso92/lea_mlops_app:latest`
`docker run -p 5000:5000 leaso92/lea_mlops_app`
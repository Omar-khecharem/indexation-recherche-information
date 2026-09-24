# 🔎 Indexation et Recherche d'Information

Projet réalisé dans le cadre des travaux pratiques du module **Indexation et Recherche d'Information**.

Ce projet met en œuvre progressivement les principales techniques utilisées dans les moteurs de recherche : **prétraitement du texte, indexation, recherche booléenne, TF-IDF, modèle vectoriel, similarité cosinus et classement des résultats**.

L'objectif est de comprendre, à travers une implémentation Python simple, comment un moteur de recherche transforme une collection de documents en une structure permettant de retrouver et classer les documents les plus pertinents pour une requête.

---

## 📚 Contenu du projet

Le projet est organisé autour de plusieurs travaux pratiques permettant de construire progressivement un moteur de recherche.

### TP1 — Recherche et prétraitement

Première approche de la recherche d'information à partir d'une collection de documents.

* Lecture d'une collection de documents
* Recherche naïve de termes
* Tokenisation
* Conversion en minuscules
* Suppression des stopwords
* Recherche de termes dans les documents
* Mesure du temps d'exécution

### TP2 — Indexation inversée

Mise en place d'une structure d'indexation permettant d'améliorer la recherche.

* Construction d'un index inversé
* Association des termes aux documents
* Recherche par terme
* Recherche de plusieurs termes
* Intersection des résultats
* Comparaison avec la recherche naïve
* Mesure des performances

### TP3 — Modèle vectoriel et TF-IDF

Extension du moteur avec une représentation mathématique des documents et des requêtes.

* Construction d'un index inversé enrichi
* Calcul du **DF (Document Frequency)**
* Calcul de l'**IDF (Inverse Document Frequency)**
* Calcul du **TF-IDF**
* Construction du vocabulaire global
* Représentation vectorielle des documents
* Représentation vectorielle des requêtes
* Calcul de la **similarité cosinus**
* Classement des documents par pertinence
* Recherche **Top-K**

### TP4 et évolutions

Le projet peut être étendu avec des techniques plus avancées de recherche d'information :

* Normalisation morphologique
* Stemming / lemmatisation
* Recherche booléenne
* Amélioration du classement
* Recherche interactive
* Optimisation des performances
* Nouvelles méthodes de représentation des documents

---

## 🧠 Architecture générale

Le fonctionnement du moteur peut être résumé ainsi :

```text
                 COLLECTION DE DOCUMENTS
                           │
                           ▼
                    Prétraitement
                           │
             ┌─────────────┴─────────────┐
             ▼                           ▼
        Tokenisation              Stopwords
             │                           │
             └─────────────┬─────────────┘
                           ▼
                    Index inversé
                           │
                           ▼
                 Vocabulaire global
                           │
             ┌─────────────┴─────────────┐
             ▼                           ▼
        Documents                     Requête
             │                           │
             ▼                           ▼
          TF-IDF                      TF-IDF
             │                           │
             └─────────────┬─────────────┘
                           ▼
                  Similarité cosinus
                           │
                           ▼
                   Classement Top-K
                           │
                           ▼
                    Résultats de recherche
```

---

## 🗂️ Structure du projet

```text
.
├── documents.tsv
├── documentsTP3.tsv
├── indexation.py
├── recherche.py
├── tp1.py
├── tp2.py
├── tp3.py
└── README.md
```

> Les noms des fichiers peuvent varier selon l'organisation utilisée pour chaque TP.

---

## ⚙️ Technologies utilisées

* **Python 3**
* Expressions régulières avec `re`
* Calculs mathématiques avec `math`
* Fichiers texte / TSV
* Structures de données Python
* Algorithmes d'indexation et de recherche d'information

Le projet privilégie une **implémentation simple et compréhensible**, sans dépendre de bibliothèques spécialisées pour les principaux algorithmes étudiés.

---

## 🔍 Fonctionnalités principales

### Prétraitement

Les documents sont transformés avant l'indexation :

```text
Texte original
      ↓
Minuscules
      ↓
Tokenisation
      ↓
Suppression des stopwords
      ↓
Termes utilisés pour l'indexation
```

### Index inversé

Chaque terme est associé aux documents dans lesquels il apparaît.

Exemple :

```text
information
    ├── D1
    ├── D6
    ├── D7
    └── D10
```

L'index enrichi contient également :

```text
terme
 ├── df
 └── postings
       ├── document
       │     └── tf
       └── document
             └── tf
```

---

## 📊 TF-IDF

Le poids d'un terme dans un document est calculé avec :

```text
TF-IDF = (1 + log10(TF)) × IDF
```

avec :

```text
IDF = log10(N / DF)
```

Cette représentation permet de donner davantage d'importance aux termes qui sont fréquents dans un document mais moins présents dans l'ensemble de la collection.

---

## 📐 Modèle vectoriel

Chaque document est représenté par un vecteur correspondant au vocabulaire global.

Par exemple :

```text
D1 = [0, 0.301, 0, 0.602, ...]
D2 = [0.176, 0, 0.477, 0, ...]
```

La requête est représentée dans le même espace vectoriel.

La pertinence entre une requête et un document est ensuite calculée avec la **similarité cosinus**.

```text
                   Requête
                      │
                      ▼
              ┌───────────────┐
              │ Similarité    │
              │   cosinus     │
              └───────────────┘
                 /    |    \
                /     |     \
              D1      D2      D3
              │       │       │
             0.91    0.63    0.27
                \     |     /
                 \    |    /
                  Classement
```

---

## 🚀 Recherche Top-K

Le moteur permet de rechercher plusieurs requêtes et de retourner les documents les plus pertinents.

Exemples de requêtes :

```text
information retrieval model
vector space model
boolean retrieval
search engines ranking
neural information retrieval
```

Les résultats sont classés selon leur score de similarité :

```text
TOP-K RESULTS

Rank    DocID    Score
1       D2       0.812
2       D1       0.654
3       D6       0.421
```

---

## 🖥️ Moteur de recherche interactif

Une version interactive permet également de lancer plusieurs recherches sans reconstruire l'index à chaque requête.

```text
========================================
FIGL SEARCH ENGINE V2
========================================
Documents indexed : 20
Vocabulary size : 87

Query > information retrieval
Top-k (3, 5, 10) > 5
```

Le moteur affiche ensuite les documents correspondant le mieux à la requête avec leur score de pertinence.

---

## ▶️ Installation et exécution

### 1. Cloner le projet

```bash
git clone https://github.com/Omar-khecharem/indexation-recherche-information.git
```

### 2. Accéder au projet

```bash
cd indexation-recherche-information
```

### 3. Vérifier Python

```bash
python --version
```

Python 3 est recommandé.

### 4. Exécuter un TP

Selon l'organisation des fichiers :

```bash
python tp1.py
```

ou :

```bash
python tp2.py
```

ou :

```bash
python tp3.py
```

---

## 📁 Format de la collection

Les documents sont stockés dans des fichiers TSV.

Exemple :

```text
D1	Information retrieval systems use inverted indexes for efficient search
D2	The vector space model represents documents and queries as vectors
D3	Boolean retrieval uses AND OR and NOT operators
D4	TF IDF measures the importance of terms in documents
```

Chaque ligne contient :

```text
ID_DOCUMENT    TEXTE_DU_DOCUMENT
```

---

## 🎯 Objectifs pédagogiques

Ce projet permet de mettre en pratique les notions fondamentales de l'**Information Retrieval** :

* Comprendre le fonctionnement d'un moteur de recherche
* Manipuler une collection documentaire
* Prétraiter du texte
* Construire un index inversé
* Calculer TF, DF et IDF
* Construire des représentations vectorielles
* Comparer une requête avec plusieurs documents
* Classer les résultats par pertinence
* Analyser les performances d'une méthode de recherche
* Comprendre les limites des différentes approches

---

## 📈 Évolution du projet

Le projet suit une progression allant d'une recherche simple vers un moteur de recherche basé sur un modèle vectoriel :

```text
Recherche naïve
      ↓
Prétraitement
      ↓
Index inversé
      ↓
Recherche multi-termes
      ↓
TF / DF / IDF
      ↓
TF-IDF
      ↓
Modèle vectoriel
      ↓
Similarité cosinus
      ↓
Classement Top-K
      ↓
Moteur de recherche interactif
```

Cette progression permet de comprendre pourquoi les moteurs de recherche utilisent des structures d'indexation et des modèles de classement plutôt qu'un simple parcours de tous les documents.

---

## 👨‍💻 Auteur

**Omar Khecharem**

Étudiant en **Génie Logiciel et Systèmes d'Information — FIGL**

**ISIMG — Institut Supérieur d'Informatique et de Multimédia de Gabès**

---

## 📌 Module

**Indexation et Recherche d'Information**

Travaux pratiques — ISIMG

---

## ⭐ Technologies et concepts

```text
Python
│
├── Text Processing
├── Tokenization
├── Stopwords
├── Inverted Index
├── Boolean Retrieval
├── TF / DF / IDF
├── TF-IDF
├── Vector Space Model
├── Cosine Similarity
├── Ranking
└── Top-K Search
```

> Projet réalisé à des fins pédagogiques afin de comprendre et implémenter progressivement les mécanismes fondamentaux d'un système de recherche d'information.

# TP1 - Indexation et Recherche d'Information

## Description

Ce TP porte sur les fondamentaux de l'indexation et de la recherche d'information. Il couvre :

- Recherche naive dans une collection de documents
- Tokenisation et suppression des stopwords
- Construction d'un index inverse
- Recherche par terme et intersection de resultats
- Mesure de performance

## Fichiers

| Fichier | Description |
|---------|-------------|
| `indexation.py` | Script principal contenant toutes les fonctions |
| `documents.tsv` | Collection de 10 documents de test |

## Utilisation

```bash
python indexation.py
```

## Fonctionnalites

1. **Recherche naive** : parcourt tous les documents pour trouver un terme
2. **Tokenisation** : decoupe le texte en mots
3. **Stopwords** : supprime les mots courants (le, la, les, un, une...)
4. **Index inverse** : structure de donnees pour une recherche rapide
5. **Intersection** : combine les resultats de plusieurs termes
6. **Benchmark** : mesure le temps d'execution

## Auteur

Omar - FIGL2

# Guide Git - Commandes Essentielles pour ton projet

## 1. Initialiser un depot local

```bash
git init
```

## 2. Ajouter les fichiers

```bash
git add .                    # Tout ajouter
git add fichier.py           # Un seul fichier
```

## 3. Committer

```bash
git commit -m "description"
```

## 4. Creer un depôt sur GitHub

1. Va sur github.com
2. Clique sur "New repository"
3. Nomme-le (ex: `indexation-tp`)
4. **NE COCHE PAS** "Add a README"
5. Clique "Create repository"
6. Copie l'URL (ex: `https://github.com/Omar/indexation-tp.git`)

## 5. Connecter le local au remote

```bash
git remote add origin https://github.com/TON_UTILISATEUR/indexation-tp.git
```

## 6. Pousser sur GitHub

```bash
git push -u origin master
```

## 7. Workflow pour chaque nouveau TP

```bash
# 1. Creer une branche pour le TP
git checkout -b tp2

# 2. Travailler sur le TP...

# 3. Ajouter et committer
git add .
git commit -m "feat: TP2 - description"

# 4. Pousser la branche
git push -u origin tp2

# 5. Sur GitHub, creer un Pull Request pour merge dans master

# 6. Une fois merge, revenir sur master
git checkout master
git pull origin master
```

## 8. Voir l'historique

```bash
git log --oneline
```

## 9. Voir le statut

```bash
git status
```

## Resume rapide

| Commande | Action |
|----------|--------|
| `git init` | Initialiser le depot |
| `git add .` | Ajouter tout |
| `git commit -m "msg"` | Sauvegarder |
| `git push` | Envoyer sur GitHub |
| `git pull` | Recuperer de GitHub |
| `git checkout -b nom` | Creer une branche |
| `git merge nom` | Fusionner une branche |

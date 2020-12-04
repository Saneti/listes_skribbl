Ce readme sert à expliquer quelques base pour utiliser git. Il n'ira pas du tout dans les détails, et si vous voulez aller plus loin, vous pourrez toujours vous référer à la documentation.
Il sert surtout pour celles et ceux qui voudraient pouvoir modifier des listes et partager de nouvelles listes (et qui ne sont pas familiers avec git).

# Installation :

## Si vous avez déjà git sur votre ordinateur : 
vous pouvez sauter cette étape. (Et probablement tout ce readme ^^)

## Si vous n'êtes pas sûrs : 
ouvrez un terminal (command prompt ou autre), et tapez git fetch. Si l'erreur retournée ressemble à "git is not recgnised as internal command...", vous ne l'avez pas.

## Vous trouverez deux liens pour l'installation de git ci-dessous.
- mac : https://git-scm.com/download/mac
- windows : https://git-scm.com/download/win

# Clonage du répertoire :

- Ouvrez un terminal et déplacez vous dans un répertoire où vous voudriez avoir ces fichiers. Si vous n'êtes pas familier avec command prompt (comme moi ^^), ouvrez un explorateur de fichiers, 
déplacez-vous (ou créez) dans le répertoire, copiez l'adresse complète et copiez-la dans le terminal comme cela :
cd adresse

- Une fois dans le bon répertoire, allez sur https://github.com/Saneti/listes_skribbl (bon vous y êtes déjà si vous lisez ça ^^), cliquez sur code (en vert) et copiez le lien Https.
Retournez dans le terminal et tapez
git clone lien

# Utilisation :

Il est important d'être dans le répertoire avec le .git. Si la première commande retourne l'erreur "not a git repository", faites
- cd listes_skribbl

Pour prendre des nouveaux fichiers ou mettre votre répertoire à jour avec le git en ligne, effectuez les deux commandes
- git fetch 
- git pull

Pour ajouter des fichiers ou des modifications, effectuez les trois commandes à la suite :
- git add .
- git commit -m"très brève explication des modifications ^^"
- git push

On ne se prend pas la tête ici ^^ et on utilise "git add .". Si vous êtes un puriste de git, faites comme vous préférez tant que le résultat est bon ^^.




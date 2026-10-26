# Règles de voix pour Instagram

Ce sont les règles de voix canoniques pour tout le bundle. Chaque skill en
hérite. Les sections « Règles dures » propres à une skill n'ajoutent que des
ajustements liés au format (longueur de légende, nombre de slides, calibrage
des hashtags) et renvoient ici.

## Règles dures

1. **Zéro tiret long (em dash) et zéro tiret moyen (en dash) entre deux
   propositions.** Le caractère en lui-même n'est plus un signe d'IA (les
   modèles 2026 en mettent moins que les humains, et 29 % des légendes
   humaines de notre corpus en contiennent un), mais la densité l'est, et en
   français la règle de ce bundle est simple : aucun, pour ne jamais avoir à
   compter. Remplace par une virgule, deux-points, des parenthèses ou un
   retour à la ligne, jamais par un point. Pas de double tiret (`--`) non
   plus. Le trait d'union des mots composés reste normal.
2. **Utilise `..` ou un retour à la ligne** comme pause douce là où tu aurais
   envie d'un tiret. Ça se lit humain et ça colle à la façon dont les gens
   écrivent vraiment leurs légendes sur Instagram.
3. **Majuscule aux noms de personnes, d'entreprises et de produits** (Stripe,
   Canva, Figma). Un nom de marque en minuscules, ça fait négligé.
4. **Une phrase peut commencer en minuscule.** Les ouvertures en minuscules
   sont natives du registre des légendes Instagram. Les noms à l'intérieur
   gardent toujours leur majuscule.
5. **Un chiffre précis bat un adjectif.** « 11 heures gagnées par semaine »
   bat « un temps fou de gagné ». « 4 200 € en 30 jours » bat « de l'argent
   bien gagné ».
6. **Une idée par légende.** Une légende qui défend trois points se lit comme
   un article de blog. Choisis celle qui gagne l'enregistrement.
7. **Pas de vente forcée.** Instagram enterre les légendes ouvertement
   promotionnelles. Enseigne ou raconte une histoire, puis indique l'étape
   suivante une seule fois.

## Marqueurs de vocabulaire (notés en densité)

Compte-les par paragraphe. Un, c'est du français ; deux, c'est limite
(signale-le dans le rapport, laisse les mots) ; trois dans un même paragraphe,
ça se lit IA et tout le paragraphe est réécrit (voir `ig-humanizer` V3).
Le jeu durable 2026 (véritable, authentique en adjectif passe-partout,
incontournable, indispensable, solution, holistique, à 360°, booster, sublimer,
élever, révolutionner, exploiter pleinement, libérer ton potentiel) compte au
même titre que les tournures administratives plus anciennes :
- booster, sublimer, élever, révolutionner, exploiter pleinement, libérer ton
  potentiel, plonger dans, optimiser, propulser, accompagner vers, fédérer
- en effet, par ailleurs, force est de constater, il est essentiel de, il est
  crucial, permettre de, dans le cadre de, n'hésite pas à
- écosystème, paradigme, univers, aventure, voyage (au sens de « ton
  voyage »), holistique, à 360°, véritable, authentique, solution

## Toujours interdit (une seule occurrence suffit, quelle que soit la densité)

Ces tournures sont retirées dès qu'on les voit. Ce sont des ponts de
révélation, des parallélismes négatifs, des phrases mortes ou de la sincérité
jouée, pas du vocabulaire :
- « Ce n'est pas juste X, c'est Y », « Pas seulement X, mais Y »
- « Dans un monde où », « à l'ère de », « dans un monde en constante évolution »
- « Le résultat ? », « La suite ? » (le pont de révélation)
- « game-changer », « level up », « next level », « must-have », « deep dive »
- « lien en bio » en remplissage (seulement quand il y a un vrai lien et une
  vraie raison)
- Les annonces de sincérité en ouverture ou en pivot : « soyons honnêtes »,
  « on ne va pas se mentir », « je vais être honnête », « franchement ? »,
  « sans filtre », « opinion impopulaire : » sur un avis qui est en fait
  populaire. Énonce le fait à plat à la place.

## Style natif Instagram

- **La première ligne, c'est tout le travail.** Instagram cache tout ce qui
  dépasse environ 125 caractères derrière « plus ». Si la ligne 1 ne gagne pas
  le tap, le reste n'est pas lu.
- **Les retours à la ligne sont de la ponctuation.** L'espace blanc entre des
  lignes courtes contrôle le rythme et rend la légende survolable. Un pavé de
  texte se fait scroller.
- **Les emoji font partie du registre, avec retenue.** 0 à 3 par légende,
  placés pour aérer le texte ou marquer une liste, jamais saupoudrés. Une
  légende poudrée de 12 emoji se lit comme un compte spam ou de l'IA.
- **Les hashtags, c'est du calibrage, pas du volume.** 3 à 5 tags bien
  calibrés battent 30 tags au hasard en 2026 (voir `hashtag-strategy.md`).
  Mets-les en fin de légende ou en premier commentaire, jamais au milieu d'une
  phrase.

## Longueur

- **Plafond de légende : 2 200 caractères.** Seuls les 125 premiers environ
  s'affichent avant « plus », donc mets le hook devant. La plupart des bonnes
  légendes font entre 150 et 1 500 caractères ; long, ça va très bien quand ça
  enseigne ou raconte une histoire qui vaut le scroll.
- **Une légende de carrousel peut être courte** parce que les slides portent
  la charge. Un post à image seule s'appuie plus fort sur la légende.
- **Légende de reel : serrée.** La vidéo est le hook ; la légende ajoute le
  contexte et la raison d'enregistrer ou de partager en une ligne ou deux.

## Structure

- **Mets le hook devant**, en première ligne (avant le pli). Énonce la
  récompense, la tension ou le chiffre d'entrée de jeu.
- **Termine sur un atterrissage, pas sur une relance morte.** « Vous en
  pensez quoi ? » est mort. Une question précise, une invitation à
  enregistrer qui nomme la raison (« enregistre pour ton prochain
  lancement »), ou une ligne de chute tranchante font toutes mieux.
- **Carrousels :** la slide 1 est le hook, la dernière slide est la récompense
  plus la demande d'enregistrement ou d'abonnement. Voir `hook-formulas.md` et
  la skill de planification de carrousel.

## Anti-patterns

- Une légende qui redit l'évidence (« Le marketing, c'est tellement important
  aujourd'hui »).
- L'appât à engagement générique (« double tape si tu es d'accord »,
  « commente OUI »).
- Les ouvertures usées : « Parlons de.. », « Voilà le truc : », « Spoiler : »,
  « Petit rappel : », « POV : » sur quelque chose qui n'est pas un POV.
- Les triades empilées ou creuses (« plus vite, moins cher, mieux ») et le
  schéma « Pas de X. Pas de Y. Juste Z. » ; une triade naturelle avec des
  éléments concrets, ça passe.
- Les lignes d'un seul mot pour faire du drame.
- Une première ligne qui a besoin de la ligne 2 pour avoir un sens (le pli la
  mange).
- 20 hashtags et plus entassés en haut de la légende.
- Des lignes EN CAPITALES pour l'intensité. Porte l'intensité par le choix des
  mots.

## Note sur l'algorithme

Le classement Instagram de 2026 s'appuie sur **les envois par portée**
(partages à des amies et en story) et sur **les enregistrements** comme
signaux les plus forts qu'un contenu mérite d'être diffusé, devant les likes.
Avant de poster, vérifie : est-ce que ça donne à une spectatrice une raison de
l'envoyer à une amie précise, ou de l'enregistrer pour plus tard ? Si ça ne
gagne qu'un like passif, affûte.

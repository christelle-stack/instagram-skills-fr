---
name: ig-hashtag-strategist
description: "Construit un jeu de hashtags Instagram calibré pour un post, selon la réalité 2026 où 3 à 5 tags bien choisis battent 30 tags au hasard. Classe chaque tag en niche (moins de 50k posts), intermédiaire (50k à 500k) ou large (500k et plus), puis assemble un mélange de 2-3 niche, 1-2 intermédiaires, 0-1 large dans lequel un petit ou moyen compte peut vraiment se classer, en accord avec le contenu du post et en rotation pour éviter les schémas de spam. Déclencheurs : choisis mes hashtags, quels hashtags pour ce post, trouve-moi des hashtags pour ce reel ou ce carrousel. Ne sert pas à écrire la légende elle-même (utilise ig-caption-writer)."
---

# Stratège hashtags Instagram

Choisis 3 à 5 hashtags qui aident vraiment, calibrés pour que le post puisse
se classer. Le mur de 30 tags est mort : en 2026 les hashtags fonctionnent
comme des étiquettes de sujet, et un petit compte se classe dans des tags de
niche, pas dans des tags larges à un million de posts. Cette skill construit
le jeu calibré.

## Quand l'utiliser

- L'utilisatrice a une légende, un carrousel ou un reel et a besoin de hashtags
- L'utilisatrice poste encore 20 à 30 tags génériques et veut l'approche 2026
- L'utilisatrice veut des tags calibrés sur la taille où son compte peut vraiment se classer

## Le modèle : la taille, pas le volume

La **taille** d'un tag, c'est son nombre total de posts. La stratégie est un
mélange pour que le post se classe dans les petits tags tout en touchant les
plus gros.

| Palier | Nombre de posts | Rôle | Usage |
|---|---|---|---|
| Niche | moins de 50k | là où un petit ou moyen compte se classe vraiment, pendant des heures | 2 à 3 |
| Intermédiaire | 50k à 500k | assez d'audience, concurrence battable | 1 à 2 |
| Large | 500k et plus | une touche d'étiquette de catégorie, classé pendant quelques minutes | 0 à 1 |

**Par défaut : 3 à 5 au total.** Raisonnement complet dans `../../references/hashtag-strategy.md`.

## Étapes

1. **Récupérer le post.** La légende, le sujet du carrousel ou le thème du
   reel, plus l'audience visée et la taille approximative du compte (pour que
   la répartition niche/intermédiaire colle).
2. **Extraire les sujets.** Dégage les 3 à 5 vrais sujets du post (le thème,
   la communauté de niche, le format, le résultat).
3. **Générer des candidats par palier.** Pour chaque sujet, propose des
   candidats niche, intermédiaires et larges. Les tags de niche sont précis et
   longue traîne (`#notionpourfreelances`) ; les tags larges sont des mots
   courants isolés (`#marketing`).
4. **Calibrer chaque candidat.** Estime le palier d'après la spécificité
   (aucune API ne donne les compteurs, donc utilise ton jugement et dis à
   l'utilisatrice de vérifier les nombres dans la recherche de l'app). Signale
   les tags manifestement génériques ou à risque de signalement
   (`#follow4follow`, `#like4like`) à écarter.
5. **Assembler le jeu.** 2 à 3 niche + 1 à 2 intermédiaires + 0 à 1 large,
   3 à 5 au total. Laisse tomber le large si rien ne colle vraiment. Chaque tag
   doit correspondre au contenu.
6. **Vérifier la correspondance.** Rejette tout tag populaire mais hors sujet ;
   un décalage entraîne mal le moteur de recommandation et baisse la portée.
7. **Faire tourner.** Dis à l'utilisatrice de varier le jeu selon le sujet, pas
   de réutiliser un seul bloc sur chaque post (des jeux identiques sur beaucoup
   de posts sentent l'automatisation).
8. **Livrer.** Le jeu de 3 à 5, chaque tag avec son palier et une ligne de
   pourquoi, plus la consigne de placement (fin de légende ou premier
   commentaire).

## Format de sortie

```
Jeu calibré (4 tags) :
  #notionpourfreelances    niche            la communauté exacte que ce post sert
  #organisationfreelance   niche            longue traîne, peu de renouvellement, classable
  #astucesproductivite     intermédiaire    audience chaude et pertinente, battable
  #notion                  large            étiquette de catégorie, une touche

Placement : fin de la légende ou premier commentaire. Fais tourner les tags de niche selon le sujet.
```

## Règles dures

Règles de voix globales : voir le `SKILL.md` racine, section Règles de voix.
Règles supplémentaires propres à cette skill :

- 3 à 5 tags au total. Ne sors jamais un bloc de 30 tags.
- Chaque tag doit décrire le contenu réel. Pas de tag populaire mais hors sujet.
- Au plus un tag large ; laisse-le tomber si rien ne colle.
- Signale et retire les tags de ferme à engagement (`#follow4follow`,
  `#like4like`) et tout tag connu comme signalé.
- Les hashtags vont en fin de légende ou en premier commentaire, jamais au milieu d'une phrase.
- Fais tourner les jeux selon le sujet ; ne donne pas à l'utilisatrice un seul bloc à coller pour toujours.

## Anti-schémas (la skill refusera)

- Sortir 20 à 30 hashtags.
- Un « pack de hashtags viraux » fait de tags larges génériques.
- Des tags qui ne correspondent pas au post pour courir après une audience plus grosse.
- Cacher 30 tags derrière des points pour « faire propre ».
- Des jeux tout en large dans lesquels un petit compte ne peut pas se classer.

## Ressources

- `../../references/hashtag-strategy.md` : le modèle de calibrage 2026 complet et la recette
- `../../references/algorithm-heuristics.md` : pourquoi ce sont les envois et les enregistrements, pas les flux de hashtags, qui font la portée

## Skills liées

- `ig-caption-writer` : écrit la légende à laquelle les hashtags s'attachent
- `ig-carousel-planner` : le carrousel dont la légende porte le jeu
- `ig-content-planner` : faire tourner les thèmes de tags sur une semaine

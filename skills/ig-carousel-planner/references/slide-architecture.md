# Architecture des slides de carrousel

Les colonnes vertébrales par formule et les règles du texte sur image que
`ig-carousel-planner` utilise. Un carrousel fait 2 à 10 slides. Conçois-le pour
le cadre portrait 4:5, celui qui remplit le plus d'écran.

## La colonne vertébrale universelle

| Slide | Rôle | Texte sur image |
|---|---|---|
| 1 (hook) | promesse + boucle ouverte | une grande idée, 6 à 12 mots, un chiffre s'il colle |
| 2 | la valeur la plus forte | le meilleur point, en tête |
| 3 à N-1 | un point chacune | court, autonome, lisible en 2 secondes |
| N (récompense) | résumé à enregistrer + une seule demande | le récap en une slide, puis enregistrer / s'abonner |

Le taux de swipe décroît avec la profondeur, donc l'ordre de la valeur compte
plus que le nombre. Mets le meilleur point en slide 2 ou 3, jamais en slide 10.

## Règles du texte sur image

- **Une idée par slide.** Si une slide a besoin de deux pensées, coupe-la en deux.
- **Lisible en 2 secondes.** Gros texte, peu de mots. La slide est une affiche,
  pas un paragraphe. Le détail va dans la légende.
- **Numérote les slides** quand le format est une liste (slide 2 = « 1. », etc.)
  pour que la boucle ouverte (« la plupart ratent la 4 ») soit payée.
- **Cohérence visuelle.** Même police, mêmes marges, même couleur d'accent sur
  toutes les slides pour que l'ensemble se lise comme un tout.
- **Zéro tiret long dans le texte sur image.** Une slide n'en a jamais besoin.
  Remplace-le par deux-points ou un retour à la ligne, jamais par un point. Le
  trait d'union dans un mot composé reste normal.

## IG5 : Carrousel liste (objectif : enregistrements)

```
Slide 1 : {N} {choses} qui {récompense}. (la plupart ratent la {k})
Slide 2 : 1. {élément} + un exemple concret
Slide 3 : 2. {élément} + exemple
...
Slide N-1 : {N}. {élément} + exemple
Slide N : la liste récapitulée en une slide + « enregistre ça pour vraiment t'en servir »
```

Place l'élément le plus surprenant en position 1 ou 2 de la liste, pas en
dernier.

## IG6 : Transformation avant/après (objectif : enregistrements, abonnements)

```
Slide 1 : {l'après, avec un chiffre ou un visuel frappant}
Slide 2 : d'où ça partait (l'avant) : la boucle ouverte, c'est l'écart
Slides 3 à N-1 : les étapes exactes, une par slide
Slide N : le résultat redit + « abonne-toi pour le système {sujet} complet »
```

L'écart avant/après entre les slides 1 et 2 est le moteur du swipe. Les étapes
doivent être assez concrètes pour être faites dès demain.

## IG7 : Carrousel casse-mythes (objectif : partages)

```
Slide 1 : {N} mythes sur {sujet} qui te coûtent {perte précise}
Slides 2 à N-1 : « Mythe : {croyance} » puis « Vérité : {ce qui marche} »
Slide N : le recadrage en une ligne + « envoie ça à quelqu'un qui croit encore au numéro 1 »
```

L'invitation à envoyer sur la dernière slide est tout l'intérêt ; un
casse-mythes, ça s'envoie.

## IG8 : Méthode à piquer (objectif : enregistrements)

```
Slide 1 : la méthode {nommée} que j'utilise pour {résultat}
Slides 2 à N-1 : une partie de la méthode par slide, avec le pourquoi
Slide N : toute la méthode en une slide (l'objet qu'on enregistre) + invitation à enregistrer
```

Le résumé en une slide, c'est ce que les gens enregistrent. Rends-le autonome.

## Repères pour le nombre de slides

| Contenu | Slides |
|---|---|
| Une liste ou une méthode serrée | 6 à 8 |
| Un ensemble pédagogique plus riche ou une transformation | 8 à 10 |
| Moins de 4 vrais points | publie plutôt une image seule |

Ne gonfle jamais à 10. Une idée en 5 points, c'est un carrousel en 5 points
(7 slides avec le hook et la récompense), pas un carrousel gonflé à 10.

## Légende associée

La légende peut être courte pour un carrousel parce que les slides portent
l'essentiel. Elle doit : reprendre le hook pour le pli « plus », ajouter une
ligne de contexte, porter le CTA et accueillir les 3 à 5 hashtags calibrés. Voir
`../../../references/hashtag-strategy.md`.

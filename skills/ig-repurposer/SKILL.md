---
name: ig-repurposer
description: "Recycle un contenu existant en post Instagram natif. Prend un post LinkedIn, un article de blog, un script YouTube, un tweet ou un fil X et le reconstruit pour Instagram : un texte long devient un carrousel ou une légende, avec un nouveau hook avant le pli des 125 caractères et les traces d'autres plateformes retirées (@-identifiants X, lien en bio), livré prêt à coller sur validation. Utilise-la pour « transforme ce post LinkedIn en carrousel » ou pour adapter n'importe quel contenu d'une autre plateforme à Instagram. Pas pour écrire à partir de zéro (utilise ig-caption-writer ou ig-carousel-planner), ni pour auditer un brouillon (ig-humanizer --mode audit)."
---

# Recycleuse de contenu Instagram

Transforme quelque chose que tu as déjà fait en post qui a l'air né sur
Instagram. Recycler, ce n'est pas copier-coller. Un post qui a cartonné sur
LinkedIn ou un fil qui a décollé sur X meurt sur Instagram si tu le colles tel
quel : mauvais hook, mauvais contenant, mauvais rythme, pas de média, et des
traces (« lien en bio », @-identifiants, murs de hashtags) qui crient
« ça vient d'ailleurs ».

Cette skill transforme, elle ne génère pas. Elle lit ta source, garde l'idée et
reconstruit la livraison pour Instagram.

## Quand l'utiliser

- « Transforme ce post LinkedIn en carrousel / légende Instagram »
- « Recycle mon article de blog / ma newsletter / mon script YouTube pour Instagram »
- « Ce fil a marché sur X, adapte-le pour Instagram »
- « J'ai une idée brute dans un autre format, rends-la native ici »

Pas pour un brouillon partant d'une page blanche (utilise `ig-caption-writer`
pour une légende seule, `ig-carousel-planner` pour un carrousel slide par
slide) ni pour relire un brouillon déjà pensé pour Instagram (utilise
`ig-humanizer --mode audit`).

## Comment ça marche

**Profil de voix d'abord (tous les brouillons).** Si `../../references/voice-profile.md` contient `rempli : oui`, charge-le et respecte l'empreinte de voix de l'utilisatrice, ses règles dures et son style de CTA et de lien du début à la fin. S'il n'est pas rempli, signale une seule fois que `ig-humanizer --mode profile` peut apprendre sa voix à partir de quelques posts, puis continue avec les règles de voix génériques.

**N'invente jamais les détails concrets.** Les règles ci-dessous réclament un chiffre précis, une date et une entité nommée, parce que c'est ce qui sépare un vrai post d'un post généré. Prends-les dans ce que l'utilisatrice a réellement dit dans cette conversation. **N'invente pas un chiffre, une date, un nom de cliente ou un résultat, et ne transforme pas une affirmation vague en chiffre plausible.** Si elle n'a rien de concret pour un temps fort, demande-lui une fois, et si elle n'a toujours rien, retire l'affirmation plutôt que de la décorer. Un chiffre inventé publié, c'est un rectificatif ; un chiffre manquant, c'est seulement un post un peu moins fort.

1. **Prends la source.** N'importe quel format : un post, un paragraphe, un
   script, une légende, une transcription, une liste à puces, un lien à lire.
   Demande la source, le média dont l'utilisatrice dispose (Instagram exige une
   image ou une vidéo) et l'objectif (enregistrements / partages / commentaires /
   abonnements) s'il n'est pas donné.
2. **Extrais la colonne vertébrale.** Retire l'enveloppe de la plateforme
   d'origine et sors la seule affirmation, la seule histoire ou le seul chiffre
   qui mérite d'être gardé. La plupart des recyclages échouent parce qu'ils
   gardent les mots au lieu du propos.
3. **Choisis le contenant.** Une affirmation ou un chiffre -> une légende seule.
   Un enseignement, une liste ou une construction -> un carrousel, un point par
   slide (confie la structure à `ig-carousel-planner`, de la slide hook à la
   slide finale). Une vidéo longue -> un carrousel qui livre la récompense, pas
   un résumé.
4. **Refais le hook pour le pli.** Instagram cache tout ce qui dépasse environ
   125 caractères derrière « plus ». La première ligne (ou la slide hook) doit
   porter tout le punch à elle seule. Le hook de la source survit presque
   jamais ; écris une nouvelle première ligne avec une formule Instagram 2026
   (voir `../../references/hook-formulas.md`), choisie selon l'objectif.
5. **Réajuste le format.** Corps de légende facile à parcourir, lignes courtes,
   de l'air entre les temps forts. Carrousel : une idée par slide, pas de pavé.
   Coupe le tissu de liaison de la source ; Instagram récompense la récompense
   placée en tête.
6. **Retire les traces d'autres plateformes.** Enlève le « lien en bio » hérité
   d'ailleurs, le « abonne-toi à la chaîne », le « lire la suite ci-dessous », les
   @-identifiants X qui n'existent que là-bas, et tout raclement de gorge du
   type « comme je l'écrivais sur LinkedIn ». Un post recyclé ne doit pas
   avouer qu'il l'est.
7. **Rappel du média.** Instagram refuse les posts sans média. Confirme l'image,
   la vidéo ou le jeu de slides que l'utilisatrice va joindre. Une légende sans
   média n'est pas publiable.
8. **Hashtags à la fin.** Confie le sujet à `ig-hashtag-strategist` ou applique
   toi-même un jeu calibré de 3 à 5 tags (voir
   `../../references/hashtag-strategy.md`). Place-les en un seul bloc à la FIN de
   la légende ou en premier commentaire, jamais en mur au milieu du texte.
9. **Passage humanizer.** Lance `ig-humanizer` V3 sur le résultat : vocabulaire
   IA 2026 par densité de paragraphe, tout tiret long (zéro dans ce bundle,
   jamais remplacé par un point), triades empilées en règle de trois,
   ouvertures passe-partout et ponts de révélation. Ne corrige qu'un paragraphe
   qui sonne plat et mécanique ; ne fabrique jamais de la variance. Garde les
   vrais chiffres et les entités nommées de la source.
10. **Carte de validation.** Montre : la correspondance source -> Instagram
    (ce qui est devenu quoi), le contenant (légende seule ou carrousel de N
    slides), la formule utilisée, le hook (signale s'il dépasse 125 caractères),
    le jeu de hashtags, le média que l'utilisatrice doit joindre, l'objectif
    principal.
11. **Livraison.** Sur validation, donne le texte validé dans un bloc à
    copier-coller (la légende, et pour un carrousel le texte de chaque slide
    numéroté dans l'ordre). Indique le média à préparer : l'image, la vidéo ou
    les slides du carrousel. Rappelle qu'Instagram refuse tout post sans média ;
    l'utilisatrice colle le texte et publie elle-même dans l'app Instagram.

## Règles d'ajustement natif (source -> Instagram)

- **Post LinkedIn -> Instagram :** un post long devient un carrousel (un point
  par slide) ou, si c'est une seule affirmation tranchée, une légende seule.
  LinkedIn tolère l'échauffement ; Instagram, non. Le hook LinkedIn est
  généralement trop long ; réécris-le pour le pli des 125 caractères.
- **Blog / newsletter -> carrousel :** transforme la structure en slides, un
  point par slide, la slide hook d'abord, la slide finale en dernier. Ne colle
  pas tout l'article dans une seule légende.
- **Script YouTube -> carrousel de la récompense :** commence par ce que la
  vidéo apporte, pas par son intro. Construis le carrousel autour de « voilà ce
  que j'ai trouvé », pas d'un résumé scène par scène.
- **Tweet / fil -> légende ou carrousel :** un tweet seul devient une légende ;
  un fil devient un carrousel, un tweet par slide avec son propre micro-point.
  Retire les @-identifiants X et la numérotation du fil.

## Règles dures

Règles de voix globales : voir la section Règles de voix du `SKILL.md` racine.
Règles propres à cette skill :

- Garde **l'affirmation et les faits** de la source intacts. Recycler change la
  livraison, jamais le sens ni les chiffres.
- La nouvelle première ligne (ou la slide hook) doit arrêter le scroll à elle
  seule avant le pli des 125 caractères. Si elle a besoin de la deuxième ligne,
  réécris-la.
- Ne colle jamais la source telle quelle pour la raccourcir. Reconstruis le hook
  et le rythme à partir de la colonne vertébrale.
- Un chiffre précis là où la source en offre un. Garde-le.
- 3 à 5 hashtags calibrés en un seul bloc à la fin, jamais 30 et jamais au
  milieu de la légende.
- Le média est obligatoire. Ne présente jamais une légende recyclée comme
  publiable sans rappeler à l'utilisatrice de joindre l'image, la vidéo ou les
  slides.
- Pas de vente forcée du produit de l'utilisatrice. Une mention naturelle
  maximum.

## Anti-patterns (la skill refuse)

- Copier-coller la source avec quelques retouches (ce n'est pas du recyclage).
- Garder les traces de la plateforme d'origine (« lien en bio », « abonne-toi à
  la chaîne », @-identifiants X, numérotation du fil).
- Un hook qui n'a de sens qu'après le pli des 125 caractères.
- Un mur de hashtags au milieu de la légende au lieu d'un bloc à la fin.
- Présenter une légende sans média comme prête à publier.
- Une première ligne TOUT EN MAJUSCULES pour l'intensité. Porte-la par le choix
  des mots.
- Un tiret long ou un tiret moyen entre deux propositions, où que ce soit.
- Des ponts de révélation « Le résultat ? » / « Voilà le truc : » et des
  empilements staccato ajoutés pendant la réécriture.
- Listes en règle de trois sans rien de concret.
- « plonger dans », « libérer ton potentiel », « booster », « révolutionner », « incontournable », « il est essentiel de ».
- Raclement de gorge méta (« J'avais d'abord publié ça sur… »).

## Ressources

- `../../references/hook-formulas.md` : les 10 squelettes de formules Instagram pour refaire le hook
- `../../references/algorithm-heuristics.md` : les règles de classement Instagram 2026 (pli, horaires, signaux)
- `../../references/hashtag-strategy.md` : la recette des 3 à 5 hashtags calibrés

## Skills liées

- `ig-caption-writer` : écrire une légende seule à partir de zéro
- `ig-carousel-planner` : structurer un carrousel slide par slide (la recycleuse lui confie les constructions longues)
- `ig-hashtag-strategist` : construire le jeu de hashtags calibré
- `ig-humanizer` : nettoyer les signes d'IA, plus `--mode audit` pour relire le résultat

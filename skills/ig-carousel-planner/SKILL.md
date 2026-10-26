---
name: ig-carousel-planner
description: "Planifie un carrousel Instagram slide par slide, jusqu'à 10 slides, avec une slide hook qui ouvre une boucle, des slides de valeur qui mettent la promesse en tête et une slide finale qui gagne l'enregistrement et l'abonnement. Choisit une formule carrousel 2026 (liste, avant/après, casse-mythes, méthode) selon l'objectif (enregistrements, partages, abonnements), rédige le texte de chaque slide plus la légende, puis livre le tout prêt à coller avec la liste des slides à préparer. Utilise-la pour « planifie un carrousel de 8 slides » ou pour structurer n'importe quel post multi-slides. Pas pour une légende d'image seule (utilise ig-caption-writer)."
---

# Planificatrice de carrousels Instagram

Planifie un carrousel qu'on swipe jusqu'au bout et qu'on enregistre. Tout se joue
sur la slide 1 (le hook qui gagne le swipe) et sur la dernière slide (la
récompense qu'on enregistre). Cette skill cartographie chaque slide, écrit le
texte à afficher sur l'image et rédige la légende qui encadre l'ensemble.

## Quand l'utiliser

- L'utilisatrice veut transformer un sujet ou des notes en carrousel multi-slides
- Elle a une liste, une méthode ou une transformation à enseigner
- Elle veut une structure slide par slide, pas seulement une légende

## Formules utilisées par cette skill (formats carrousel)

| Code | Formule | Objectif principal | Idéale pour |
|---|---|---|---|
| IG5 | Carrousel liste | enregistrements | une liste pédagogique numérotée, un élément par slide |
| IG6 | Transformation avant/après | enregistrements, abonnements | la preuve d'un résultat avec les étapes entre les deux |
| IG7 | Carrousel casse-mythes | partages | corriger les croyances de ta niche |
| IG8 | Méthode à piquer | enregistrements | une méthode nommée et réutilisable |

Squelettes complets dans `../../references/hook-formulas.md`.

## Architecture des slides (la colonne vertébrale en 10 slides)

Un carrousel fait 2 à 10 slides. La colonne vertébrale fiable :

| Slide | Rôle |
|---|---|
| **1 (hook)** | la promesse + une boucle ouverte (« la plupart ratent la 4 »). Gagne le swipe. Gros texte, une idée. |
| **2 et 3** | la valeur la plus forte, en tête (le taux de swipe décroît avec la profondeur). |
| **4 à N-1** | un point par slide, chacune autonome, chacune lisible en 2 secondes. |
| **N (récompense)** | le résumé en une slide (l'objet qu'on enregistre) + une seule demande (enregistrer / s'abonner). |

6 à 10 slides, c'est la zone idéale pour un carrousel pédagogique. Moins de 4,
c'est en général une image seule. Voir `references/slide-architecture.md` pour
les colonnes vertébrales par formule.

## Étapes

**Profil de voix d'abord (tous les brouillons).** Si `../../references/voice-profile.md` contient `rempli : oui`, charge-le et respecte l'empreinte de voix de l'utilisatrice, ses règles dures et son style de CTA et de lien du début à la fin. S'il n'est pas rempli, signale une seule fois que `ig-humanizer --mode profile` peut apprendre sa voix à partir de quelques posts, puis continue avec les règles de voix génériques.

**N'invente jamais les détails concrets.** Les règles ci-dessous réclament un chiffre précis, une date et une entité nommée, parce que c'est ce qui sépare un vrai post d'un post généré. Prends-les dans ce que l'utilisatrice a réellement dit dans cette conversation. **N'invente pas un chiffre, une date, un nom de cliente ou un résultat, et ne transforme pas une affirmation vague en chiffre plausible.** Si elle n'a rien de concret pour un temps fort, demande-lui une fois, et si elle n'a toujours rien, retire l'affirmation plutôt que de la décorer. Un chiffre inventé publié, c'est un rectificatif ; un chiffre manquant, c'est seulement un post un peu moins fort.

1. **Rassemble les entrées.** Sujet, la liste / méthode / transformation, public
   visé et objectif (enregistrements / partages / abonnements).
2. **Choisis la formule.** Utilise le tableau des objectifs ; propose 2 ou 3
   formules qui collent et laisse-la choisir.
3. **Fixe le nombre de slides.** Adapte-le au contenu réel (6 à 10 en général).
   Ne gonfle jamais pour atteindre 10 ; les lectrices sentent le remplissage et
   décrochent.
4. **Écris la slide 1.** La promesse plus la boucle. Gros texte sur l'image, une
   seule idée. Mets un chiffre en tête s'il y en a un qui colle.
5. **Cartographie les slides de valeur.** Place le point le plus fort en slide 2
   ou 3. Un point par slide, chacune capable de tenir seule. Rédige le texte sur
   image de chacune (court : il doit se lire en 2 secondes sur un cadre 4:5).
6. **Écris la slide finale.** Un récapitulatif en une slide qui vaut
   l'enregistrement à lui seul, plus une seule demande (enregistre-le /
   abonne-toi pour la suite).
7. **Écris la légende.** La légende soutient le carrousel (elle peut être
   courte), reprend le hook pour le pli et porte les hashtags. Confie-les à
   `ig-hashtag-strategist` ou applique le jeu calibré de 3 à 5 tags.
8. **Passage humanizer** sur le texte des slides et la légende. Traque le
   vocabulaire IA 2026 par densité (par slide, par paragraphe de légende),
   supprime tout tiret long (zéro sur une slide, zéro dans la légende ; jamais
   remplacé par un point), casse les triades empilées et les ponts de
   révélation. Les slides sont courtes par nature : ne coupe ni ne gonfle jamais
   une slide pour le rythme. Règles canoniques : `ig-humanizer` V3.
9. **Carte de validation.** Montre : la formule, le plan slide par slide avec le
   texte de chacune, la légende, le jeu de hashtags, l'objectif principal et un
   rappel que l'utilisatrice fournit 2 à 10 images (que des images, pas de
   mélange) dans cet ordre.
10. **Livraison.** Sur validation, donne la légende validée et le texte de
    chaque slide, numéroté dans l'ordre, dans un bloc à copier-coller. Indique le
    média à préparer : les 2 à 10 images des slides, toutes au même format,
    dans l'ordre du plan. Rappelle qu'Instagram refuse tout post sans média :
    l'utilisatrice monte ses slides, puis les publie elle-même dans l'app
    Instagram avec la légende.

## Règles dures

Règles de voix globales : voir la section Règles de voix du `SKILL.md` racine.
Règles propres à cette skill :

- La slide 1 est une promesse avec une boucle ouverte, jamais un simple titre.
- La valeur en tête sur les slides 2 et 3 ; n'enterre jamais le meilleur point à
  la fin.
- Un point par slide, lisible en 2 secondes sur un cadre portrait 4:5.
- 2 à 10 slides, pas plus. Ne gonfle jamais pour tomber sur un chiffre rond.
- Que des images, pas de mélange (Instagram refuse un carrousel image + vidéo).
- La dernière slide doit gagner l'enregistrement avec un résumé en une slide et
  une seule demande.

## Anti-patterns (la skill refuse)

- Une slide 1 qui n'est qu'un titre, sans promesse ni boucle.
- Un carrousel de 10 slides gonflé à partir d'une idée en 4 points.
- Le point le plus fort gardé pour la dernière slide.
- Trois CTA concurrents sur la slide finale.
- Mélanger des images et une vidéo dans un même carrousel.
- Des pavés de texte sur image illisibles en un swipe.
- Un tiret long ou un tiret moyen sur une slide ou dans la légende, des grappes de vocabulaire IA, des règles de trois empilées ou creuses.
- Des « Le résultat ? » en pont de révélation et des empilements staccato ajoutés pour le punch.

## Ressources

- `../../references/hook-formulas.md` : les formules carrousel (IG5 à IG8) avec leurs squelettes
- `../../references/algorithm-heuristics.md` : classement des carrousels et règles de swipe 2026
- `../../references/hashtag-strategy.md` : la recette des 3 à 5 hashtags calibrés
- `references/slide-architecture.md` : colonnes vertébrales par formule et règles du texte sur image

## Skills liées

- `ig-caption-writer` : quand l'idée est une image seule, pas un carrousel
- `ig-hashtag-strategist` : construire le jeu de hashtags calibré
- `ig-humanizer` : nettoyer le texte des slides et la légende
- `ig-hook-extractor` : décortiquer un carrousel que tu admires

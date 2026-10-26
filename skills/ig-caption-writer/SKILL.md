---
name: ig-caption-writer
description: "Rédige une légende Instagram avec le hook dans les 125 premiers caractères, un corps facile à parcourir et un seul CTA clair, à partir d'une formule de hook 2026 choisie selon l'objectif (enregistrements, partages, commentaires, abonnements). Passe le texte à l'humanizer et, sur validation, le livre prêt à coller avec le média à préparer. Utilise-la pour « écris la légende de mon reel », « écris-moi une légende Instagram sur X » ou pour légender une image seule. Pas pour un carrousel slide par slide (utilise ig-carousel-planner) ni pour auditer un brouillon (utilise ig-humanizer --mode audit)."
---

# Rédactrice de légendes Instagram

Écris une légende qui gagne le tap et l'enregistrement. Instagram cache tout ce
qui dépasse environ 125 caractères derrière « plus », donc le hook fait tout le
travail dans la première ligne. Cette skill place ce hook en tête, garde un
corps facile à parcourir et termine sur un seul appel à l'action clair.

## Quand l'utiliser

- L'utilisatrice dit « écris-moi une légende Instagram sur X »
- Elle a une image seule ou un reel et il lui faut la légende qui va autour
- Elle veut un hook plus tranchant pour un brouillon qu'elle a déjà
- Elle veut une légende prête à coller dans l'app avec son média

## Formules utilisées par cette skill (formats légende d'abord)

| Code | Formule | Objectif principal | Idéale pour |
|---|---|---|---|
| IG1 | Résultat chiffré d'abord | enregistrements | un résultat à la précision bizarre + une promesse « pique-la » |
| IG2 | Vérité à contre-courant | partages | une affirmation tranchée, défendable, à rebours du conseil courant |
| IG3 | Scène du quotidien | commentaires | un moment précis que tout le monde connaît, sans préambule |
| IG4 | Confession en mini-récit | commentaires, abonnements | une vraie histoire à la première personne, avec un coût |

Squelettes complets dans `../../references/hook-formulas.md`. Pour les carrousels
(IG5 à IG8), utilise `ig-carousel-planner` ; pour les reels (IG9 et IG10), le hook
vit dans la vidéo, et cette skill écrit la légende qui l'accompagne.

### Choisis d'abord selon l'objectif

| Objectif | Va vers |
|---|---|
| Enregistrements | IG1 |
| Partages | IG2 |
| Commentaires | IG3, IG4 |
| Abonnements | IG4 |

## Étapes

**Profil de voix d'abord (tous les brouillons).** Si `../../references/voice-profile.md` contient `rempli : oui`, charge-le et respecte l'empreinte de voix de l'utilisatrice, ses règles dures et son style de CTA et de lien du début à la fin. S'il n'est pas rempli, signale une seule fois que `ig-humanizer --mode profile` peut apprendre sa voix à partir de quelques posts, puis continue avec les règles de voix génériques.

**N'invente jamais les détails concrets.** Les règles ci-dessous réclament un chiffre précis, une date et une entité nommée, parce que c'est ce qui sépare un vrai post d'un post généré. Prends-les dans ce que l'utilisatrice a réellement dit dans cette conversation. **N'invente pas un chiffre, une date, un nom de cliente ou un résultat, et ne transforme pas une affirmation vague en chiffre plausible.** Si elle n'a rien de concret pour un temps fort, demande-lui une fois, et si elle n'a toujours rien, retire l'affirmation plutôt que de la décorer. Un chiffre inventé publié, c'est un rectificatif ; un chiffre manquant, c'est seulement un post un peu moins fort.

1. **Rassemble les entrées.** Sujet, angle, média (image seule ou reel), public
   visé et objectif (enregistrements / partages / commentaires / abonnements).
2. **Choisis la formule.** Utilise le tableau des objectifs pour présélectionner,
   puis propose 2 ou 3 formules qui collent aussi au sujet et laisse-la choisir.
3. **Écris le hook (125 premiers caractères).** Il doit poser la promesse, la
   tension ou le chiffre avant le pli « plus » et se suffire à lui-même.
4. **Écris le corps.** Lignes courtes, de l'air entre les temps forts, une seule
   idée. Enseigne ou raconte ce que le hook a promis. Reste sous 2 200
   caractères.
5. **Écris un seul CTA.** Une invitation précise à enregistrer ou à envoyer
   (« enregistre ça pour ton prochain lancement », « envoie ça à la copine qui
   fait encore le numéro 2 »), une vraie question ou une seule prochaine étape.
   Jamais « qu'en penses-tu ? ».
6. **Ajoute les hashtags.** Confie le sujet à `ig-hashtag-strategist` ou applique
   toi-même le jeu calibré de 3 à 5 tags (voir `../../references/hashtag-strategy.md`).
   Place-les à la fin ou précise qu'ils vont en premier commentaire.
7. **Passage humanizer.** Traque le vocabulaire IA 2026 par densité de
   paragraphe, supprime tout tiret long (zéro dans ce bundle, remplacé par une
   virgule, deux-points, des parenthèses ou un retour à la ligne, jamais par un
   point), casse les triades empilées, les ouvertures passe-partout et les ponts
   de révélation. Ne corrige qu'un paragraphe qui sonne plat et mécanique ;
   ne fabrique jamais de la variance ni des lignes d'un mot pour le drame.
   Ajoute un chiffre à la précision bizarre avec un référent nommé, ou une entité
   nommée, quand l'affirmation le permet. Règles canoniques : `ig-humanizer` V3.
8. **Audit optionnel.** Appelle `ig-humanizer --mode audit` pour une vérification
   réussi / échoué.
9. **Carte de validation.** Montre : la formule utilisée, le hook (signale s'il
   dépasse 125 caractères), la légende complète, le nombre de caractères, le jeu
   de hashtags, l'objectif principal et le média que l'utilisatrice doit fournir.
10. **Livraison.** Sur validation, donne la légende validée dans un bloc à
    copier-coller, indique le média à préparer (l'image ou la vidéo, pour un reel
    la vidéo elle-même) et rappelle qu'Instagram refuse tout post sans média.
    L'utilisatrice colle le texte et joint son média directement dans l'app
    Instagram.

## Règles dures

Règles de voix globales : voir la section Règles de voix du `SKILL.md` racine.
Règles propres à cette skill :

- Les 125 premiers caractères doivent arrêter le scroll à eux seuls. Réécris tout
  hook qui a besoin de la deuxième ligne pour avoir du sens.
- Une idée par légende. Deux idées, c'est deux posts.
- Un chiffre précis là où l'affirmation le permet.
- 3 à 5 hashtags calibrés, jamais 30. 0 à 3 emojis, placés avec intention.
- Le média est obligatoire. Ne présente jamais une légende comme publiable sans
  rappeler à l'utilisatrice de joindre l'image ou la vidéo.
- Pas de vente forcée. Une mention naturelle de la prochaine étape, maximum.

## Anti-patterns (la skill refuse)

- Un hook qui n'a de sens qu'après le pli.
- Un tiret long ou un tiret moyen entre deux propositions, où que ce soit.
- Ouvertures « Parlons de… », « Voilà le truc : », « Spoiler : », « Petit rappel : » ; « Le résultat ? » ou « La suite ? » comme pont de révélation.
- Candeur annoncée (« Soyons honnêtes », « On ne va pas se mentir », « POV : » sur quelque chose qui n'est pas un POV) sans fait daté derrière.
- Empilements staccato (« Pas de X. Pas de Y. Juste Z. ») et lignes d'un mot ajoutées pour le drame.
- 20 à 30 hashtags entassés en haut.
- Bait d'engagement (« double tap si tu es d'accord », « commente OUI »).
- Listes en règle de trois sans rien de concret.
- « plonger dans », « libérer ton potentiel », « sublimer », « booster », « révolutionner », « incontournable », « n'hésite pas à », « il est essentiel de », « dans un monde où », « véritable », « solution ».
- Gonfler une idée d'une ligne pour qu'elle ait l'air consistante.

## Ressources

- `../../references/hook-formulas.md` : les 10 formules Instagram (IG1 à IG4 sont les formats légende d'abord)
- `../../references/algorithm-heuristics.md` : les règles de classement Instagram 2026
- `../../references/hashtag-strategy.md` : la recette des 3 à 5 hashtags calibrés
- `references/caption-checklist.md` : la liste de contrôle et d'ajustement par légende

## Skills liées

- `ig-carousel-planner` : quand l'idée est un carrousel slide par slide
- `ig-hashtag-strategist` : construire le jeu de hashtags calibré
- `ig-humanizer` : nettoyeur de signes d'IA, plus `--mode audit` pour la relecture
- `ig-hook-extractor` : décortiquer le hook d'un post que tu admires

---
name: ig-profile-optimizer
description: "Audite et réécrit un profil Instagram de bout en bout pour 2026 : photo de profil, champ NOM recherchable lesté d'un mot-clé, @identifiant, bio (150 caractères : valeur plus sujet plus preuve), lien aligné sur l'objectif, catégorie, stories à la une, grille des 9 premiers posts et jusqu'à 3 posts épinglés. Se déclenche sur « revois mon profil », « corrige ma bio », « optimise mes stories à la une », « audit de profil ». Toute la décision de s'abonner se joue sur l'en-tête du profil. Pas pour écrire des légendes (utilise ig-caption-writer)."
---

# Optimisatrice de profil Instagram

Audite les neuf parties d'un profil Instagram (photo, champ NOM, @identifiant,
bio, lien, catégorie, stories à la une, grille des 9 premiers posts, posts
épinglés) à l'aune de ce qui transforme vraiment une visiteuse en abonnée en
2026, puis réécrit chaque partie qui en a besoin. Sur Instagram, toute la
décision de s'abonner se joue sur l'en-tête du profil plus les deux ou trois
premières rangées de la grille : photo, NOM, bio, lien, puis la grille d'un coup
d'œil. C'est ça que cette skill répare.

## Quand l'utiliser

- L'utilisatrice colle son profil Instagram ou son @identifiant et demande un audit
- « Corrige ma bio », « réécris ma bio Instagram », « c'est quoi les bonnes stories à la une »
- Elle commence à publier sérieusement et veut que le profil soit à la hauteur du contenu
- N'importe laquelle de ces phrases : « revois mon profil », « optimise mes stories à la une », « audit de profil »

Pas pour écrire des légendes (utilise `ig-caption-writer`) ni planifier un
carrousel (utilise `ig-carousel-planner`).

## Entrées

- URL du profil / @identifiant (ou une capture de l'en-tête du profil + les premières rangées de la grille)
- Objectif : **gagner des abonnées** / **vendre un produit** / **trouver des clientes** / **asseoir son expertise**. Le CTA de la bio, la cible du lien et les posts épinglés changent selon l'objectif
- Optionnel : ses posts les plus performants, pour choisir les épinglés et l'ordre de la grille

## Sortie

1. **Tableau de score** (9 parties, réussi / à retravailler / échoué)
2. **Corrections prioritaires** classées par impact (champ NOM, bio et épinglés d'abord)
3. **Réécritures Avant -> Après** pour chaque partie qui échoue
4. **Plan des stories à la une** (couvertures, ordre, noms) et **choix de grille + d'épinglés** argumentés

## Étapes

1. **Prise d'infos.** Récupère l'état du profil + l'objectif. Note le type de
   compte (personnel / créatrice / professionnel), puisque les comptes
   professionnels et créatrice débloquent la catégorie et le tableau de bord
   professionnel.
2. **Note les 9 parties** d'après le tableau de score ci-dessous.
3. **Leste le champ NOM avec un mot-clé.** Le champ NOM (pas le @identifiant) est
   ce que la recherche Instagram indexe. Règle-le sur `Vrai prénom + le sujet
   que les gens tapent` (par ex. « Léa Marchand | Croissance Instagram »), en
   30 caractères. C'est la correction SEO la plus rentable de tout le profil.
4. **Réécris la bio (150 caractères).** Formule : `qui tu aides + de quoi tu
   parles + une preuve ou un détail précis`. Commence par la valeur, pas par
   l'intitulé de poste. Pas d'ouverture cliché « J'aide X à Y » sauf si la suite
   est précise. Les retours à la ligne et un emoji d'ancrage passent ; une
   tempête d'emojis, non. Tiens en 150.
5. **Règle le lien.** Un seul lien aligné sur l'objectif (offre / newsletter /
   prise de rendez-vous). S'il en faut plusieurs, une page de liens unique, pas
   une page d'accueil nue. Les comptes professionnels et créatrice peuvent
   désormais ajouter plusieurs liens, mais celui du haut porte toujours le clic.
6. **Règle la catégorie** (comptes professionnels / créatrice). Une seule
   étiquette claire qui colle à la niche, affichée sous le NOM. Elle renforce la
   bio ; elle ne la répète pas.
7. **Planifie les stories à la une.** 4 à 6 à la une, classées de gauche à droite
   selon la prochaine question de la visiteuse : Par ici / Preuves / Offre / FAQ
   / À propos. Couvertures personnalisées dans un style cohérent, noms courts
   d'un mot qui tiennent sans être tronqués. Les 3 ou 4 premières sont ce qu'une
   nouvelle visiteuse voit avant de scroller.
8. **Répare la grille des 9 premiers posts.** Les neuf premières tuiles sont la
   vitrine. Vise une lecture d'un coup d'œil, un aspect cohérent (couleur,
   cadrage ou style de texte) et un mix qui montre de l'étendue sans chaos.
   Réordonne ou remplace les tuiles faibles du haut ; la grille se juge comme un
   ensemble, pas tuile par tuile.
9. **Choisis les posts épinglés (jusqu'à 3).** Les trois meilleures preuves de
   ce qu'une nouvelle abonnée va recevoir, alignées sur l'objectif : un post
   très performant, une offre claire et un post de présentation / « à qui ça
   s'adresse ». Les épinglés passent avant l'ordre de la grille, donc sers-t'en.
10. **Vérifie la photo.** Visage net, qui remplit le cadre, récent, fort
    contraste sur fond uni. Elle s'affiche en tout petit, donc le détail est
    perdu ; le contraste, non.
11. **Livre le comparatif avant/après** + le test de l'en-tête : lis seulement la
    photo, le NOM, la bio, le lien et la première rangée de la grille, et
    demande-toi « est-ce qu'une inconnue s'abonnerait rien qu'avec ça ? ».

## Tableau de score en neuf parties

| # | Partie | Critères de réussite (2026) |
|---|------|----------------------|
| 1 | **Photo de profil** | Visage net qui remplit le cadre, récent, fort contraste, fond uni, lisible en petit |
| 2 | **Champ NOM** | Vrai prénom + un mot-clé recherchable que les gens tapent, en 30 caractères (c'est ce champ qui est indexé, pas le @identifiant) |
| 3 | **@identifiant** | Court, mémorisable, cohérent avec la marque, sans chiffres ni tirets bas si possible |
| 4 | **Bio** | Valeur + sujet + preuve en 150 caractères ; pas d'ouverture cliché ; commence par ce qu'une abonnée y gagne ; pas de tempête d'emojis |
| 5 | **Lien** | Un seul, aligné sur l'objectif ; une page de liens s'il en faut plusieurs ; celui du haut porte le clic |
| 6 | **Catégorie** | Réglée (professionnel / créatrice), une seule étiquette de niche claire qui renforce la bio |
| 7 | **Stories à la une** | 4 à 6, classées selon la prochaine question de la visiteuse, couvertures personnalisées cohérentes, noms courts non tronqués |
| 8 | **Grille des 9 premiers** | Aspect cohérent, lisible d'un coup d'œil, montre de l'étendue ; tuiles faibles du haut réordonnées ou remplacées |
| 9 | **Posts épinglés** | Jusqu'à 3 présents, chacun une preuve forte alignée sur l'objectif (pas des posts récents au hasard) |

## Exemples de bio (150 caractères)

| Objectif | Avant | Après |
|---|---|---|
| Trouver des clientes | « Coach business certifiée ✨ Passionnée par l'entrepreneuriat féminin 🚀 » | « Je t'aide à passer de 2 000 € à 5 000 € par mois sans vendre ton âme. 127 solopreneuses accompagnées depuis Lyon. Appel découverte ⬇ » |
| Vendre un produit | « Pâtisserie artisanale 🍰 Fait maison avec amour » | « Des pâtisseries vegan livrées à Bruxelles en 48 h. 1 200 commandes en 2025, zéro rappel. Commande de la semaine ⬇ » |
| Gagner des abonnées | « Prof de yoga 🧘‍♀️ Montréal » | « 10 min de yoga par jour pour les dos qui bossent assis. Chaque matin à 7 h, heure de Montréal. Commence par la séance épinglée » |

Dans chaque « Après » : qui est aidée, de quoi parle le compte, un chiffre ou un
lieu précis, et une seule prochaine étape. Les chiffres viennent de
l'utilisatrice, jamais de toi.

## Règles dures

Règles de voix globales : voir la section Règles de voix du `SKILL.md` racine.
Règles propres à cette skill :

- L'en-tête doit passer le test de l'en-tête : une inconnue qui lit seulement la
  photo + le NOM + la bio + le lien + la première rangée de la grille doit savoir
  à qui ça s'adresse et avoir envie de s'abonner.
- Commence la bio par le bénéfice pour la lectrice, pas par l'intitulé de poste
  de l'utilisatrice.
- Le champ NOM porte toujours un mot-clé recherchable ; ne le laisse jamais en
  simple prénom.
- Garde chaque réécriture dans les limites de la plateforme (bio 150, NOM 30).
  Ne livre jamais une bio tronquée ni un nom de story à la une qui se coupe.
- Les stories à la une et la grille se jugent comme des ensembles ; corrige
  l'ordre et la cohérence, pas seulement des éléments isolés.
- Zéro tiret long dans la bio (une bio de 150 caractères n'en a jamais besoin ;
  utilise un point, une virgule ou un retour à la ligne). Pas de « booster »,
  « sublimer », « révolutionner », « incontournable », « libérer ton potentiel ».

## Skills liées

- `ig-caption-writer` : écrire les légendes que le profil et la grille optimisés vont accueillir
- `ig-hook-extractor` : trouver un hook digne d'être épinglé dans un post qui a déjà marché
- `ig-content-planner` : planifier la cadence qui remplit la grille et les stories à la une
- `ig-humanizer --mode audit` : auditer la bio et les légendes épinglées avant de publier

---
name: ig-content-planner
description: "Génère un plan de contenu Instagram hebdomadaire à partir d'un thème, d'un public et de piliers de contenu. Produit un mix jour par jour de reels, carrousels, images seules et stories, chacun avec une formule de hook, un angle, une heure de publication et un objectif principal, plus un objectif hebdo d'enregistrements et de partages (le levier 2026), une cadence de stories et un contrôle d'équilibre entre enregistrements, partages, commentaires et abonnements. Utilise-la pour « planifie ma semaine » ou « qu'est-ce que je poste cette semaine ». Pas pour rédiger une seule légende (utilise ig-caption-writer) ni un seul carrousel (utilise ig-carousel-planner)."
---

# Planificatrice de contenu Instagram

Produit un plan Instagram hebdomadaire construit autour d'une discipline de
piliers et du mix de formats qu'Instagram récompense : les reels pour la portée,
les carrousels pour les enregistrements, les stories pour la relation. Le plan
fixe un objectif hebdo d'enregistrements et de partages, parce que les envois
par portée et les enregistrements sont les leviers de 2026.

## Quand l'utiliser

- L'utilisatrice demande « planifie ma semaine sur Instagram » ou « qu'est-ce que je poste cette semaine »
- Elle veut sortir de la publication au coup par coup et installer un rythme
- Avant une semaine de lancement (le plan aligne un pilier produit)

## Entrées

- **Thème** (optionnel) : par ex. « lancement de notre formation design »
- **Description du public :** par ex. « designers juniors, personnes en reconversion »
- **Mix de piliers** (optionnel) : par défaut 40 % Pédagogie / 30 % Récit /
  20 % Engagement / 10 % Promotion
- **Cadence de publication** (optionnel) : par défaut 4 à 5 posts de feed par semaine + stories quotidiennes
- **Échantillons de voix** (optionnel) : d'anciennes légendes pour calibrer la voix

## Sortie

Un plan en Markdown avec :

### Calendrier sur 7 jours

| Jour | Format | Pilier | Formule | Angle en une ligne | Objectif | Heure |
|---|---|---|---|---|---|---|
| Lun | Reel | Pédagogie | IG9 Reel rupture de pattern | « tu postes tes reels au pire moment » | partages | 12h00 |
| Mar | Carrousel | Pédagogie | IG5 Carrousel liste | « 7 erreurs de portfolio » | enregistrements | 11h30 |
| Mer | Série de stories | Engagement | sondage + question | « quelle mise en page gagne ? » | commentaires | 19h00 |
| Jeu | Carrousel | Récit | IG6 Transformation avant/après | « de mes premiers 0 € à mes premiers 4 000 € » | abonnements | 11h00 |
| Ven | Image seule | Engagement | IG3 Scène du quotidien | « ouvrir Canva pour un seul visuel » | commentaires | 13h00 |
| Sam | Reel | Pédagogie | IG10 Reel « comment j'ai fait » | « comment je monte un reel en 20 min » | enregistrements | 10h00 |
| Dim | Série de stories | Promotion | repartage + lien | « les inscriptions sont ouvertes » | abonnements | 18h00 |

(La skill remplit les vrais angles à partir du thème. Les stories tournent chaque
jour en dessous des posts de feed. Heures en heure de Paris.)

### Objectif hebdo d'enregistrements

- Fixe une **cible concrète d'enregistrements + partages** pour la semaine (le
  levier principal). Heuristique par défaut : au moins 3 posts de feed de la
  semaine sont des formats qui font enregistrer (IG1, IG5, IG6, IG8, IG10) et au
  moins 2 sont des formats qui font envoyer (IG2, IG7, IG9).
- Suis les enregistrements et les partages comme métrique de tête, pas les likes.

### Cadence quotidienne de stories

- 2 à 4 stories par jour : coulisses, un sticker sondage ou question, et au moins
  un repartage d'un post de feed récent (un signal équivalent à un envoi qui
  pousse le post vers les abonnées qui l'ont raté).
- Les stories approfondissent la relation avec les abonnées ; elles ne courent
  pas après la portée hors abonnées.

### Contrôle d'équilibre hebdo

- [ ] Mix de formats : au moins 2 reels (portée), au moins 2 carrousels (enregistrements), stories chaque jour
- [ ] Au moins 3 posts qui font enregistrer et 2 posts qui font envoyer
- [ ] Au moins 1 vrai post de récit à la première personne (créer la confiance, gagner des abonnements)
- [ ] Aucun pilier au-dessus de 50 % des posts de feed de la semaine
- [ ] Aucune formule répétée plus de deux fois dans la semaine
- [ ] Pilier Promotion : 1 à 2 posts maximum
- [ ] Mix d'objectifs réparti entre enregistrements, partages, commentaires, abonnements

## Mix d'objectifs (équilibrer la semaine)

Chaque formule gagne un signal principal. Une semaine qui n'est que de
l'enregistrement ou que du quotidien partagé sonne fabriquée. Répartis les
objectifs :

| Objectif | Formules | Cible hebdo |
|---|---|---|
| Enregistrements | IG1, IG5, IG6, IG8, IG10 | au moins 3 (le levier de tête) |
| Partages | IG2, IG7, IG9 | au moins 2 |
| Commentaires | IG3, IG4 | au moins 1 |
| Abonnements | IG4, IG6, IG8 | au moins 1 |

## Règles

- **La régularité bat la fréquence.** 4 à 5 posts de feed de qualité par semaine
  avec des stories quotidiennes battent un déversement quotidien de remplissage.
  Ne gonfle pas pour atteindre un nombre.
- **Les reels pour la portée, les carrousels pour les enregistrements, les
  stories pour la relation.** Utilise la bonne surface pour le bon travail.
- **Les reels peuvent tourner plus souvent** que les carrousels sans lasser,
  parce que chacun touche un nouveau public hors abonnées.
- **Meilleurs créneaux :** en semaine 11h à 13h et 19h à 21h (heure de Paris),
  plus le dimanche soir. Vérifie les statistiques de l'utilisatrice quand elles
  sont disponibles.
- **Pilier Promotion : 1 à 2 posts par semaine maximum.** En abuser enterre la
  portée.
- **Une formule par créneau, variée sur la semaine.** N'empile pas trois
  carrousels IG5.

## Correspondance formule -> pilier

| Pilier | Formules à privilégier |
|---|---|
| Pédagogie | IG5 Carrousel liste, IG8 Méthode à piquer, IG10 Reel « comment j'ai fait », IG1 Résultat chiffré d'abord |
| Récit | IG4 Confession en mini-récit, IG6 Transformation avant/après |
| Engagement | IG3 Scène du quotidien, IG9 Reel rupture de pattern, stickers de story |
| Promotion | IG6 (des résultats qui sous-entendent le produit), IG1 (tes propres données) |

## Étapes

1. Rassemble les entrées. Demande le thème, le public et les préférences de
   piliers s'ils ne sont pas fournis.
2. Vérifie que le mix de piliers fait 100 % ; alerte si un pilier dépasse 50 %.
3. Pour chaque jour, choisis : le format (reel / carrousel / image / story), le
   pilier, la formule (sans trop la répéter), l'angle, l'heure de publication
   (fuseau horaire du public) et l'objectif.
4. Fixe l'objectif hebdo enregistrements + partages et la cadence quotidienne
   de stories.
5. Lance le contrôle d'équilibre hebdo et le contrôle du mix d'objectifs ;
   signale ce qui manque.
6. Rends le tout en Markdown, plus un JSON optionnel pour import.

## Exemple

Voir `references/example-week.md` pour un plan sur 7 jours rempli.

## Fichiers

- `SKILL.md` : ce fichier
- `references/example-week.md` : plan sur 7 jours travaillé
- `references/pillars-framework.md` : la discipline des piliers Instagram expliquée

## Skills liées

- `ig-caption-writer` : rédiger chaque légende d'image seule à partir du plan
- `ig-carousel-planner` : rédiger chaque carrousel à partir du plan
- `ig-hashtag-strategist` : faire tourner des jeux de hashtags calibrés sur la semaine
- `ig-hook-extractor` : étudier les posts des concurrentes pendant la planification

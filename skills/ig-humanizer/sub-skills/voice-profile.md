# Sous-skill : construire ou mettre à jour le Profil de voix et de marque

Construit ou rafraîchit `../../../references/voice-profile.md` pour que chaque
skill d'écriture de ce bundle rédige dans la vraie voix de l'utilisatrice au
lieu d'une voix « humaine » générique. Fonctionne avec n'importe quel agent
(Claude Code, Codex, OpenClaw) : le chemin de base n'a besoin que des textes
de l'utilisatrice collés dans la conversation. Un token de lecture (Apify) est
un accélérateur optionnel, jamais obligatoire.

## Quand ça se déclenche

- L'utilisatrice dit « construis mon profil de voix », « apprends ma voix »,
  « apprends comment j'écris », ou lance `ig-humanizer --mode profile`.
- À proposer aussi la première fois qu'une skill d'écriture tourne et trouve
  `rempli : non`.

## Entrées (une seule suffit)

1. **Échantillons collés (défaut portable).** Demande 3 à 6 vrais posts
   Instagram de l'utilisatrice. Ça suffit : pas de token, pas d'historique.
2. **Assistée par la couche de lecture (optionnel).** Si un token Apify est
   configuré, ou si le connecteur MCP Apify est branché, récupère l'activité
   récente de l'utilisatrice via la couche de lecture du bundle comme
   échantillons supplémentaires, en plus de ceux collés.
3. **Manuel.** L'utilisatrice peut aussi simplement énoncer sa niche, ses
   règles et ses liens.

## Étapes

1. Réunir au moins 3 vrais échantillons de l'écriture de l'utilisatrice.
2. Extraire l'empreinte de voix des échantillons, pas de suppositions : rythme
   des phrases, ouvertures récurrentes, habitudes de ponctuation, vocabulaire
   favori, mots qu'elle évite, comportement avec les emojis et les hashtags.
3. Déduire la niche, la cliente idéale et les piliers des sujets des
   échantillons ; confirmer plutôt que deviner.
4. Capturer les règles dures et le style de CTA et de lien que les
   échantillons révèlent ou que l'utilisatrice énonce.
5. Écrire `../../../references/voice-profile.md` : remplir les sections 1 à 5,
   copier mot pour mot les 2 à 4 lignes les plus fortes dans « Exemples
   signature », et régler le bloc Statut sur `rempli : oui`,
   `source: <pasted|read-layer|manual>`, `updated: <aujourd'hui>`.
6. Montrer le profil rempli pour validation avant de l'enregistrer ; dire à
   l'utilisatrice que chaque skill d'écriture s'y alignera désormais
   automatiquement.

## Règles dures

- Construis l'empreinte à partir des VRAIS échantillons de l'utilisatrice. N'invente jamais une voix.
- Préserve ses manies (une expression fétiche, un rythme inhabituel). C'est
  tout l'intérêt ; seul le nettoyage générique des tics d'IA s'applique plus
  tard aux brouillons, pas au profil.
- Avec seulement 3 échantillons, dis que c'est un premier passage ; suggère de
  relancer après 10 posts ou plus.
- Ne mets jamais dans le fichier quelque chose que l'utilisatrice n'a pas fourni.

## Liés

- Le profil rempli est lu par les skills d'écriture de ce bundle avant de rédiger.
- À relancer chaque fois que la voix ou le cap de l'utilisatrice change.

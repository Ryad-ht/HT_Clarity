# 📦 Étude de cas fictive — Optimisation logistique pour un transporteur indien

## 🎯 Objectif

Améliorer la performance logistique d’un transporteur basé en Inde grâce à l’exploitation de ses données de livraison, historiquement stockées mais jamais analysées.

---

## 🧩 Contexte simulé

Une société de transport :

- 📂 Stocke toutes ses données sous format `.csv`, sans les exploiter.
- 🚚 Subit des retards fréquents de livraison.
- 🛠️ Ne dispose d’aucun outil pour suivre ses fournisseurs ou optimiser ses trajets.

**Conséquences simulées :**

- 📉 Impossible d’identifier les fournisseurs inefficaces
- 🚛 Trajets non optimisés, augmentant la consommation
- 🕒 Aucun indicateur clair sur la ponctualité

---

## 🛠️ Solution proposée : Audit + Dashboard interactif

1. **Nettoyage & structuration** des données dans Python
2. **Export** vers `.csv` propre
3. **Import dans Tableau Public**
4. **Création de 4 visualisations clés** dans un **dashboard interactif**

---

## 📊 Visualisations réalisées

| Visualisation                         | Utilité métier |
|--------------------------------------|----------------|
| 📈 Nombre de trajets par mois        | Identifier les pics d’activité et la saisonnalité |
| ⏱️ Pourcentage de livraisons à l’heure | Suivre la ponctualité sur la durée |
| 🚛 Distance moyenne par type de véhicule | Repérer les véhicules sur-utilisés ou inefficaces |
| 🏆 Top 10 fournisseurs (avec alerte sur les inconnus) | Identifier les partenaires les plus actifs (et les plus opaques) |

---

## ✅ Avant / Après

| Avant (situation initiale)         | Après (résultats obtenus)                    |
|-----------------------------------|----------------------------------------------|
| ❌ Aucune visualisation           | ✅ Dashboard complet, interactif et filtrable |
| ❌ Aucune analyse fournisseur     | ✅ Classement des top fournisseurs            |
| ❌ Données brutes non utilisées   | ✅ Structure nettoyée & réutilisable          |
| ❌ Retards invisibles             | ✅ Pourcentage de ponctualité par mois        |

---

## 🧪 Technologies utilisées

- `Python` (pandas, openpyxl) : nettoyage & transformation
- `Tableau Public` : visualisation et dashboard final
- `Excel` : structuration initiale et simulation brute

---

## 🔗 Résultat final

👉 [Lien vers le dashboard sur Tableau Public](https://public.tableau.com/app/profile/...) *(à remplacer par ton vrai lien)*

---

## 📝 Pourquoi cette étude fictive ?

Cette étude a été menée pour illustrer un cas d'usage concret dans notre offre de services "Data Clarity". Elle permet de :

- Prouver notre capacité à transformer un fichier brut en outil décisionnel
- Fournir un exemple visuel à nos prospects sans NDA
- Servir de support à notre pack d’audit + dashboard interactif

---

👋 *Projet réalisé dans le cadre de notre offre de service data pour TPE/PME. Contact : [tonemail@exemple.com]*

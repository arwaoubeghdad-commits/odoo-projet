Arwa Oubeghdad G2 5IIR
# odoo-docker

Projet Odoo 16 exécuté avec Docker (Odoo + PostgreSQL) et contenant un module personnalisé `gestion_bibliotheque`.

## Description
Ce dépôt fournit un environnement prêt à l’emploi pour lancer **Odoo 16** via **Docker Compose** et tester/développer un module Odoo.
Le module **Gestion de Bibliothèque** (nom technique : `gestion_bibliotheque`) illustre les concepts principaux d’Odoo :

- modèles (Python) dans `addons/gestion_bibliotheque/models/`
- vues, menus et actions (XML) dans `addons/gestion_bibliotheque/views/`
- droits d’accès (CSV) dans `addons/gestion_bibliotheque/security/`

## Technologies
- Odoo 16
- PostgreSQL 13
- Docker / Docker Compose
- Python / XML

## Structure du projet
- `docker-compose.yml` : services Odoo + PostgreSQL
- `config/odoo.conf` : configuration Odoo (si utilisée)
- `addons/` : modules personnalisés
  - `gestion_bibliotheque/` : module principal

## Prérequis
- Docker Desktop (Windows)
- Docker Compose (inclus avec Docker Desktop)

## Lancement
Dans le dossier du projet :

```bash
docker compose up -d
```

Accéder à Odoo :
- http://localhost:8069

## Installation / mise à jour du module
1. Ouvrir Odoo
2. Activer le mode développeur (ex: ajouter `?debug=1` à l’URL)
3. Aller dans **Apps**
4. Cliquer sur **Update Apps List** (mettre à jour la liste)
5. Rechercher `gestion_bibliotheque`
6. Cliquer sur **Install** ou **Upgrade**

## Notes
- Si des modifications de code ne s’affichent pas, redémarrer Odoo et faire un **Upgrade** du module.

## Auteur
EMSI

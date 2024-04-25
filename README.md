# Reservation-system-tkinter

<img width="630" alt="Reservation-System-Tkinter" src="https://github.com/bilalfatian/Reservation-system-tkinter/assets/92918987/ade936dc-b19c-47a5-b803-cd2cec730775">


Ce projet vise à mettre en place une application de gestion pour une agence, spécialisée dans la location de maisons de vacances sur des îles. Actuellement, la gestion des données se fait de manière manuelle, ce qui rend difficile l'extraction rapide et efficace d'informations cruciales. Pour remédier à cette situation, une base de données et des interfaces graphiques seront mises en place afin d'améliorer le service clientèle.

# Objectif du Projet
L'objectif principal est de concevoir et développer un système d'information permettant à l'agence de gérer efficacement ses réservations de maisons de vacances. Cela implique la création d'un modèle entité-association, d'un schéma relationnel, de contraintes d'intégrité, de tables de base de données, ainsi que le développement d'interfaces graphiques pour l'insertion, la recherche, la modification et la suppression de données.

# Contenu du Projet
## Modèle Entité-Association (E/A):
- Identifie les entités telles que Maison, Client et Réservation.
- Définit les associations entre ces entités, telles que la relation entre Client et Réservation.
- Spécifie les attributs pour chaque entité, comme le nom de la maison, l'adresse du client, etc.
- Définit les clés d'identification pour chaque entité, par exemple, l'identifiant de la maison comme clé primaire.
## Schéma Relationnel:
- Crée une représentation du modèle E/A en termes de tables relationnelles.
- Identifie les clés primaires et étrangères pour chaque table.
- Contraintes d'Intégrité:
Spécifie les règles pour restreindre les valeurs possibles des attributs.
Exemples de contraintes incluent les numéros de semaine valides pour les réservations et le tarif minimum par chambre pour les loyers.
## Tables de Base de Données:
- Crée toutes les tables nécessaires en tenant compte des contraintes définies.
- Assurez-vous que la base de données rejette les opérations invalides, telles que l'introduction d'un numéro de semaine invalide.
## Interfaces Graphiques:
- Développe des interfaces conviviales pour l'insertion, la recherche, la modification et la suppression de données.
- Les interfaces permettent aux utilisateurs d'ajouter de nouveaux clients, maisons de vacances, de rechercher des informations pertinentes, etc.
# Technologies Utilisées
- Base de données: SQLite
- Langage de programmation: Python
- Bibliothèques: Pandas, NumPy, Tkinter

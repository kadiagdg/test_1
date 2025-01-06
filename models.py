#models.py
from sqlalchemy import create_engine, Column, Integer, String, Boolean, BigInteger, TIMESTAMP, ForeignKey
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

# Table User
class User(Base):
    __tablename__ = 'users'

    id = Column(BigInteger, primary_key=True)
    name = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    actif = Column(Boolean, nullable=False)  # 0 = actif, 1 = inactif
    phone = Column(String(20), nullable=True)  # Nouvelle colonne

    # Relations
    projets = relationship('Projet', back_populates='user')
    services = relationship('Service', back_populates='user')
    tchat = relationship('Tchat', back_populates='user')


# Table Projet
class Projet(Base):
    __tablename__ = 'projets'

    id = Column(BigInteger, primary_key=True)
    name = Column(String(255), nullable=False)
    description = Column(String(1000), nullable=True)
    created_at = Column(TIMESTAMP, nullable=True)
    updated_at = Column(TIMESTAMP, nullable=True)

    # Clé étrangère pour lier à l'utilisateur
    user_id = Column(BigInteger, ForeignKey('users.id'), nullable=False)

    # Relation avec la table User
    user = relationship('User', back_populates='projets')
    media = relationship('Media', back_populates='projet')


# Table Service
class Service(Base):
    __tablename__ = 'services'

    id = Column(BigInteger, primary_key=True)
    name = Column(String(255), nullable=False)
    description = Column(String(1000), nullable=True)

    # Clé étrangère pour lier à l'utilisateur
    user_id = Column(BigInteger, ForeignKey('users.id'), nullable=False)

    # Relation avec la table User
    user = relationship('User', back_populates='services')
    media = relationship('Media', back_populates='service')


# Table Media
class Media(Base):
    __tablename__ = 'media'

    id = Column(BigInteger, primary_key=True)
    file_path = Column(String(255), nullable=False)
    file_type = Column(String(50), nullable=False)  # Par exemple : image, vidéo, etc.

    # Clé étrangère pour lier à un projet ou service
    projet_id = Column(BigInteger, ForeignKey('projets.id'), nullable=True)
    service_id = Column(BigInteger, ForeignKey('services.id'), nullable=True)

    # Relations avec les tables Projet et Service
    projet = relationship('Projet', back_populates='media')
    service = relationship('Service', back_populates='media')


# Table Acceuil
class Acceuil(Base):
    __tablename__ = 'acceuil'

    id = Column(BigInteger, primary_key=True)
    title = Column(String(255), nullable=False)
    content = Column(String(1000), nullable=False)
    created_at = Column(TIMESTAMP, nullable=True)
    updated_at = Column(TIMESTAMP, nullable=True)


# Table Footer
class Footer(Base):
    __tablename__ = 'footer'

    id = Column(BigInteger, primary_key=True)
    content = Column(String(1000), nullable=False)
    created_at = Column(TIMESTAMP, nullable=True)
    updated_at = Column(TIMESTAMP, nullable=True)


# Table Webinaire
class Webinaire(Base):
    __tablename__ = 'webinaire'

    id = Column(BigInteger, primary_key=True)
    title = Column(String(255), nullable=False)
    description = Column(String(1000), nullable=False)
    date = Column(TIMESTAMP, nullable=False)


# Table Atelier
class Atelier(Base):
    __tablename__ = 'atelier'

    id = Column(BigInteger, primary_key=True)
    title = Column(String(255), nullable=False)
    description = Column(String(1000), nullable=False)
    date = Column(TIMESTAMP, nullable=False)


# Table AlbumPhoto
class AlbumPhoto(Base):
    __tablename__ = 'album_photo'

    id = Column(BigInteger, primary_key=True)
    title = Column(String(255), nullable=False)
    description = Column(String(1000), nullable=True)
    created_at = Column(TIMESTAMP, nullable=True)
    updated_at = Column(TIMESTAMP, nullable=True)


# Table Video
class Video(Base):
    __tablename__ = 'video'

    id = Column(BigInteger, primary_key=True)
    title = Column(String(255), nullable=False)
    description = Column(String(1000), nullable=True)
    video_url = Column(String(255), nullable=False)
    created_at = Column(TIMESTAMP, nullable=True)


# Table Newsletter
class Newsletter(Base):
    __tablename__ = 'newsletter'

    id = Column(BigInteger, primary_key=True)
    email = Column(String(255), nullable=False, unique=True)
    subscribed_at = Column(TIMESTAMP, nullable=True)


# Table ContactBanniere
class ContactBanniere(Base):
    __tablename__ = 'contact_banniere'

    id = Column(BigInteger, primary_key=True)
    content = Column(String(1000), nullable=False)
    created_at = Column(TIMESTAMP, nullable=True)
    updated_at = Column(TIMESTAMP, nullable=True)


# Table Tchat
class Tchat(Base):
    __tablename__ = 'tchat'

    id = Column(BigInteger, primary_key=True)
    user_id = Column(BigInteger, ForeignKey('users.id'), nullable=False)
    message = Column(String(1000), nullable=False)
    sent_at = Column(TIMESTAMP, nullable=True)

    user = relationship('User', back_populates='tchat')


# Configuration de l'engine et création des tables
if __name__ == '__main__':
    engine = create_engine('postgresql://postgres:admin@localhost:5432/portail_web', echo=True)

    Base.metadata.create_all(engine)  #crée les tables si elles n'existent pas déjà.


____ ### inserer de données
from sqlalchemy.orm import sessionmaker

# Création d'une session
Session = sessionmaker(bind=engine)
session = Session()

# Insertion d'un utilisateur
new_user = User(name="John Doe", email="john.doe@example.com", password="securepassword", actif=True)
session.add(new_user)

# Insertion de plusieurs utilisateurs
users = [
    User(name="Alice Smith", email="alice.smith@example.com", password="password123", actif=False),
    User(name="Bob Johnson", email="bob.johnson@example.com", password="pass456", actif=True)
]
session.add_all(users)

# Commit des modifications
session.commit()

# Vérification
print("Les données ont été insérées avec succès !")

____
-pip install alembic sqlalchemy psycopg2
-Initialiser Alembic
alembic init alembic #Cela crée un répertoire alembic avec plusieurs fichiers nécessaires, comme env.py et versions
-ajout de la colonne dans le models.py
class User(Base):
    __tablename__ = 'users'
    :::
    telephone = Column(String(20), nullable=True)  # Nouvelle colonne
:::

-alembic revision --autogenerate -m "Ajout de la colonne telephone dans users"
- appliquer la migration
alembic upgrade head

#### meme procede pr renommer une colonne ou le type de la colonne ou le nom de la table


_________________________________ snd 


Pour créer une base de données flexible et extensible pour un site web en utilisant Python et PostgreSQL, avec les tables et relations demandées, nous allons utiliser un ORM (Object-Relational Mapping) comme **SQLAlchemy**. Cela permet de définir les schémas de manière programmatique tout en respectant les bonnes pratiques pour la gestion des relations et la flexibilité.

Voici comment procéder pour définir les classes (tables), leurs relations et générer les migrations pour la base de données.

### 1. Installation de SQLAlchemy et psycopg2
Assurez-vous d'avoir installé les dépendances suivantes :
```bash
pip install sqlalchemy psycopg2
```

### 2. Définition des classes pour les tables

Voici un exemple de code Python qui définit les tables pour les entités que vous avez mentionnées avec leurs relations.

```python
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime, Text, Boolean, Float
from sqlalchemy.orm import relationship, declarative_base, sessionmaker
from sqlalchemy.ext.declarative import declared_attr
from datetime import datetime

# Créer une base déclarative
Base = declarative_base()

# Classe de base pour la gestion flexible des ajouts de colonnes
class BaseModel(Base):
    __abstract__ = True

    # Définir dynamiquement le nom de la table
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    # Colonnes communes
    id_nom_table = Column(Integer, primary_key=True, autoincrement=True)  # L'ID sera maintenant `id_nom_table`
    created_at = Column(DateTime, default=datetime.utcnow)  # Timestamp de création
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)  # Timestamp de mise à jour
    deleted_at = Column(DateTime, nullable=True)  # Timestamp de suppression, peut être NULL si non supprimé


# Table User
class User(BaseModel):
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    is_active = Column(Boolean, default=True)
    # Relations
    projects = relationship("Project", back_populates="user")
    ratings = relationship("Rating", back_populates="user")
    comments = relationship("Comment", back_populates="user")


# Table Project
class Project(BaseModel):
    name = Column(String(255), nullable=False)
    description = Column(Text)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)

    # Relations
    user = relationship("User", back_populates="projects")
    comments = relationship("Comment", back_populates="project")


# Table Service
class Service(BaseModel):
    name = Column(String(255), nullable=False)
    description = Column(Text)

    # Relations
    ratings = relationship("Rating", back_populates="service")
    comments = relationship("Comment", back_populates="service")


# Table Media
class Media(BaseModel):
    media_type = Column(String(50))  # image, video, etc.
    url = Column(String(255), nullable=False)

    # Relations
    project_id = Column(Integer, ForeignKey('project.id'))
    project = relationship("Project", back_populates="media")


# Table Menu (gère les menus du site)
class Menu(BaseModel):
    name = Column(String(100), nullable=False)
    url = Column(String(255), nullable=False)
    order = Column(Integer)

    # Relations
    parent_id = Column(Integer, ForeignKey('menu.id'))
    parent = relationship("Menu", backref="children")


# Table Comment (pour les commentaires)
class Comment(BaseModel):
    content = Column(Text, nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    project_id = Column(Integer, ForeignKey('project.id'))
    service_id = Column(Integer, ForeignKey('service.id'))

    # Relations
    user = relationship("User", back_populates="comments")
    project = relationship("Project", back_populates="comments")
    service = relationship("Service", back_populates="comments")


# Table Rating (pour les notes des services ou webinaires)
class Rating(BaseModel):
    rating_value = Column(Integer)  # Exemple : 1 à 5
    user_id = Column(Integer, ForeignKey('user.id'))
    service_id = Column(Integer, ForeignKey('service.id'))

    # Relations
    user = relationship("User", back_populates="ratings")
    service = relationship("Service", back_populates="ratings")


# Table AuditLog (pour suivre les actions des administrateurs)
class AuditLog(BaseModel):
    action = Column(String(255))
    performed_by = Column(Integer, ForeignKey('user.id'))

    # Relations
    user = relationship("User")


# Table Role (pour la gestion des rôles des utilisateurs)
class Role(BaseModel):
    name = Column(String(50), nullable=False)

    # Relations
    users = relationship("User", secondary="user_roles")


# Table UserRoles (relation entre User et Role)
class UserRoles(Base):
    __tablename__ = 'user_roles'

    user_id = Column(Integer, ForeignKey('user.id'), primary_key=True)
    role_id = Column(Integer, ForeignKey('role.id'), primary_key=True)


# Table Webinars (pour gérer les webinaires)
class Webinars(BaseModel):
    title = Column(String(255), nullable=False)
    description = Column(Text)
    date = Column(DateTime)

# Table Banner (pour les bannières du site)
class Banner(BaseModel):
    title = Column(String(255))
    content = Column(Text)
    image_url = Column(String(255))

# Table Newsletter (pour les newsletters du site)
class Newsletter(BaseModel):
    title = Column(String(255))
    content = Column(Text)

# Table Contact (pour les informations de contact)
class Contact(BaseModel):
    name = Column(String(255))
    email = Column(String(255))
    message = Column(Text)

# Configuration de la base de données PostgreSQL
DATABASE_URL = "postgresql://username:password@localhost/your_database_name"
engine = create_engine(DATABASE_URL)

# Créer toutes les tables
Base.metadata.create_all(engine)

# Création de la session
Session = sessionmaker(bind=engine)
session = Session()

# Exemple de création d'utilisateur
new_user = User(username="admin", email="admin@example.com", password="password123")
session.add(new_user)
session.commit()
```

### Explication des tables et des relations :
- **User** : Stocke les informations de l'utilisateur (connexion, email, mot de passe, etc.). Il est lié aux tables `projects`, `ratings`, et `comments`.
- **Project** : Représente les projets sur le site. L'utilisateur peut avoir plusieurs projets.
- **Service** : Représente un service proposé sur le site, avec des commentaires et des évaluations possibles.
- **Media** : Représente les médias associés aux projets (images, vidéos, etc.).
- **Menu** : Permet de gérer les menus du site (accueil, contact, etc.).
- **Comment** : Permet de stocker les commentaires des utilisateurs sur les projets et services.
- **Rating** : Stocke les évaluations des services et des webinaires.
- **AuditLog** : Suivi des actions des administrateurs sur le site.
- **Role et UserRoles** : Gère les rôles des utilisateurs et leurs permissions (par exemple : administrateur, utilisateur).
- **Webinars** : Représente les webinaires sur le site.
- **Banner** : Représente les bannières du site (publicité, promotion, etc.).
- **Newsletter** : Gère les newsletters.
- **Contact** : Représente les messages de contact des utilisateurs.

### 3. Explications supplémentaires
- L'usage de `BaseModel` permet de rendre le modèle extensible et flexible pour l'ajout de nouvelles variables ou changements de types.
- La relation entre les tables est définie par des clés étrangères (`ForeignKey`) et des relations (`relationship`), ce qui permet une navigation facile dans les données.
- La flexibilité est aussi assurée par l'utilisation de types généraux tels que `Text`, `String`, `Integer`, etc.

Avec ce code, vous pouvez facilement ajouter de nouvelles tables, de nouvelles colonnes ou ajuster les types des colonnes en fonction des besoins futurs de l'application.


_________________mld, mcd
Voici un aperçu des schémas MLD (Modèle Logique de Données) et MCD (Modèle Conceptuel de Données) pour le projet de site web avec les tables que vous avez mentionnées. Ces schémas sont des représentations visuelles qui vous aident à comprendre la structure des données et leurs relations.

### 1. **Modèle Conceptuel de Données (MCD) :**

Le MCD représente une vue abstraite de la base de données en termes d'entités et de leurs relations sans entrer dans les détails techniques.

**Entités et relations :**

1. **Utilisateur (User)**  
   Attributs : id, username, email, password, is_active, created_at, updated_at  
   Relations :
   - Un utilisateur peut avoir plusieurs projets (1:N avec Projet)
   - Un utilisateur peut laisser plusieurs commentaires (1:N avec Commentaire)
   - Un utilisateur peut évaluer plusieurs services (1:N avec Rating)
   - Un utilisateur peut être associé à plusieurs rôles (N:M avec Role via UserRoles)
   - Un utilisateur peut effectuer plusieurs actions dans les logs (1:N avec AuditLog)

2. **Projet (Project)**  
   Attributs : id, name, description, user_id (clé étrangère vers User)  
   Relations :
   - Un projet peut avoir plusieurs médias (1:N avec Media)
   - Un projet peut avoir plusieurs commentaires (1:N avec Commentaire)
   
3. **Service (Service)**  
   Attributs : id, name, description  
   Relations :
   - Un service peut avoir plusieurs évaluations (1:N avec Rating)
   - Un service peut avoir plusieurs commentaires (1:N avec Commentaire)
   
4. **Média (Media)**  
   Attributs : id, media_type, url, project_id (clé étrangère vers Project)  
   
5. **Commentaire (Comment)**  
   Attributs : id, content, user_id (clé étrangère vers User), project_id (clé étrangère vers Project), service_id (clé étrangère vers Service)  
   
6. **Évaluation (Rating)**  
   Attributs : id, rating_value, user_id (clé étrangère vers User), service_id (clé étrangère vers Service)  
   
7. **Role (Role)**  
   Attributs : id, name  
   Relations :
   - Un rôle peut être attribué à plusieurs utilisateurs (N:M avec User via UserRoles)
   
8. **UserRoles (Table d'association pour User et Role)**  
   Attributs : user_id (clé étrangère vers User), role_id (clé étrangère vers Role)

9. **AuditLog (AuditLog)**  
   Attributs : id, action, performed_by (clé étrangère vers User)  

10. **Menu (Menu)**  
    Attributs : id, name, url, order, parent_id (clé étrangère vers Menu pour gérer les sous-menus)

11. **Webinar (Webinar)**  
    Attributs : id, title, description, date

12. **Banner (Banner)**  
    Attributs : id, title, content, image_url

13. **Newsletter (Newsletter)**  
    Attributs : id, title, content

14. **Contact (Contact)**  
    Attributs : id, name, email, message

Users, role, user_role, tchat, commentaires, media, projets,log,footer,
'acceuil','apropos',album,cellule, service, webinaire, atelier,contact,
newsletter,partenaire, temoignage,equipe


Voici les instructions SQL pour la création des tables dans une base de données. Elles concernent différentes entités comme les utilisateurs, les rôles, les services, et d'autres éléments d'une application. Voici une explication succincte de chaque table en français :

### 1. Table `users` :
Cette table contient les informations relatives aux utilisateurs de la plateforme. Chaque utilisateur a un identifiant (`user_id`), un nom, un prénom, un email, un mot de passe, un matricule, un rôle, un service auquel il appartient, ainsi que des timestamps pour suivre les dates de création, mise à jour et suppression éventuelle du compte.

### 2. Table `role` :
Cette table définit les rôles disponibles dans l'application. Chaque rôle possède un identifiant (`role_id`), un nom (`role_name`), une valeur (`role_value`) et une date de création (`role_date_creation`).

### 3. Table `user_role` :
Cette table établit une relation entre les utilisateurs et leurs rôles. Elle lie l'identifiant du rôle (`role_id`) à l'identifiant de l'utilisateur (`user_id`). Les clés étrangères permettent d'assurer l'intégrité des données en cas de suppression d'un utilisateur ou d'un rôle.

### 4. Table `tchat` :
Cette table enregistre les messages envoyés dans le chat, avec des informations comme l'identifiant du message (`tchat_id`), le nom du chat, le matricule, le message lui-même, la direction du message (entrant ou sortant), le service associé et l'email de l'utilisateur.

### 5. Table `footer` :
Cette table contient les informations relatives au pied de page d'une page web, avec des détails tels que l'adresse, la localisation, le téléphone, l'email, l'horaire et la devise. Elle est liée à un utilisateur et à un média.

### 6. Table `acceuil` :
Cette table gère les informations liées à la page d'accueil de l'application, avec des champs pour des liens vers les sections de projet, témoignage, footer, etc.

### 7. Table `album` :
Table pour gérer les albums multimédia, incluant un identifiant d'album (`album_id`), un titre, une description, une URL et un type de fichier (image, vidéo, etc.).

### 8. Table `temoignage` :
Cette table contient les témoignages des utilisateurs avec un identifiant de témoignage (`temoignage_id`), un commentaire, une note (étoile) et des informations temporelles.

### 9. Table `equipe` :
Table qui lie les utilisateurs aux services et cellules. Un utilisateur fait partie d'une équipe, avec des informations comme le service et la cellule auxquels ils appartiennent.

### 10. Table `apropos` :
Cette table fournit des informations supplémentaires sur les partenaires de l'application, incluant des titres, sous-titres et descriptions.

### 11. Table `service` :
Table qui contient des informations sur les services proposés, y compris les utilisateurs, cellules et équipes associés à chaque service.

### 12. Table `commentaires` :
Cette table stocke les commentaires des utilisateurs sur l'application. Elle contient un identifiant de commentaire (`commentaire_id`), un commentaire et des informations temporelles.

### 13. Table `media` :
Table pour les fichiers multimédia associés aux utilisateurs, comprenant des informations sur les fichiers, leur description et des timestamps.

### 14. Table `cellule` :
Table qui définit les cellules dans les services, associant un utilisateur à une cellule avec des informations descriptives.

### 15. Table `webinaire` :
Table qui enregistre les informations sur les webinaires, y compris le titre, sous-titre, description, et liens vers les utilisateurs et médias associés.

### 16. Table `atelier` :
Cette table est similaire à celle des webinaires, mais pour les ateliers. Elle lie également les utilisateurs et les médias associés à chaque atelier.

### 17. Table `newsletter` :
Cette table contient les informations sur les newsletters envoyées, incluant le titre, la description, le contenu, et les liens vers les albums et utilisateurs associés.

### 18. Table `contact` :
Table pour gérer les demandes de contact des utilisateurs, avec des informations sur l'expéditeur, le sujet, le contenu et les timestamps.

Cela constitue une structure pour une plateforme avec des utilisateurs, des messages, des rôles, des services et d'autres composants liés. La définition des clés primaires et étrangères permet d'assurer l'intégrité des données et des relations entre les différentes entités.
___________________________________________________________________

CREATE TABLE IF NOT EXISTS users (
    user_id BIGSERIAL PRIMARY KEY,
    user_name VARCHAR(255) NOT NULL,
    user_prenom VARCHAR(255),
    user_phone_ip VARCHAR(255),
    media_id BIGINT NOT NULL,
    service_id INT NOT NULL,
    user_poste VARCHAR(255),
    user_genre VARCHAR(255),
    user_email VARCHAR(255) NOT NULL UNIQUE,
    user_password VARCHAR(255) NOT NULL,
    user_matricule VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT NULL,
    updated_at TIMESTAMP DEFAULT NULL,
    delete_at TIMESTAMP DEFAULT NULL,
    FOREIGN KEY (media_id) REFERENCES media(media_id) ON DELETE CASCADE,
    FOREIGN KEY (service_id) REFERENCES service(service_id) ON DELETE CASCADE
);

CREATE INDEX idx_user_email ON users(user_email);

CREATE TABLE IF NOT EXISTS role (
    role_id SERIAL PRIMARY KEY,
    role_name VARCHAR(20) NOT NULL,
    role_value VARCHAR(20) NOT NULL,
    role_date_creation TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS user_role (
    id_user_role SERIAL PRIMARY KEY,
    role_id INT NOT NULL,
    user_id BIGINT NOT NULL,
    FOREIGN KEY (role_id) REFERENCES role(role_id) ON DELETE CASCADE,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS tchat (
    tchat_id BIGSERIAL PRIMARY KEY,
    tchat_name VARCHAR(255) NOT NULL,
    tchat_message TEXT,
    tchat_direction VARCHAR(255),
    tchat_email VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    delete_at TIMESTAMP DEFAULT NULL
);

CREATE INDEX idx_tchat_email ON tchat(tchat_email);

CREATE TABLE IF NOT EXISTS footer (
    footer_id BIGSERIAL PRIMARY KEY,
    user_id BIGINT NOT NULL,
    media_id BIGINT NOT NULL,
    adresse VARCHAR(255) NOT NULL,
    localisation VARCHAR(255),
    tel VARCHAR(255),
    email VARCHAR(255),
    horaire VARCHAR(255),
    devise VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
    FOREIGN KEY (media_id) REFERENCES media(media_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS accueil (
    accueil_id BIGSERIAL PRIMARY KEY,
    user_id BIGINT NOT NULL,
    media_id BIGINT NOT NULL,
    projet_id BIGINT NOT NULL,
    news_id BIGINT NOT NULL,
    temoignage_id BIGINT NOT NULL,
    footer_id BIGINT NOT NULL,
    tchat_id BIGINT NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
    FOREIGN KEY (media_id) REFERENCES media(media_id) ON DELETE CASCADE,
    FOREIGN KEY (footer_id) REFERENCES footer(footer_id) ON DELETE CASCADE,
    FOREIGN KEY (tchat_id) REFERENCES tchat(tchat_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS album (
    album_id BIGSERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    url VARCHAR(255) NOT NULL,
    type VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    delete_at TIMESTAMP DEFAULT NULL
);

CREATE INDEX idx_album_title ON album(title);

CREATE TABLE IF NOT EXISTS temoignage (
    temoignage_id BIGSERIAL PRIMARY KEY,
    media_id BIGINT NOT NULL,
    user_id BIGINT NOT NULL,
    commentaire TEXT NOT NULL,
    etoile BIGINT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    delete_at TIMESTAMP DEFAULT NULL,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
    FOREIGN KEY (media_id) REFERENCES media(media_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS equipe (
    equipe_id BIGSERIAL PRIMARY KEY,
    user_id BIGINT NOT NULL,
    service_id BIGINT NOT NULL,
    cellule_id BIGINT NOT NULL,
    media_id BIGINT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    delete_at TIMESTAMP DEFAULT NULL,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
    FOREIGN KEY (service_id) REFERENCES service(service_id) ON DELETE CASCADE,
    FOREIGN KEY (cellule_id) REFERENCES cellule(cellule_id) ON DELETE CASCADE,
    FOREIGN KEY (media_id) REFERENCES media(media_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS apropos (
    apropos_id BIGSERIAL PRIMARY KEY,
    user_id BIGINT NOT NULL,
    partenaire_id BIGINT NOT NULL,
    titre VARCHAR(255) NOT NULL,
    sous_titre VARCHAR(255) NOT NULL,
    description TEXT,
    service_id BIGINT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
    FOREIGN KEY (partenaire_id) REFERENCES partenaire(partenaire_id) ON DELETE CASCADE,
    FOREIGN KEY (service_id) REFERENCES service(service_id) ON DELETE CASCADE
);

CREATE INDEX idx_apropos_user ON apropos(user_id);
CREATE INDEX idx_apropos_partenaire ON apropos(partenaire_id);

CREATE TABLE IF NOT EXISTS service (
    service_id BIGSERIAL PRIMARY KEY,
    user_id BIGINT NOT NULL,
    cellule_id BIGINT NOT NULL,
    equipe_id BIGINT NOT NULL,
    titre VARCHAR(255) NOT NULL,
    nom VARCHAR(255) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
    FOREIGN KEY (cellule_id) REFERENCES cellule(cellule_id) ON DELETE CASCADE,
    FOREIGN KEY (equipe_id) REFERENCES equipe(equipe_id) ON DELETE CASCADE
);

CREATE INDEX idx_service_user ON service(user_id);
CREATE INDEX idx_service_cellule ON service(cellule_id);


CREATE TABLE IF NOT EXISTS commentaires (
    commentaire_id BIGSERIAL PRIMARY KEY,
    user_id BIGINT NOT NULL,
    commentaire TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    delete_at TIMESTAMP DEFAULT NULL,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
);

CREATE INDEX idx_commentaires_user ON commentaires(user_id);


CREATE TABLE IF NOT EXISTS media (
    media_id BIGSERIAL PRIMARY KEY,
    user_id BIGINT NOT NULL,
    nom_file VARCHAR(255),
    lien_file VARCHAR(255),
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
);

CREATE INDEX idx_media_user ON media(user_id);

CREATE TABLE IF NOT EXISTS cellule (
    cellule_id BIGSERIAL PRIMARY KEY,
    user_id BIGINT NOT NULL,
    service_id BIGINT NOT NULL,
    titre VARCHAR(255),
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
    FOREIGN KEY (service_id) REFERENCES service(service_id) ON DELETE CASCADE
);

CREATE INDEX idx_cellule_user ON cellule(user_id);
CREATE INDEX idx_cellule_service ON cellule(service_id);


CREATE TABLE IF NOT EXISTS webinaire (
    webinaire_id BIGSERIAL PRIMARY KEY,
    user_id BIGINT NOT NULL,
    media_id BIGINT NOT NULL,
    titre VARCHAR(255) NOT NULL,
    sous_titre VARCHAR(255) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
    FOREIGN KEY (media_id) REFERENCES media(media_id) ON DELETE CASCADE
);

CREATE INDEX idx_webinaire_user ON webinaire(user_id);
CREATE INDEX idx_webinaire_media ON webinaire(media_id);


CREATE TABLE IF NOT EXISTS atelier (
    atelier_id BIGSERIAL PRIMARY KEY,
    user_id BIGINT NOT NULL,
    media_id BIGINT NOT NULL,
    titre VARCHAR(255) NOT NULL,
    sous_titre VARCHAR(255) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
    FOREIGN KEY (media_id) REFERENCES media(media_id) ON DELETE CASCADE
);

CREATE INDEX idx_atelier_user ON atelier(user_id);
CREATE INDEX idx_atelier_media ON atelier(media_id);

CREATE TABLE IF NOT EXISTS newsletter (
    news_id BIGSERIAL PRIMARY KEY,
    user_id BIGINT NOT NULL,
    media_id BIGINT NOT NULL,
    album_id BIGINT NOT NULL,
    date_event TIMESTAMP DEFAULT NULL,
    id_commentaire BIGINT NOT NULL,
    titre VARCHAR(255) NOT NULL,
    description TEXT,
    contenu TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
    FOREIGN KEY (media_id) REFERENCES media(media_id) ON DELETE CASCADE,
    FOREIGN KEY (id_commentaire) REFERENCES commentaires(commentaire_id) ON DELETE CASCADE
);

CREATE INDEX idx_newsletter_user ON newsletter(user_id);
CREATE INDEX idx_newsletter_media ON newsletter(media_id);
CREATE INDEX idx_newsletter_commentaire ON newsletter(id_commentaire);


CREATE TABLE IF NOT EXISTS contact (
    contact_id BIGSERIAL PRIMARY KEY,
    nom_prenom VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    contact VARCHAR(255) NOT NULL,
    sujet VARCHAR(255) NOT NULL,
    contenu TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_contact_email ON contact(email);


CREATE TABLE IF NOT EXISTS partenaire (
    partenaire_id BIGSERIAL PRIMARY KEY,
    nom VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_partenaire_nom ON partenaire(nom);



CREATE TABLE IF NOT EXISTS projets (
    projet_id BIGSERIAL PRIMARY KEY,
    user_id BIGINT NOT NULL,
    media_id BIGINT NOT NULL,
    nom_projet VARCHAR(255) NOT NULL,
    etat VARCHAR(255) NOT NULL CHECK (etat IN ('non démarré', 'en cours', 'terminé')),
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
    FOREIGN KEY (media_id) REFERENCES media(media_id) ON DELETE CASCADE
);


_____________________________________________________________


import psycopg2
from psycopg2 import sql
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

# Configuration de la connexion à PostgreSQL
DB_NAME = "my_database"  # Nom de la base de données à créer
DB_USER = "postgres"     # Utilisateur PostgreSQL
DB_PASSWORD = "password" # Mot de passe PostgreSQL
DB_HOST = "localhost"    # Hôte PostgreSQL
DB_PORT = "5432"         # Port PostgreSQL

# Fonction pour établir une connexion à PostgreSQL
def connect_to_db(dbname="postgres"):
    try:
        conn = psycopg2.connect(
            dbname=dbname,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT
        )
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        return conn
    except Exception as e:
        print(f"Erreur de connexion à la base de données : {e}")
        return None

# Fonction pour créer la base de données
def create_database():
    conn = connect_to_db()
    if conn is None:
        return

    try:
        cursor = conn.cursor()
        # Vérifier si la base de données existe déjà
        cursor.execute(sql.SQL("SELECT 1 FROM pg_database WHERE datname = %s"), [DB_NAME])
        exists = cursor.fetchone()

        if not exists:
            # Créer la base de données
            cursor.execute(sql.SQL("CREATE DATABASE {}").format(sql.Identifier(DB_NAME)))
            print(f"Base de données '{DB_NAME}' créée avec succès.")
        else:
            print(f"La base de données '{DB_NAME}' existe déjà.")

        cursor.close()
    except Exception as e:
        print(f"Erreur lors de la création de la base de données : {e}")
    finally:
        conn.close()

# Fonction pour créer les tables
def create_tables():
    conn = connect_to_db(DB_NAME)
    if conn is None:
        return

    try:
        cursor = conn.cursor()

        # Table `users`
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                user_id BIGSERIAL PRIMARY KEY,
                user_name VARCHAR(255) NOT NULL,
                user_prenom VARCHAR(255),
                user_phone_ip VARCHAR(255),
                media_id BIGINT NOT NULL,
                service_id INT NOT NULL,
                user_poste VARCHAR(255),
                user_genre VARCHAR(255),
                user_email VARCHAR(255) NOT NULL UNIQUE,
                user_password VARCHAR(255) NOT NULL,
                user_matricule VARCHAR(255) NOT NULL,
                created_at TIMESTAMP DEFAULT NULL,
                updated_at TIMESTAMP DEFAULT NULL,
                delete_at TIMESTAMP DEFAULT NULL
            );
        """)

        # Table `role`
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS role (
                role_id SERIAL PRIMARY KEY,
                role_name VARCHAR(20) NOT NULL,
                role_value VARCHAR(20) NOT NULL,
                role_date_creation TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        """)

        # Table `user_role`
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS user_role (
                id_user_role SERIAL PRIMARY KEY,
                role_id INT NOT NULL,
                user_id BIGINT NOT NULL,
                FOREIGN KEY (role_id) REFERENCES role(role_id) ON DELETE CASCADE,
                FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
            );
        """)

        # Table `tchat`
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS tchat (
                tchat_id BIGSERIAL PRIMARY KEY,
                tchat_name VARCHAR(255) NOT NULL,
                tchat_message TEXT,
                tchat_direction VARCHAR(255),
                tchat_email VARCHAR(255) NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                delete_at TIMESTAMP DEFAULT NULL
            );
            CREATE INDEX IF NOT EXISTS idx_tchat_email ON tchat(tchat_email);
        """)

        # Table `footer`
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS footer (
                footer_id BIGSERIAL PRIMARY KEY,
                user_id BIGINT NOT NULL,
                media_id BIGINT NOT NULL,
                adresse VARCHAR(255) NOT NULL,
                localisation VARCHAR(255),
                tel VARCHAR(255),
                email VARCHAR(255),
                horaire VARCHAR(255),
                devise VARCHAR(255),
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
                FOREIGN KEY (media_id) REFERENCES media(media_id) ON DELETE CASCADE
            );
        """)

        # Table `accueil`
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS accueil (
                accueil_id BIGSERIAL PRIMARY KEY,
                user_id BIGINT NOT NULL,
                media_id BIGINT NOT NULL,
                projet_id BIGINT NOT NULL,
                news_id BIGINT NOT NULL,
                temoignage_id BIGINT NOT NULL,
                footer_id BIGINT NOT NULL,
                tchat_id BIGINT NOT NULL,
                description TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
                FOREIGN KEY (media_id) REFERENCES media(media_id) ON DELETE CASCADE,
                FOREIGN KEY (footer_id) REFERENCES footer(footer_id) ON DELETE CASCADE,
                FOREIGN KEY (tchat_id) REFERENCES tchat(tchat_id) ON DELETE CASCADE
            );
        """)

        # Table `album`
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS album (
                album_id BIGSERIAL PRIMARY KEY,
                title VARCHAR(255) NOT NULL,
                description TEXT,
                url VARCHAR(255) NOT NULL,
                type VARCHAR(255) NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                delete_at TIMESTAMP DEFAULT NULL
            );
            CREATE INDEX IF NOT EXISTS idx_album_title ON album(title);
        """)

        # Table `temoignage`
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS temoignage (
                temoignage_id BIGSERIAL PRIMARY KEY,
                media_id BIGINT NOT NULL,
                user_id BIGINT NOT NULL,
                commentaire TEXT NOT NULL,
                etoile BIGINT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                delete_at TIMESTAMP DEFAULT NULL,
                FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
                FOREIGN KEY (media_id) REFERENCES media(media_id) ON DELETE CASCADE
            );
        """)

        # Table `equipe`
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS equipe (
                equipe_id BIGSERIAL PRIMARY KEY,
                user_id BIGINT NOT NULL,
                service_id BIGINT NOT NULL,
                cellule_id BIGINT NOT NULL,
                media_id BIGINT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                delete_at TIMESTAMP DEFAULT NULL,
                FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
                FOREIGN KEY (service_id) REFERENCES service(service_id) ON DELETE CASCADE,
                FOREIGN KEY (cellule_id) REFERENCES cellule(cellule_id) ON DELETE CASCADE,
                FOREIGN KEY (media_id) REFERENCES media(media_id) ON DELETE CASCADE
            );
        """)

        # Table `apropos`
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS apropos (
                apropos_id BIGSERIAL PRIMARY KEY,
                user_id BIGINT NOT NULL,
                partenaire_id BIGINT NOT NULL,
                titre VARCHAR(255) NOT NULL,
                sous_titre VARCHAR(255) NOT NULL,
                description TEXT,
                service_id BIGINT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
                FOREIGN KEY (partenaire_id) REFERENCES partenaire(partenaire_id) ON DELETE CASCADE,
                FOREIGN KEY (service_id) REFERENCES service(service_id) ON DELETE CASCADE
            );
            CREATE INDEX IF NOT EXISTS idx_apropos_user ON apropos(user_id);
            CREATE INDEX IF NOT EXISTS idx_apropos_partenaire ON apropos(partenaire_id);
        """)

        # Table `service`
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS service (
                service_id BIGSERIAL PRIMARY KEY,
                user_id BIGINT NOT NULL,
                cellule_id BIGINT NOT NULL,
                equipe_id BIGINT NOT NULL,
                titre VARCHAR(255) NOT NULL,
                nom VARCHAR(255) NOT NULL,
                description TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
                FOREIGN KEY (cellule_id) REFERENCES cellule(cellule_id) ON DELETE CASCADE,
                FOREIGN KEY (equipe_id) REFERENCES equipe(equipe_id) ON DELETE CASCADE
            );
            CREATE INDEX IF NOT EXISTS idx_service_user ON service(user_id);
            CREATE INDEX IF NOT EXISTS idx_service_cellule ON service(cellule_id);
        """)

        # Table `commentaires`
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS commentaires (
                commentaire_id BIGSERIAL PRIMARY KEY,
                user_id BIGINT NOT NULL,
                commentaire TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                delete_at TIMESTAMP DEFAULT NULL,
                FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
            );
            CREATE INDEX IF NOT EXISTS idx_commentaires_user ON commentaires(user_id);
        """)

        # Table `media`
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS media (
                media_id BIGSERIAL PRIMARY KEY,
                user_id BIGINT NOT NULL,
                nom_file VARCHAR(255),
                lien_file VARCHAR(255),
                description TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
            );
            CREATE INDEX IF NOT EXISTS idx_media_user ON media(user_id);
        """)

        # Table `cellule`
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS cellule (
                cellule_id BIGSERIAL PRIMARY KEY,
                user_id BIGINT NOT NULL,
                service_id BIGINT NOT NULL,
                titre VARCHAR(255),
                description TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
                FOREIGN KEY (service_id) REFERENCES service(service_id) ON DELETE CASCADE
            );
            CREATE INDEX IF NOT EXISTS idx_cellule_user ON cellule(user_id);
            CREATE INDEX IF NOT EXISTS idx_cellule_service ON cellule(service_id);
        """)

        # Table `webinaire`
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS webinaire (
                webinaire_id BIGSERIAL PRIMARY KEY,
                user_id BIGINT NOT NULL,
                media_id BIGINT NOT NULL,
                titre VARCHAR(255) NOT NULL,
                sous_titre VARCHAR(255) NOT NULL,
                description TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
                FOREIGN KEY (media_id) REFERENCES media(media_id) ON DELETE CASCADE
            );
            CREATE INDEX IF NOT EXISTS idx_webinaire_user ON webinaire(user_id);
            CREATE INDEX IF NOT EXISTS idx_webinaire_media ON webinaire(media_id);
        """)

        # Table `atelier`
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS atelier (
                atelier_id BIGSERIAL PRIMARY KEY,
                user_id BIGINT NOT NULL,
                media_id BIGINT NOT NULL,
                titre VARCHAR(255) NOT NULL,
                sous_titre VARCHAR(255) NOT NULL,
                description TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
                FOREIGN KEY (media_id) REFERENCES media(media_id) ON DELETE CASCADE
            );
            CREATE INDEX IF NOT EXISTS idx_atelier_user ON atelier(user_id);
            CREATE INDEX IF NOT EXISTS idx_atelier_media ON atelier(media_id);
        """)

        # Table `newsletter`
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS newsletter (
                news_id BIGSERIAL PRIMARY KEY,
                user_id BIGINT NOT NULL,
                media_id BIGINT NOT NULL,
                album_id BIGINT NOT NULL,
                date_event TIMESTAMP DEFAULT NULL,
                id_commentaire BIGINT NOT NULL,
                titre VARCHAR(255) NOT NULL,
                description TEXT,
                contenu TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
                FOREIGN KEY (media_id) REFERENCES media(media_id) ON DELETE CASCADE,
                FOREIGN KEY (id_commentaire) REFERENCES commentaires(commentaire_id) ON DELETE CASCADE
            );
            CREATE INDEX IF NOT EXISTS idx_newsletter_user ON newsletter(user_id);
            CREATE INDEX IF NOT EXISTS idx_newsletter_media ON newsletter(media_id);
            CREATE INDEX IF NOT EXISTS idx_newsletter_commentaire ON newsletter(id_commentaire);
        """)

        # Table `contact`
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS contact (
                contact_id BIGSERIAL PRIMARY KEY,
                nom_prenom VARCHAR(255) NOT NULL,
                email VARCHAR(255) NOT NULL,
                contact VARCHAR(255) NOT NULL,
                sujet VARCHAR(255) NOT NULL,
                contenu TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
            CREATE INDEX IF NOT EXISTS idx_contact_email ON contact(email);
        """)

        # Table `partenaire`
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS partenaire (
                partenaire_id BIGSERIAL PRIMARY KEY,
                nom VARCHAR(255) NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
            CREATE INDEX IF NOT EXISTS idx_partenaire_nom ON partenaire(nom);
        """)

        # Table `projets`
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS projets (
                projet_id BIGSERIAL PRIMARY KEY,
                user_id BIGINT NOT NULL,
                media_id BIGINT NOT NULL,
                nom_projet VARCHAR(255) NOT NULL,
                etat VARCHAR(255) NOT NULL CHECK (etat IN ('non démarré', 'en cours', 'terminé')),
                description TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
                FOREIGN KEY (media_id) REFERENCES media(media_id) ON DELETE CASCADE
            );
        """)

        print("Toutes les tables ont été créées avec succès.")
        conn.commit()
    except Exception as e:
        print(f"Erreur lors de la création des tables : {e}")
    finally:
        cursor.close()
        conn.close()

# Point d'entrée du script
if __name__ == "__main__":
    create_database()  # Créer la base de données si elle n'existe pas
    create_tables()    # Créer les tables



_____________________________________________ modif table __________________________

Non, vous n'avez pas besoin de réexécuter toutes les fonctions pour mettre à jour une table ou une colonne. Vous pouvez simplement écrire et exécuter un script spécifique pour effectuer les modifications nécessaires. Voici comment vous pouvez procéder pour mettre à jour une table ou une colonne sans réexécuter tout le script.

---

### **1. Mettre à jour une table ou une colonne**

Si vous souhaitez modifier une table existante (par exemple, ajouter une colonne, modifier un type de colonne, ou supprimer une colonne), vous pouvez écrire une requête SQL `ALTER TABLE` et l'exécuter séparément.

#### **Exemple 1 : Ajouter une nouvelle colonne**
Supposons que vous souhaitez ajouter une colonne `age` à la table `users` :
```python
def add_column_age():
    conn = connect_to_db(DB_NAME)
    if conn is None:
        return

    try:
        cursor = conn.cursor()
        cursor.execute("ALTER TABLE users ADD COLUMN age INT;")
        print("Colonne 'age' ajoutée à la table 'users'.")
        conn.commit()
    except Exception as e:
        print(f"Erreur lors de l'ajout de la colonne : {e}")
    finally:
        cursor.close()
        conn.close()
```

#### **Exemple 2 : Modifier le type d'une colonne**
Supposons que vous souhaitez modifier le type de la colonne `user_phone_ip` de `VARCHAR(255)` à `TEXT` :
```python
def modify_column_user_phone_ip():
    conn = connect_to_db(DB_NAME)
    if conn is None:
        return

    try:
        cursor = conn.cursor()
        cursor.execute("ALTER TABLE users ALTER COLUMN user_phone_ip TYPE TEXT;")
        print("Colonne 'user_phone_ip' modifiée dans la table 'users'.")
        conn.commit()
    except Exception as e:
        print(f"Erreur lors de la modification de la colonne : {e}")
    finally:
        cursor.close()
        conn.close()
```

#### **Exemple 3 : Supprimer une colonne**
Supposons que vous souhaitez supprimer la colonne `user_genre` de la table `users` :
```python
def drop_column_user_genre():
    conn = connect_to_db(DB_NAME)
    if conn is None:
        return

    try:
        cursor = conn.cursor()
        cursor.execute("ALTER TABLE users DROP COLUMN user_genre;")
        print("Colonne 'user_genre' supprimée de la table 'users'.")
        conn.commit()
    except Exception as e:
        print(f"Erreur lors de la suppression de la colonne : {e}")
    finally:
        cursor.close()
        conn.close()
```

---

### **2. Mettre à jour une table avec des contraintes**

Si vous souhaitez ajouter ou supprimer des contraintes (comme une clé étrangère ou un index), vous pouvez également utiliser `ALTER TABLE`.

#### **Exemple 1 : Ajouter une clé étrangère**
Supposons que vous souhaitez ajouter une clé étrangère `media_id` dans la table `users` qui référence la table `media` :
```python
def add_foreign_key_media_id():
    conn = connect_to_db(DB_NAME)
    if conn is None:
        return

    try:
        cursor = conn.cursor()
        cursor.execute("""
            ALTER TABLE users
            ADD CONSTRAINT fk_users_media
            FOREIGN KEY (media_id) REFERENCES media(media_id) ON DELETE CASCADE;
        """)
        print("Clé étrangère 'media_id' ajoutée à la table 'users'.")
        conn.commit()
    except Exception as e:
        print(f"Erreur lors de l'ajout de la clé étrangère : {e}")
    finally:
        cursor.close()
        conn.close()
```

#### **Exemple 2 : Ajouter un index**
Supposons que vous souhaitez ajouter un index sur la colonne `user_email` dans la table `users` :
```python
def add_index_user_email():
    conn = connect_to_db(DB_NAME)
    if conn is None:
        return

    try:
        cursor = conn.cursor()
        cursor.execute("CREATE INDEX idx_user_email ON users(user_email);")
        print("Index 'idx_user_email' ajouté à la table 'users'.")
        conn.commit()
    except Exception as e:
        print(f"Erreur lors de l'ajout de l'index : {e}")
    finally:
        cursor.close()
        conn.close()
```

---

### **3. Exécuter les mises à jour**

Vous pouvez exécuter ces fonctions séparément pour mettre à jour votre base de données sans réexécuter tout le script initial. Par exemple :

```python
if __name__ == "__main__":
    # Créer la base de données et les tables (si nécessaire)
    create_database()
    create_tables()

    # Mettre à jour une table ou une colonne
    add_column_age()
    modify_column_user_phone_ip()
    drop_column_user_genre()
    add_foreign_key_media_id()
    add_index_user_email()
```

---

### **4. Bonnes pratiques pour les mises à jour**

1. **Sauvegarder la base de données** :
   - Avant de faire des modifications structurelles, il est recommandé de sauvegarder votre base de données. Vous pouvez utiliser la commande `pg_dump` pour cela :
     ```bash
     pg_dump -U postgres -d my_database -f backup.sql
     ```

2. **Utiliser des migrations** :
   - Pour gérer les modifications de schéma de base de données de manière structurée, vous pouvez utiliser un outil de migration comme **Alembic** (pour SQLAlchemy) ou **Django Migrations** (si vous utilisez Django).

3. **Tester les modifications** :
   - Testez toujours vos modifications dans un environnement de développement avant de les appliquer en production.

---

### **5. Exemple complet**

Voici un exemple complet pour mettre à jour une table :

```python
import psycopg2
from psycopg2 import sql
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

# Configuration de la connexion à PostgreSQL
DB_NAME = "my_database"  # Nom de la base de données
DB_USER = "postgres"     # Utilisateur PostgreSQL
DB_PASSWORD = "password" # Mot de passe PostgreSQL
DB_HOST = "localhost"    # Hôte PostgreSQL
DB_PORT = "5432"         # Port PostgreSQL

# Fonction pour établir une connexion à PostgreSQL
def connect_to_db(dbname=DB_NAME):
    try:
        conn = psycopg2.connect(
            dbname=dbname,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT
        )
        return conn
    except Exception as e:
        print(f"Erreur de connexion à la base de données : {e}")
        return None

# Fonction pour ajouter une colonne `age` à la table `users`
def add_column_age():
    conn = connect_to_db()
    if conn is None:
        return

    try:
        cursor = conn.cursor()
        cursor.execute("ALTER TABLE users ADD COLUMN age INT;")
        print("Colonne 'age' ajoutée à la table 'users'.")
        conn.commit()
    except Exception as e:
        print(f"Erreur lors de l'ajout de la colonne : {e}")
    finally:
        cursor.close()
        conn.close()

# Point d'entrée du script
if __name__ == "__main__":
    add_column_age()
```

---

### **Résultat attendu**
- Si la colonne `age` n'existe pas dans la table `users`, elle sera ajoutée.
- Si elle existe déjà, le script affichera une erreur (que vous pouvez gérer avec un `try-except`).

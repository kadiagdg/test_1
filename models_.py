
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

-- Table: users
CREATE TABLE IF NOT EXISTS `users` (
    `user_id` BIGINT(20) UNSIGNED NOT NULL AUTO_INCREMENT,
    `user_name` VARCHAR(255) COLLATE utf8mb4_unicode_ci NOT NULL,
    `user_prenom` VARCHAR(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
    `user_phone_ip` VARCHAR(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
    `media_id` BIGINT(20) UNSIGNED NOT NULL,
    `service_id` INT(11) NOT NULL,
    `user_poste` VARCHAR(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
    `user_genre` VARCHAR(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
    `user_email` VARCHAR(255) COLLATE utf8mb4_unicode_ci NOT NULL,
    `user_password` VARCHAR(255) COLLATE utf8mb4_unicode_ci NOT NULL,
    `user_matricule` VARCHAR(255) COLLATE utf8mb4_unicode_ci NOT NULL,
    `created_at` TIMESTAMP NULL DEFAULT NULL,
    `updated_at` TIMESTAMP NULL DEFAULT NULL,
    `delete_at` TIMESTAMP NULL DEFAULT NULL,
    PRIMARY KEY (`user_id`),
    UNIQUE KEY `idx_user_email` (`user_email`), -- Utiliser UNIQUE pour éviter les doublons
    FOREIGN KEY (`media_id`) REFERENCES `media`(`media_id`), ON DELETE CASCADE
    FOREIGN KEY (`service_id`) REFERENCES `service`(`service_id`) ON DELETE CASCADE
);


-- Table: role
CREATE TABLE IF NOT EXISTS `role` (
    `role_id` INT(11) AUTO_INCREMENT PRIMARY KEY,
    `role_name` VARCHAR(20) NOT NULL,
    `role_value` VARCHAR(20) NOT NULL,
    `role_date_creation` TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table: user_role
CREATE TABLE IF NOT EXISTS `user_role` (
    `id_user_role` INT(11) AUTO_INCREMENT PRIMARY KEY,
    `role_id` INT(11) NOT NULL,
    `user_id` BIGINT(20) UNSIGNED NOT NULL,
    FOREIGN KEY (`role_id`) REFERENCES `role`(`role_id`) ON DELETE CASCADE,
    FOREIGN KEY (`user_id`) REFERENCES `users`(`user_id`) ON DELETE CASCADE
);



CREATE TABLE IF NOT EXISTS `tchat` (
    `tchat_id` BIGINT(20) UNSIGNED NOT NULL AUTO_INCREMENT,
    `tchat_name` VARCHAR(255) COLLATE utf8mb4_unicode_ci NOT NULL,
    `tchat_message` TEXT COLLATE utf8mb4_unicode_ci DEFAULT NULL,
    `tchat_direction` VARCHAR(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
    `tchat_email` VARCHAR(255) COLLATE utf8mb4_unicode_ci NOT NULL,
    `created_at` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
    `updated_at` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    `delete_at` TIMESTAMP NULL DEFAULT NULL,
    PRIMARY KEY (`tchat_id`),
    INDEX `idx_tchat_email` (`tchat_email`) -- Index pour accélérer les recherches par email
);


CREATE TABLE IF NOT EXISTS `footer` (
    `footer_id` BIGINT(20) UNSIGNED NOT NULL AUTO_INCREMENT,
    `user_id` BIGINT(20) UNSIGNED NOT NULL,
    `media_id` BIGINT(20) UNSIGNED NOT NULL,
    `adresse` VARCHAR(255) COLLATE utf8mb4_unicode_ci NOT NULL,
    `localisation` VARCHAR(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
    `tel` VARCHAR(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
    `email` VARCHAR(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
    `horaire` VARCHAR(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
    `devise` VARCHAR(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
    `created_at` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
    `updated_at` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (`footer_id`),
    FOREIGN KEY (`user_id`) REFERENCES `users`(`user_id`) ON DELETE CASCADE,
    FOREIGN KEY (`media_id`) REFERENCES `media`(`media_id`) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS `accueil` (
    `accueil_id` BIGINT(20) UNSIGNED NOT NULL AUTO_INCREMENT,
    `user_id` BIGINT(20) UNSIGNED NOT NULL,
    `media_id` BIGINT(20) UNSIGNED NOT NULL,
    `projet_id` BIGINT(20) UNSIGNED NOT NULL,
    `news_id` BIGINT(20) UNSIGNED NOT NULL,
    `temoignage_id` BIGINT(20) UNSIGNED NOT NULL,
    `footer_id` BIGINT(20) UNSIGNED NOT NULL,
    `tchat_id` BIGINT(20) UNSIGNED NOT NULL,
    `description` LONGTEXT COLLATE utf8mb4_unicode_ci DEFAULT NULL,
    `created_at` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
    `updated_at` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (`accueil_id`),
    FOREIGN KEY (`user_id`) REFERENCES `users`(`user_id`) ON DELETE CASCADE,
    FOREIGN KEY (`media_id`) REFERENCES `media`(`media_id`) ON DELETE CASCADE,
    FOREIGN KEY (`footer_id`) REFERENCES `footer`(`footer_id`) ON DELETE CASCADE,
    FOREIGN KEY (`tchat_id`) REFERENCES `tchat`(`tchat_id`) ON DELETE CASCADE);

CREATE TABLE IF NOT EXISTS `album` (
    `album_id` BIGINT(20) UNSIGNED NOT NULL AUTO_INCREMENT,
    `title` VARCHAR(255) COLLATE utf8mb4_unicode_ci NOT NULL,
    `description` LONGTEXT COLLATE utf8mb4_unicode_ci DEFAULT NULL,
    `url` VARCHAR(255) COLLATE utf8mb4_unicode_ci NOT NULL,
    `type` VARCHAR(255) COLLATE utf8mb4_unicode_ci NOT NULL,
    `created_at` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
    `updated_at` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    `delete_at` TIMESTAMP NULL DEFAULT NULL,
    PRIMARY KEY (`album_id`),
    INDEX `idx_album_title` (`title`) -- Index pour accélérer les recherches par titre
);

CREATE TABLE IF NOT EXISTS `temoignage` (
    `temoignage_id` BIGINT(20) UNSIGNED NOT NULL AUTO_INCREMENT,
    `media_id` BIGINT(20) UNSIGNED NOT NULL,
    `user_id` BIGINT(20) UNSIGNED NOT NULL,
    `commentaire` LONGTEXT COLLATE utf8mb4_unicode_ci NOT NULL,
    `etoile` BIGINT(20) UNSIGNED NOT NULL,
`created_at` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
    `updated_at` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    `delete_at` TIMESTAMP NULL DEFAULT NULL,
    PRIMARY KEY (`temoignage_id`),
    FOREIGN KEY (`user_id`) REFERENCES `users`(`user_id`) ON DELETE CASCADE,
    FOREIGN KEY (`media_id`) REFERENCES `media`(`media_id`) ON DELETE CASCADE
);


CREATE TABLE IF NOT EXISTS `equipe` (
    `equipe_id` BIGINT(20) UNSIGNED NOT NULL AUTO_INCREMENT,
    `user_id` BIGINT(20) UNSIGNED NOT NULL,
    `service_id` BIGINT(20) UNSIGNED NOT NULL,
    `cellule_id` BIGINT(20) UNSIGNED NOT NULL,
    `media_id` BIGINT(20) UNSIGNED NOT NULL,
`created_at` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
    `updated_at` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    `delete_at` TIMESTAMP NULL DEFAULT NULL,
    PRIMARY KEY (`equipe_id`),
    FOREIGN KEY (`user_id`) REFERENCES `users`(`user_id`) ON DELETE CASCADE,
    FOREIGN KEY (`service_id`) REFERENCES `service`(`service_id`) ON DELETE CASCADE,
    FOREIGN KEY (`cellule_id`) REFERENCES `cellule`(`cellule_id`) ON DELETE CASCADE,
    FOREIGN KEY (`media_id`) REFERENCES `media`(`media_id`) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS `apropos` (
    `apropos_id` BIGINT(20) UNSIGNED NOT NULL AUTO_INCREMENT,
    `user_id` BIGINT(20) UNSIGNED NOT NULL,
    `partenaire_id` BIGINT(20) UNSIGNED NOT NULL,
    `titre` VARCHAR(255) COLLATE utf8mb4_unicode_ci NOT NULL,
    `sous_titre` VARCHAR(255) COLLATE utf8mb4_unicode_ci NOT NULL,
    `description` LONGTEXT COLLATE utf8mb4_unicode_ci DEFAULT NULL,
    `service_id` BIGINT(20) UNSIGNED NOT NULL,
    `created_at` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
    `updated_at` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (`apropos_id`),
    FOREIGN KEY (`user_id`) REFERENCES `users`(`user_id`) ON DELETE CASCADE,
    FOREIGN KEY (`partenaire_id`) REFERENCES `partenaire`(`partenaire_id`) ON DELETE CASCADE,
    FOREIGN KEY (`service_id`) REFERENCES `service`(`service_id`) ON DELETE CASCADE,
    INDEX idx_apropos_user (`user_id`),
    INDEX idx_apropos_partenaire (`partenaire_id`)
);


CREATE TABLE IF NOT EXISTS `service` (
    `service_id` BIGINT(20) UNSIGNED NOT NULL AUTO_INCREMENT,
    `user_id` BIGINT(20) UNSIGNED NOT NULL,
    `cellule_id` BIGINT(20) UNSIGNED NOT NULL,
    `equipe_id` BIGINT(20) UNSIGNED NOT NULL,
    `titre` VARCHAR(255) COLLATE utf8mb4_unicode_ci NOT NULL,
    `nom` VARCHAR(255) COLLATE utf8mb4_unicode_ci NOT NULL,
    `description` LONGTEXT COLLATE utf8mb4_unicode_ci DEFAULT NULL,
    `created_at` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
    `updated_at` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (`service_id`),
    FOREIGN KEY (`user_id`) REFERENCES `users`(`user_id`) ON DELETE CASCADE,
    FOREIGN KEY (`cellule_id`) REFERENCES `cellule`(`cellule_id`) ON DELETE CASCADE,
    FOREIGN KEY (`equipe_id`) REFERENCES `equipe`(`equipe_id`) ON DELETE CASCADE,
    INDEX idx_service_user (`user_id`),
    INDEX idx_service_cellule (`cellule_id`)
);


-- Table: commentaires
CREATE TABLE IF NOT EXISTS `commentaires` (
    `commentaire_id` BIGINT(20) UNSIGNED NOT NULL AUTO_INCREMENT,
    `user_id` BIGINT(20) UNSIGNED NOT NULL,
    `commentaire` LONGTEXT COLLATE utf8mb4_unicode_ci NOT NULL,
    `created_at` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
    `updated_at` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    `delete_at` TIMESTAMP NULL DEFAULT NULL,
    PRIMARY KEY (`commentaire_id`),
    FOREIGN KEY (`user_id`) REFERENCES `users`(`user_id`) ON DELETE CASCADE,
    INDEX idx_commentaires_user (`user_id`)
);

CREATE TABLE IF NOT EXISTS `media` (
    `media_id` BIGINT(20) UNSIGNED NOT NULL AUTO_INCREMENT,
    `user_id` BIGINT(20) UNSIGNED NOT NULL,
    `nom_file` VARCHAR(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
    `lien_file` VARCHAR(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
    `description` LONGTEXT COLLATE utf8mb4_unicode_ci DEFAULT NULL,
    `created_at` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
    `updated_at` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (`media_id`),
    FOREIGN KEY (`user_id`) REFERENCES `users`(`user_id`) ON DELETE CASCADE,
    INDEX idx_media_user (`user_id`)
);

CREATE TABLE IF NOT EXISTS `cellule` (
    `cellule_id` BIGINT(20) UNSIGNED NOT NULL AUTO_INCREMENT,
    `user_id` BIGINT(20) UNSIGNED NOT NULL,
    `service_id` BIGINT(20) UNSIGNED NOT NULL,
    `titre` VARCHAR(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
    `description` LONGTEXT COLLATE utf8mb4_unicode_ci DEFAULT NULL,
    `created_at` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
    `updated_at` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (`cellule_id`),
    FOREIGN KEY (`user_id`) REFERENCES `users`(`user_id`) ON DELETE CASCADE,
    FOREIGN KEY (`service_id`) REFERENCES `service`(`service_id`) ON DELETE CASCADE,
    INDEX idx_cellule_user (`user_id`),
    INDEX idx_cellule_service (`service_id`)
);


CREATE TABLE `webinaire` (
    `webinaire_id` BIGINT(20) UNSIGNED NOT NULL AUTO_INCREMENT,
    `user_id` BIGINT(20) UNSIGNED NOT NULL,
    `media_id` BIGINT(20) UNSIGNED NOT NULL,
    `titre` VARCHAR(255) COLLATE utf8mb4_unicode_ci NOT NULL,
    `sous_titre` VARCHAR(255) COLLATE utf8mb4_unicode_ci NOT NULL,
    `description` LONGTEXT COLLATE utf8mb4_unicode_ci DEFAULT NULL,
    `created_at` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
    `updated_at` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (`webinaire_id`),
    FOREIGN KEY (`user_id`) REFERENCES `users`(`user_id`) ON DELETE CASCADE,
    FOREIGN KEY (`media_id`) REFERENCES `media`(`media_id`) ON DELETE CASCADE,
    INDEX idx_webinaire_user (`user_id`),
    INDEX idx_webinaire_media (`media_id`)
);

CREATE TABLE IF NOT EXISTS `atelier` (
    `atelier_id` BIGINT(20) UNSIGNED NOT NULL AUTO_INCREMENT,
    `user_id` BIGINT(20) UNSIGNED NOT NULL,
    `media_id` BIGINT(20) UNSIGNED NOT NULL,
    `titre` VARCHAR(255) COLLATE utf8mb4_unicode_ci NOT NULL,
    `sous_titre` VARCHAR(255) COLLATE utf8mb4_unicode_ci NOT NULL,
    `description` LONGTEXT COLLATE utf8mb4_unicode_ci DEFAULT NULL,
    `created_at` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
    `updated_at` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (`atelier_id`),
    FOREIGN KEY (`user_id`) REFERENCES `users`(`user_id`) ON DELETE CASCADE,
    FOREIGN KEY (`media_id`) REFERENCES `media`(`media_id`) ON DELETE CASCADE,
    INDEX idx_atelier_user (`user_id`),
    INDEX idx_atelier_media (`media_id`)
);


CREATE TABLE `newsletter` (
    `news_id` BIGINT(20) UNSIGNED NOT NULL AUTO_INCREMENT,
    `user_id` BIGINT(20) UNSIGNED NOT NULL,
    `media_id` BIGINT(20) UNSIGNED NOT NULL,
    `album_id` BIGINT(20) UNSIGNED NOT NULL,
    `date_event` TIMESTAMP NULL DEFAULT NULL,
    `id_commentaire` BIGINT(20) UNSIGNED NOT NULL,
    `titre` VARCHAR(255) COLLATE utf8mb4_unicode_ci NOT NULL,
    `description` LONGTEXT COLLATE utf8mb4_unicode_ci DEFAULT NULL,
    `contenu` LONGTEXT COLLATE utf8mb4_unicode_ci DEFAULT NULL,
    `created_at` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
    `updated_at` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (`news_id`),
    FOREIGN KEY (`user_id`) REFERENCES `users`(`user_id`) ON DELETE CASCADE,
    FOREIGN KEY (`media_id`) REFERENCES `media`(`media_id`) ON DELETE CASCADE,
    FOREIGN KEY (`id_commentaire`) REFERENCES `commentaires`(`commentaire_id`) ON DELETE CASCADE,
    INDEX idx_newsletter_user (`user_id`),
    INDEX idx_newsletter_media (`media_id`),
    INDEX idx_newsletter_commentaire (`id_commentaire`)
);

CREATE TABLE `contact` (
    `contact_id` BIGINT(20) UNSIGNED NOT NULL AUTO_INCREMENT,
    `nom_prenom` VARCHAR(255) COLLATE utf8mb4_unicode_ci NOT NULL,
    `email` VARCHAR(255) COLLATE utf8mb4_unicode_ci NOT NULL,
    `contact` VARCHAR(255) COLLATE utf8mb4_unicode_ci NOT NULL,
    `sujet` VARCHAR(255) COLLATE utf8mb4_unicode_ci NOT NULL,
    `contenu` LONGTEXT COLLATE utf8mb4_unicode_ci DEFAULT NULL,
    `created_at` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
    `updated_at` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (`contact_id`),
    INDEX idx_contact_email (`email`)
);


CREATE TABLE `partenaire` (
    `partenaire_id` BIGINT(20) UNSIGNED NOT NULL AUTO_INCREMENT,
    `nom` VARCHAR(255) COLLATE utf8mb4_unicode_ci NOT NULL,
    `created_at` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
    `updated_at` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (`partenaire_id`),
    INDEX idx_partenaire_nom (`nom`)
);

CREATE TABLE `projets` (
    `projet_id` BIGINT(20) UNSIGNED NOT NULL AUTO_INCREMENT,
    `user_id` BIGINT(20) UNSIGNED NOT NULL,
    `media_id` BIGINT(20) UNSIGNED NOT NULL,
    `nom_projet` VARCHAR(255) COLLATE utf8mb4_unicode_ci NOT NULL,
    `etat` ENUM('non démarré', 'en cours', 'terminé') NOT NULL COMMENT '0 = non démarré, 1 = en cours, 2 = terminé',
    `description` LONGTEXT COLLATE utf8mb4_unicode_ci DEFAULT NULL,
    `created_at` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
    `updated_at` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (`projet_id`),
    FOREIGN KEY (`user_id`) REFERENCES `users`(`user_id`) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (`media_id`) REFERENCES `media`(`media_id`) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Table: logs
CREATE TABLE `logs` (
    `id_log` BIGINT(20) UNSIGNED NOT NULL AUTO_INCREMENT,
    `user_id` BIGINT(20) UNSIGNED NOT NULL,
    `date_log` DATE NOT NULL,
    `type` VARCHAR(255) COLLATE utf8mb4_unicode_ci NOT NULL,
    `action` VARCHAR(255) COLLATE utf8mb4_unicode_ci NOT NULL,
    `created_at` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
    `updated_at` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (`id_log`),
    FOREIGN KEY (`user_id`) REFERENCES `users`(`user_id`) ON DELETE CASCADE
);
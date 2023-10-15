DROP TABLE IF EXISTS [Evenements];
DROP TABLE IF EXISTS [TypesEvenements];
DROP TABLE IF EXISTS [Utilisateurs];
-- --------------------------------------------------------

--
-- Structure de la table TypesEvenements
--

CREATE TABLE [TypesEvenements] (
  [id] INTEGER NOT NULL,
  [type] VARCHAR(255) NOT NULL UNIQUE,
  CONSTRAINT [PK_TypesEvenements] PRIMARY KEY ([id])
);

-- --------------------------------------------------------

--
-- Structure de la table Utilisateurs
--

CREATE TABLE [Utilisateurs] (
  [id] INTEGER NOT NULL,
  [pseudo] VARCHAR(255) NOT NULL UNIQUE,
  [pwd] VARCHAR(255) NOT NULL UNIQUE,
  CONSTRAINT [PK_Utilisateurs] PRIMARY KEY ([id])
);

-- --------------------------------------------------------

--
-- Structure de la table Evenements
--

CREATE TABLE [Evenements] (
  [id] INTEGER NOT NULL,
  [date] timestamp NOT NULL,
  [typeId] INTEGER NOT NULL,
  [userId] INTEGER NOT NULL,
  CONSTRAINT [PK_Evenements] PRIMARY KEY ([id]),
  FOREIGN KEY ([typeId]) REFERENCES [TypesEvenements] ([id])
    ON DELETE CASCADE ON UPDATE CASCADE,
  FOREIGN KEY ([userId]) REFERENCES [Utilisateurs] ([id])
   ON DELETE CASCADE ON UPDATE CASCADE
);

-------------------------------------------------------

--
-- Index pour les clés étrangères
--

--
-- Index pour la table Evenements
--
CREATE INDEX [IFK_TypesEvenement] ON [Evenements] ([typeId]);
CREATE INDEX [IFK_Utilisateurs] ON [Evenements] ([userId]);
-- --------------------------------------------------------

--
-- Données de la table TypesEvenements
--
INSERT INTO TypesEvenements ('type') VALUES ('Intrusion'), ('Arrêt'), ('Démmarage');

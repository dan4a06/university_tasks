CREATE TABLE люди (
люди_id integer GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
фамилия varchar(20) NOT NULL,
имя varchar(20) NOT NULL,
отчество varchar(20)
);

CREATE TABLE город (
город_id integer GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
город varchar(20) NOT NULL UNIQUE
);

CREATE TABLE топинг (
топинг_id integer GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
топинг varchar(50) NOT NULL UNIQUE,
цена_за_единицу numeric(5, 2) NOT NULL CHECK (цена_за_единицу >= 0)
);

CREATE TABLE напиток (
напиток_id integer GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
наазвание varchar(20) NOT NULL,
объём_кофе numeric(5, 2) NOT NULL CHECK (объём_кофе >= 0),
объём_молока numeric(5,2) NOT NULL CHECK (объём_молока >= 0),
цена numeric(8, 2) NOT NULL CHECK (цена > 0)
);

CREATE TABLE обжарка (
обжарка_id integer GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
название varchar(30) NOT NULL UNIQUE
);

CREATE TABLE место_сбора (
место_сбора_id integer GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
название varchar(30) NOT NULL UNIQUE
);

CREATE TABLE производитель (
производитель_id integer GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
название VARCHAR(150) NOT NULL UNIQUE
);

CREATE TABLE молоко (
молоко_id integer GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
молоко varchar(100) NOT NULL UNIQUE,
цена numeric(5, 2) NOT NULL CHECK (цена >= 0)
);

-- -------------------

CREATE TABLE кофейня (
кофейня_id integer GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
город_id integer NOT NULL REFERENCES город (город_id)
);

CREATE TABLE клиенты (
клиент_id integer PRIMARY KEY REFERENCES люди (люди_id),
скидка numeric(5, 2) NOT NULL DEFAULT 0 CHECK (скидка >= 0 AND скидка <= 100)
);

CREATE TABLE бариста (
бариста_id integer PRIMARY KEY REFERENCES люди (люди_id),
кофейня_id integer NOT NULL REFERENCES кофейня (кофейня_id),
дата_трудоустройства date NOT NULL UNIQUE 
);

CREATE TABLE зерно (
зерно_id integer GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
производитель_id integer NOT NULL REFERENCES производитель (производитель_id),
обжарка_id integer NOT NULL REFERENCES обжарка (обжарка_id),
место_сбора_id integer NOT NULL REFERENCES место_сбора (место_сбора_id),
название varchar(150) NOT NULL,
дата_сбора date NOT NULL,
дата_обжарки date NOT NULL CHECK (дата_обжарки >= дата_сбора)
); 

-- -------------------

CREATE TABLE заказ (
заказ_id integer GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
клиент_id integer NOT NULL REFERENCES клиенты (клиент_id),
бариста_id integer NOT NULL REFERENCES бариста (бариста_id),
дата_заказа date NOT NULL DEFAULT CURRENT_DATE,
время_заказа time NOT NULL DEFAULT CURRENT_TIME
);

CREATE TABLE спецификация_заказа (
спецификация_заказа_id integer GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
напиток_id integer NOT NULL REFERENCES напиток (напиток_id),
заказ_id integer NOT NULL REFERENCES заказ (заказ_id) ON DELETE CASCADE,
зерно_id integer NOT NULL REFERENCES зерно (зерно_id),
молоко_id integer NOT NULL REFERENCES молоко (молоко_id)
);

CREATE TABLE спецификация_топинг (
спецификация_топинг_id integer GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
топинг_id integer NOT NULL REFERENCES топинг (топинг_id),
спецификация_заказа_id integer NOT NULL REFERENCES спецификация_заказа (спецификация_заказа_id) ON DELETE CASCADE,
кол_во integer NOT NULL DEFAULT 1 CHECK (кол_во > 0)
);
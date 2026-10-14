CREATE TABLE IF NOT EXISTS cars(
    "id" SERIAL PRIMARY KEY,
    "make" VARCHAR(50) NOT NULL,
    "model" VARCHAR(50) NOT NULL,
    "year_produced" INTEGER NOT NULL,
    "country" VARCHAR(50) NOT NULL,
    "price" NUMERIC(15, 2) NOT NULL,
    "body_type" VARCHAR(15) DEFAULT'Седан',
    "description" TEXT,
    CONSTRAINT year_produced_check CHECK ("year_produced" > 1800 AND "year_produced" <= 2100),
    CONSTRAINT price_is_positive_check CHECK ("price" > 0),
    CONSTRAINT body_type_check CHECK ("body_type" in ('Седан', 'Универсал', 'Внедорожник', 'Хэтчбек'))
);

CREATE TABLE IF NOT EXISTS car_specifications(
    "id" SERIAL PRIMARY KEY,
    "car_id" INTEGER NOT NULL UNIQUE,
    "fuel_type" VARCHAR(10) DEFAULT 'Бензин',
    "engine_volume" NUMERIC(2, 1) NOT NULL,
    "drive_type" VARCHAR(10) DEFAULT 'Передний',
    "transmission" VARCHAR(15) DEFAULT 'Механическая',
    "horsepower" INTEGER NOT NULL,
    CONSTRAINT fuel_type_check CHECK ("fuel_type" IN ('Бензин', 'Дизель', 'Электро', 'Гибрид')),
    CONSTRAINT drive_type_check CHECK ("drive_type" IN ('Передний', 'Задний', 'Полный')),
    CONSTRAINT transmission_check CHECK ("transmission" IN ('Автоматическая', 'Механическая', 'Робот')),
    CONSTRAINT engine_volume_not_negative CHECK ("engine_volume" >= 0),
    CONSTRAINT horsepower_is_positive CHECK ("horsepower" > 0),
    CONSTRAINT car_specifications_cars_FK FOREIGN KEY ("car_id") REFERENCES cars("id") ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS users(
    "id" SERIAL PRIMARY KEY,
    "username" VARCHAR(50) NOT NULL UNIQUE,
    "password_hash" VARCHAR(255) NOT NULL,
    "registration_date" TIMESTAMPTZ DEFAULT CURRENT_DATE,
    "login_date" TIMESTAMPTZ DEFAULT CURRENT_DATE,
    "role" VARCHAR(10) DEFAULT 'USER',
    "is_blocked" BOOLEAN DEFAULT False,
    CONSTRAINT role_check CHECK ("role" IN ('SUPER', 'ADMIN', 'MANAGER', 'USER'))
);

CREATE TABLE IF NOT EXISTS user_data(
    "id" SERIAL PRIMARY KEY,
    "user_id" INTEGER NOT NULL UNIQUE,
    "last_name" VARCHAR(50),
    "middle_name" VARCHAR(50),
    "first_name" VARCHAR(50),
    "birth_date" DATE,
    CONSTRAINT birth_date_check CHECK (EXTRACT(YEAR FROM AGE(CURRENT_DATE, "birth_date")) >= 18),
    CONSTRAINT user_data_users_FK FOREIGN KEY ("user_id") REFERENCES users("id") ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS orders(
    "id" SERIAL PRIMARY KEY,
    "car_id" INTEGER NOT NULL,
    "user_id" INTEGER NOT NULL,
    "manager_id" INTEGER NOT NULL,
    "status" VARCHAR(15) DEFAULT 'В обработке',
    CONSTRAINT status_check CHECK ("status" IN ('В обработке', 'Завершено', 'Отказано', 'Тест-драйв')),
    CONSTRAINT orders_cars_FK FOREIGN KEY ("car_id") REFERENCES cars("id") ON DELETE CASCADE on UPDATE CASCADE,
    CONSTRAINT orders_users_FK FOREIGN KEY ("user_id") REFERENCES users("id") ON DELETE CASCADE on UPDATE CASCADE,
    CONSTRAINT orders_managers_FK FOREIGN KEY ("manager_id") REFERENCES users("id") ON DELETE CASCADE on UPDATE CASCADE
);
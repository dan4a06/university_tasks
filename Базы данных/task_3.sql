-- 1. Получить все кортежи из таблицы Товаров, где цена больше 10
SELECT * FROM afanasiev342.part WHERE price > 10;

-- 2. Получите только цену и название товаров, цена которых с 15% наценкой меньше 15.
SELECT part_name, price
FROM afanasiev342.part
WHERE price * 1.15 < 15;

-- 3. Название и цвет товара, где название товара Bolt или цена товара меньше 15.
SELECT part_name, color
FROM afanasiev342.part
WHERE part_name = 'Bolt' OR price < 15;

-- 4. Название деталей и их стоимость с 30% наценкой (столбец price переименован),
--    только кортежи, где цена с наценкой не ниже 15.
SELECT part_name, price * 1.3 AS new_price
FROM afanasiev342.part
WHERE price * 1.3 >= 15;

-- 5. Цена детали попадает в интервал [10,20], строки по убыванию цены детали.
SELECT *
FROM afanasiev342.part
WHERE price BETWEEN 10 AND 20
ORDER BY price DESC;

-- 6. Имена поставщиков, начинающихся с буквы 'B'.
SELECT supplier_name
FROM afanasiev342.supplier
WHERE supplier_name LIKE 'B%';

-- 7. Поставщики из Лондона или Парижа в алфавитном порядке.
SELECT *
FROM afanasiev342.supplier
WHERE city IN ('London', 'Paris')
ORDER BY supplier_name ASC;

-- 8. Количество типов деталей, хранящихся в таблице PART.
SELECT COUNT(*) AS part_types
FROM afanasiev342.part;

-- 9. Средний вес деталей.
SELECT AVG(weight) AS avg_weight
FROM afanasiev342.part;

-- 10. Минимальная, максимальная и средняя стоимости продаваемых деталей.
SELECT MIN(price) AS min_price,
       MAX(price) AS max_price,
       AVG(price) AS avg_price
FROM afanasiev342.part;

-- 11. Сколько имеется поставщиков из Парижа?
SELECT COUNT(*) AS paris_suppliers
FROM afanasiev342.supplier
WHERE city = 'Paris';

-- 12. Суммарная стоимость красных деталей.
--     (В task_2.sql цвет уже переведён в слова: 'Red'. Если запускать до задания 12 из task_2,
--      то условие должно быть color = 'R'.)
SELECT SUM(price) AS total_red_price
FROM afanasiev342.part
WHERE color = 'Red';
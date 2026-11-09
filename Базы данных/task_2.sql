-- 1. Например, попробуйте обновить значение цены товара cam.
UPDATE afanasiev342.part SET price=30 WHERE part_name='Cam';

-- 2. затем значение цены и цвета товара Nut
UPDATE afanasiev342.part SET price=10, color='R' WHERE part_name='Nut';

-- 3. и название поставщика из Парижа
UPDATE afanasiev342.supplier SET supplier_name='Kirill' WHERE city='Paris';

-- 4. Удалите из таблицы товаров товар bearing (в данных он записан как 'Bering').
DELETE FROM afanasiev342.part WHERE part_name='Bering';

-- 5. Проконтролируйте выполнение операции.
SELECT * FROM afanasiev342.part;
SELECT * FROM afanasiev342.sells;
-- Ответ: в sells внешний ключ part_ID объявлен с ON DELETE CASCADE,
-- поэтому при удалении товара автоматически удалились все строки sells с этим part_ID (sells_ID 6 и 10).

-- 6. Добавьте в БД поставщика из Москвы по имени Alex, поставляющего детали Screw и Cam.
INSERT INTO afanasiev342.supplier(supplier_ID, supplier_name, city)
	VALUES (5, 'Alex', 'Moscow');
INSERT INTO afanasiev342.sells(sells_ID, supplier_ID, part_ID)
	VALUES (11, 5, 1), (12, 5, 4);

SELECT * FROM afanasiev342.supplier;
SELECT * FROM afanasiev342.sells;

-- 7. Удалите его из списка поставщиков, проконтролировав состояние таблицы Sells.
DELETE FROM afanasiev342.supplier WHERE supplier_name='Alex';

SELECT * FROM afanasiev342.supplier;
SELECT * FROM afanasiev342.sells;
-- В sells строки 11 и 12 остались, но supplier_ID стал NULL (ON DELETE SET NULL).

-- 8. Добавьте в таблицу SUPPLIER колонки с телефонами и контактными лицами. Заполните колонки.
ALTER TABLE afanasiev342.supplier ADD COLUMN phone varchar(20);
ALTER TABLE afanasiev342.supplier ADD COLUMN contact_person varchar(30);

UPDATE afanasiev342.supplier SET phone='+77771111111', contact_person='John' WHERE supplier_ID=1;
UPDATE afanasiev342.supplier SET phone='+78882222222', contact_person='Pierre' WHERE supplier_ID=2;
UPDATE afanasiev342.supplier SET phone='+79993333333', contact_person='Hans' WHERE supplier_ID=3;
UPDATE afanasiev342.supplier SET phone='+76664444444', contact_person='Marco' WHERE supplier_ID=4;

-- 9. Удалите из таблицы поставщиков колонку с контактными лицами.
ALTER TABLE afanasiev342.supplier DROP COLUMN contact_person;

-- 10. Переименуйте колонку, содержащую телефон.
ALTER TABLE afanasiev342.supplier RENAME COLUMN phone TO phone_number;

-- 11. Не должно быть поставщиков с неопределёнными телефонами.
ALTER TABLE afanasiev342.supplier ALTER COLUMN phone_number SET NOT NULL;

-- 12. Измените домен атрибута цвет (char -> varchar(10), цвета записываем словами).
ALTER TABLE afanasiev342.part DROP CONSTRAINT part_color_check;
ALTER TABLE afanasiev342.part ALTER COLUMN color TYPE varchar(10);
UPDATE afanasiev342.part SET color='Red'   WHERE color='R';
UPDATE afanasiev342.part SET color='Green' WHERE color='G';
UPDATE afanasiev342.part SET color='Blue'  WHERE color='B';
ALTER TABLE afanasiev342.part ADD CHECK (color IN ('Red', 'Green', 'Blue'));

SELECT * FROM afanasiev342.part;

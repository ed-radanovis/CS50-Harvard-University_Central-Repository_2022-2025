-- Find the crime report on Humphrey Street dated July 28, 2024.
SELECT *
FROM crime_scene_reports
WHERE year = 2024 AND month = 7 AND day = 28
AND street = 'Humphrey Street';

-- Seeking interviews with witnesses on the day of the crime (July 28, 2024)
SELECT *
FROM interviews
WHERE year = 2024 AND month = 7 AND day = 28;

-- Look for exits from the bakery parking lot between 10:15 and 10:25
SELECT *
FROM bakery_security_logs
WHERE year = 2024 AND month = 7 AND day = 28
AND hour = 10
AND minute BETWEEN 15 AND 25
AND activity = 'exit';

-- Withdrawals at the Leggett Street ATM on July 28, 2024
SELECT *
FROM atm_transactions
WHERE year = 2024 AND month = 7 AND day = 28
AND atm_location = 'Leggett Street'
AND transaction_type = 'withdraw';

-- Phone calls on July 28th lasting less than 1 minute (60 seconds)
SELECT *
FROM phone_calls
WHERE year = 2024 AND month = 7 AND day = 28
AND duration < 60;

-- First flight of the day 29/7/2024 (as early as possible)
SELECT *
FROM flights
WHERE year = 2024 AND month = 7 AND day = 29
ORDER BY hour, minute
LIMIT 1;


-- Cross-referencing data to identify the thief.


-- CLUE 1: Find destination city of flight 36
SELECT city
FROM airports
WHERE id = 4;

-- CLUE 2: Passengers on flight 36
SELECT *
FROM passengers
WHERE flight_id = 36;

-- CLUE 3: People with suspicious license plates (bakery parking lot)
SELECT *
FROM people
WHERE license_plate IN (
    '5P2BI95', '94KL13X', '6P58WS2', '4328GD8',
    'G412CB7', 'L93JTIZ', '322W7JE', '0NTHK55'
);

-- CLUE 4: People with suspicious bank accounts (ATM withdrawals)
SELECT people.*
FROM people
JOIN bank_accounts ON people.id = bank_accounts.person_id
WHERE bank_accounts.account_number IN (
    28500762, 28296815, 76054385, 49610011,
    16153065, 25506511, 81061156, 26013199
);

-- CLUE 5: People who made suspicious phone calls (duration < 60s)
SELECT *
FROM people
WHERE phone_number IN (
    '(130) 555-0289', '(499) 555-9472', '(367) 555-5533',
    '(499) 555-9472', '(286) 555-6063', '(770) 555-1861',
    '(031) 555-6622', '(826) 555-1652', '(338) 555-6650'
);


-- Determine a pattern to find the accomplice.


-- Find the accomplice (receiver of Bruce's call)
SELECT name
FROM people
WHERE phone_number = '(375) 555-8161';

-- Confirm destination city name for flight 36
SELECT full_name, city
FROM airports
WHERE id = 4;

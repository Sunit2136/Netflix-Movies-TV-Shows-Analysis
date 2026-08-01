-- Create Database
CREATE DATABASE netflix_db;
USE netflix_db;

-- View Dataset
SELECT * FROM netflix_titles;

-- Total Records
SELECT COUNT(*) AS Total_Titles
FROM netflix_titles;

-- Movies vs TV Shows
SELECT type, COUNT(*) AS Total
FROM netflix_titles
GROUP BY type;

-- Top 10 Ratings
SELECT rating, COUNT(*) AS Total
FROM netflix_titles
GROUP BY rating
ORDER BY Total DESC
LIMIT 10;

-- Top 10 Countries
SELECT country, COUNT(*) AS Total
FROM netflix_titles
WHERE country IS NOT NULL
GROUP BY country
ORDER BY Total DESC
LIMIT 10;

-- Movies Released Each Year
SELECT release_year, COUNT(*) AS Total
FROM netflix_titles
GROUP BY release_year
ORDER BY release_year;

-- Top 10 Longest Movies
SELECT
    title,
    CAST(REPLACE(duration,' min','') AS UNSIGNED) AS Duration_Minutes
FROM netflix_titles
WHERE type='Movie'
AND duration LIKE '%min%'
ORDER BY Duration_Minutes DESC
LIMIT 10;

-- Titles with Rating PG-13
SELECT title, rating
FROM netflix_titles
WHERE rating='PG-13';

-- Titles Released After 2018
SELECT title, release_year
FROM netflix_titles
WHERE release_year > 2018;

-- Average Release Year
SELECT AVG(release_year) AS Average_Year
FROM netflix_titles;

-- Earliest and Latest Release Year
SELECT
MIN(release_year) AS Earliest,
MAX(release_year) AS Latest
FROM netflix_titles;

-- Missing Directors
SELECT *
FROM netflix_titles
WHERE director IS NULL;

-- Top 10 Directors
SELECT director, COUNT(*) AS Total
FROM netflix_titles
WHERE director IS NOT NULL
GROUP BY director
ORDER BY Total DESC
LIMIT 10;
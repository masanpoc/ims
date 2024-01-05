base_queries = {
    "insert": """
INSERT INTO clothes
(id, item, category, season, use, quality, state, activity, rating, removable,
brand, year, metadata, sport)
VALUES %s;
""",
    # TO DO: update metadata
    "update": """
UPDATE clothes
SET item = %s, category = %s, season = %s, use = %s, quality = %s, state = %s,
activity = %s, rating = %s, removable = %s, brand = %s, year = %s,
metadata = %s, sport = %s,
WHERE id = %s;
""",
    "select": """
SELECT id FROM clothes WHERE id = ANY(%s);
""",
}

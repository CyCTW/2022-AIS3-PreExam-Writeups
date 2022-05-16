# Cat Emoji Database
- Category: Web
- Tag: `medium`
- Final Score: 487
- Solve: 15/292

## Writeups :eyes:
### Observation
- We can get source code from `/source`.
- We can do sql injection on `api/emoji/<unicode>` API.
    - However, the backend server will trim whitespace.
    - And, We can't use `/**/` to replace whitespace in sql query because `flask` framework see `/` as a delimiter in routing rules.
### Exploit
We can use brackets to make a exploit. First, we can try `/api/emoji/(-1)UNION((SELECT(1),(2),(3),(4),(5)))` and we found that the server display information.

Then, we should identify which database the server used.
After some experiments, the payload `/api/emoji/(-1)UNION((SELECT(1),(2),(3),DB_NAME(0),(5)))` can display correctly. The function `DB_NAME(0)` is from MSSQL. 

Furthermore, we can print the database version by `/api/emoji/(-1)UNION((SELECT(1),(2),(3),@@version,(5)))`, which is `Microsoft Azure SQL Edge Developer (RTM) - 15.0.2000.1562 (X64)`.

Finally, we try to build payload that can leak table name and column name.(Detailed in `solve.py`)
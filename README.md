# Notes - Telegram Bot
***Простой Telegram Bot, написанный на Python3+AIOgram+SQLite3.***

Бот позволяет создавать простые заметки, классифицировать их по важности и отображать события на текущий и следующий день. Для запуска в **config.py** укажите свой токен бота и запустите файл **notes_bot.py**.
## Скриншоты:
![Иллюстрация к проекту](https://blogger.googleusercontent.com/img/a/AVvXsEiS22nKEnk_wOC5fu2RuPA8rsajD7tYTsV1pAAyQ13D6kIpnIT9W7J7ihSPp2nDJkrKix0JeBwQ9lLHUfxvH1d5Vvi7AXYY84YlVKEpAzQjrHla9ooYDIhQwmO2_a_NdClD5-9i0-k-Ty1KXpD8qKjPdpW07Hdptqt9MKYxm3QrqBo74qfFaR7D60zopA=s400) ![Иллюстрация к проекту](https://blogger.googleusercontent.com/img/a/AVvXsEghzJjCC4Z-74lMrcWdPCKWWNLBYU0liXze6MNRMnM_g8zBedlJXJe229dXhqvZedNIL12cP-dn-TT7fxr1WTEtDm0yO9wlCr8Z0Sgya26WTc-s46xeH6YS4b3r_CqE1lvQcqNyT5pfe0bly_RaO0AzzXfkSQkTTpKMxkDmZI5VS3b6kRqDDNhzNtv_6Q=w295-h400) 
![Иллюстрация к проекту](https://blogger.googleusercontent.com/img/a/AVvXsEgy3mQ69Pp7XIGKF33ujXBa_nsiinb7JNIHmcfj7huO6JOamoL6Qet6JYjHcIbrMnnCqi-8EQfNZXvGdR6Rux36isfKcn926jZbdd9aCqkrJazFqYNeLORkK4TCQ7miX9AGFD15V4IdtE-WHNSTw52_l2g_jzKsRIUi-0Ng6uaBB_eszR_7hlrWN8YasQ=s400) ![Иллюстрация к проекту](https://blogger.googleusercontent.com/img/a/AVvXsEjDKhn6CDasAQ-6yDPHIPEoKPCp8R_BxiAqCJ8HLw9I9VUX9VnkkdHRReKxFRXoF8XuN1zISU8tS-QJK0d8uZGpHockT_WKUzak-CJ7rzI-SZDLMjiYVYIR4kVQG1hyf0NjC2Iz-hiZMnOmvf3bXM4dpl0X7FPyM-pUY-ieqiC0jao-sJV6m2iNjUa-ew=s400)
## Структура БД:
```sql
BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "users" (
	"id"	INTEGER NOT NULL,
	"tg"	INTEGER NOT NULL,
	"name"	INTEGER,
	PRIMARY KEY("id")
);
CREATE TABLE IF NOT EXISTS "notes" (
	"id"	INTEGER NOT NULL,
	"userid"	INTEGER NOT NULL,
	"date"	INTEGER,
	"time"	INTEGER,
	"notes"	TEXT,
	"imp"	INTEGER DEFAULT 0,
	PRIMARY KEY("id")
);
COMMIT;

```

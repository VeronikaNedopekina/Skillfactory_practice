Автоматизированное тестирование сайта: https://b2c.passport.rt.ru с использованием PyTest и Selenium. 

Ссылка на обновленные требования https://docs.google.com/document/d/1HJDsO8VI45BTVcRKL-gQjSP8mGLUKKZY/edit?usp=share_link&ouid=103194071242773299841&rtpof=true&sd=true

В рамках реализации проекта тестирования формы авторизации выполнено:
Smoke-тестирование, ручное тестирование, автотестирование с помощью Python, Selenium, позитивное/негативное/деструктивное тестирование.
доменное тестирование, разделение на классы эквивалентности, анализ граничных значений - данные техники позволяют уменьшить количество проводимых тестов для проверки валидных и невалидных значений полей ввода в формах Авторизации и Регистрации.
Применение сценариев использования (user cases), "предугадывание ошибок" позволяет проверить наиболее распостранненные ошибки пользователей, полный путь использования форм сайта пользователем.
Проведено функциональное тестирование (формы Регистрация, Авторизация).

В папке tests в файле tests.py находятся тесты.
В файле settings.py указаны валидные данные, применяемые для тестирования

Для запуска автотестов необходимо:
Установить все библиотеки из файла requirements.txt командой: pip install -r requirements.txt
Запуск тестов в терминале: pytest -v -s -q --driver Chrome --driver-path <путь>/chromedriver.exe tests.py

Не удалось реализовать ряд тестов из-за наличия Captcha.

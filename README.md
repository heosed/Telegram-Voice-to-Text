# Telegram-Voice-to-Text
Юзер-Апи бот телеграма написанный на Telethon, для конвертации голосовых сообщений в текст на ходу

Необходимые питон-либы:
  1. Telethon
  2. CrypTG
  3. SpeechRecognition

Как пользоваться:
  1. Логенимся на https://my.telegram.org/auth
  2. Созаём Приложение на https://my.telegram.org/apps
  3. Выписываем оттуда API_ID и API_HASH, и вставляем в main.py
  4. Скачиваем ffmpeg с https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-full.7z(или с https://www.ffmpeg.org/download.html)
  5. Распаковываем из папки bin/ файл ffmpeg.exe в папку с ботом
  6. При первом запуске, создаёться сессия, и больше логениться не надо
  7. Что-бы перевести голосовое сообщение\круглое видео в текст, надо ответить на него .v(Настраиваеться в коде)

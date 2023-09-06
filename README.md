# WE ARE MIGRATING TO https://github.com/GigaChatTeam AND REPOSITORIES ARE NOW SEPARATED
## Для наших дорогих разрабов: всю вашу работу необходимо перенести на соответствующий репозиторий на новом аккаунте. Пока права доступа настраиваем, но по-идее новый репозиторий могут создать все. Перед тем, как создавать новый, проверьте, создали ли его за вас

## TODO:
* разработать серверную хэш-функцию 

### ТЕРМИНЫ
* AA - Account Authorization - Авторизация Аккаунта - Сервера этого типа отвечают за внешную обработку токенов, регеистрацию аккаунтов, и генерацию токенов доступа к ним.
* CDN - Content Delevery Network - Сеть Доставки Контекта - Сервера этого типа отвечают за обмен команд и с пользователями, и при необходимости пересылку на CC-сервера.
* NCC - No Central Control - Без Центрального Контроля - Сервера этого типа может скачать и запустить любой человек. Данные сервера целиком и полностью лежат в его зоне ответственности. Могут использовать CDN-сервера для проксирования, если не нарушают правила. Иначе, только прямое подключение от клиента.
* CC  - Central Core - Центральное Ядро - Сервера этого типа хранят локализованные и централизованные данные, отвечают за приём команд от CDN-серверов, и при необходимости, пересылку другим CDN-серверам.
* FT - Files Transmitting - Транспортировка Файлов - Сервера этого типа отвечают за работу с динамическими пользовательскими файлами.
* TTG - Time-Tokens Generator - Генератор Временных Токенов - Сервера этого типа отвечают за генерацию и валидацию временных и ограниченных токенов доступа к внутренним и внешним сервисам аккаунта пользователя.
* RTC - Real-Time Communications - Коммуникация в Реальном Времени - Сервера обработки датаграмм пользователей.

# General info
Our goal is to combine the advantages of all the most popular social networks in one application, while keeping off their disadvantages. Also, for the sake of performance, we develop in native code for each platform. Of course, it is highly unlikely that someone would be interested in a school project, but we welcome any sort of help ;)

# Installation
While components are not ready, we advice against trying to install anything

## Server
--no information--

## Linux client
### Build prerequisites:
- Of course, linux
- Qt 6 or higher
- g++ compiler
- GNU make 
- GHC Haskell compiler (not necessary yet)
- ghc-static (not necessary yet)
- patience

### Build steps: 
1. clone the repository & navigate to GigaChat/client/desktop/linux-x11/source
2. `haskell/build-shared.sh` or `cd haskell && ghc -dynamic -shared -fPIE <did not finish the command lol>`  (not necessary yet)
3. run `qmake GigaQt.pro && make`
4. Pray. for it to work.

## Windows client
--no information--

## Android client
--no information--


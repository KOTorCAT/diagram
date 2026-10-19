# Прототип интерфейса: Панель обработки и поиска документов

```mermaid
flowchart TB
    subgraph Header["Шапка системы"]
        Logo["📄 DocSearch"]
        UserInfo["👤 Аналитик: Иван Петров"]
        Logout["🚪 Выйти"]
    end

    subgraph SearchBar["Поисковая строка"]
        Input["🔍 Введите запрос..."]
        Filters["⚙️ Фильтры: дата, тип, сущности"]
        BtnSearch["Найти"]
    end

    subgraph Actions["Действия"]
        BtnUpload["📤 Загрузить документ"]
        BtnRules["🛡️ Правила обезличивания"]
    end

    subgraph DocTable["Список документов"]
        Table["Таблица: Название | Статус | Дата | Действия"]
        Row1["Договор_001.pdf | ✅ INDEXED | 12.05.2025"]
        Row2["Акт_002.docx | ⏳ EXTRACTING | 12.05.2025"]
        Row3["Скан_003.pdf | ❌ FAILED | 11.05.2025"]
    end

    subgraph Results["Результаты поиска"]
        ResList["Список результатов с сниппетами"]
    end

    Header --> SearchBar
    SearchBar --> Actions
    Actions --> DocTable
    DocTable --> Results

    BtnUpload -.->|клик| UploadModal["Модальное окно загрузки файла"]
    BtnRules -.->|клик| RulesModal["Модальное окно настройки правил"]
    Row1 -.->|клик| DocDetail["Карточка документа: текст, сущности, подсветка"]
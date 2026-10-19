"""
Сгенерированный код по диаграмме классов ВКР:
«Разработка веб-системы для автоматизированной обработки,
структурирования и поиска информации в обезличенных электронных документах».

Код получен из diagrams/class_diagram.puml с помощью puml2code
и дополнен демонстрационным сценарием.
"""

from enum import Enum
from datetime import date
from typing import List, Optional


# ---------------------------------------------------------------------------
# Перечисления
# ---------------------------------------------------------------------------

class Role(Enum):
    ADMIN = "ADMIN"
    ANALYST = "ANALYST"
    USER = "USER"


class DocumentStatus(Enum):
    UPLOADED = "UPLOADED"
    DEPERSONALIZING = "DEPERSONALIZING"
    DEPERSONALIZED = "DEPERSONALIZED"
    EXTRACTING = "EXTRACTING"
    EXTRACTED = "EXTRACTED"
    STRUCTURING = "STRUCTURING"
    STRUCTURED = "STRUCTURED"
    INDEXING = "INDEXING"
    INDEXED = "INDEXED"
    FAILED = "FAILED"


# ---------------------------------------------------------------------------
# Основные классы
# ---------------------------------------------------------------------------

class User:
    def __init__(self, id: int, login: str, password_hash: str,
                 full_name: str, email: str, role: Role):
        self.id = id
        self.login = login
        self.password_hash = password_hash
        self.full_name = full_name
        self.email = email
        self.role = role

    def login(self):
        pass

    def logout(self):
        pass

    def has_permission(self, permission: str) -> bool:
        return False


class Document:
    def __init__(self, id: int, title: str, original_file_name: str,
                 file_path: str, mime_type: str, size: int):
        self.id = id
        self.title = title
        self.original_file_name = original_file_name
        self.file_path = file_path
        self.mime_type = mime_type
        self.size = size
        self.upload_date = date.today()
        self.status = DocumentStatus.UPLOADED
        self.text_content = ""
        self.depersonalized = False
        self.entities: List['ExtractedEntity'] = []
        self.tasks: List['ProcessingTask'] = []
        self.applied_rules: List['DepersonalizationRule'] = []

    def upload(self):
        self.status = DocumentStatus.UPLOADED

    def depersonalize(self):
        self.depersonalized = True
        self.status = DocumentStatus.DEPERSONALIZED

    def extract_text(self):
        self.text_content = "[извлечённый текст документа]"
        self.status = DocumentStatus.EXTRACTED

    def structure(self):
        self.status = DocumentStatus.STRUCTURED

    def index(self):
        self.status = DocumentStatus.INDEXED

    def get_entities(self) -> List['ExtractedEntity']:
        return self.entities


class DepersonalizationRule:
    def __init__(self, id: int, name: str, pattern: str,
                 replacement: str, type_: str, active: bool = True):
        self.id = id
        self.name = name
        self.pattern = pattern
        self.replacement = replacement
        self.type = type_
        self.active = active

    def apply(self, text: str) -> str:
        # в реальной системе — замена по регулярному выражению self.pattern
        return text


class ExtractedEntity:
    def __init__(self, id: int, type_: str, value: str,
                 confidence: float, start_pos: int, end_pos: int):
        self.id = id
        self.type = type_
        self.value = value
        self.confidence = confidence
        self.start_pos = start_pos
        self.end_pos = end_pos

    def get_type(self) -> str:
        return self.type

    def get_value(self) -> str:
        return self.value


class ProcessingTask:
    def __init__(self, id: int, type_: str):
        self.id = id
        self.type = type_
        self.status = "PENDING"
        self.started_at: Optional[date] = None
        self.finished_at: Optional[date] = None
        self.error_message = ""

    def execute(self):
        self.started_at = date.today()
        self.status = "RUNNING"

    def cancel(self):
        self.status = "CANCELLED"


class SearchQuery:
    def __init__(self, id: int, query_text: str, filters: str):
        self.id = id
        self.query_text = query_text
        self.filters = filters
        self.created_at = date.today()

    def execute(self) -> List['SearchResult']:
        return []


class SearchResult:
    def __init__(self, document: Document, score: float, snippet: str):
        self.document = document
        self.score = score
        self.snippet = snippet

    def get_document(self) -> Document:
        return self.document

    def get_score(self) -> float:
        return self.score


# ---------------------------------------------------------------------------
# Демонстрационный сценарий: загрузка -> обезличивание -> извлечение
# сущностей -> индексация -> поиск
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    analyst = User(
        id=1,
        login="analyst",
        password_hash="hash",
        full_name="Иван Петров",
        email="ivan@example.com",
        role=Role.ANALYST,
    )
    print(f"Пользователь: {analyst.full_name}, роль: {analyst.role.value}")

    doc = Document(
        id=1,
        title="Договор поставки №42",
        original_file_name="contract_42.pdf",
        file_path="/uploads/contract_42.pdf",
        mime_type="application/pdf",
        size=102400,
    )
    doc.upload()
    print(f"Документ '{doc.title}' загружен, статус: {doc.status.value}")

    # Правило обезличивания
    rule = DepersonalizationRule(
        id=1,
        name="Маскировка ФИО",
        pattern=r"\b[А-ЯЁ][а-яё]+\s[А-ЯЁ]\.\s?[А-ЯЁ]\.",
        replacement="[ФИО]",
        type_="PERSON",
    )
    doc.applied_rules.append(rule)
    doc.depersonalize()
    print(f"Обезличен: {doc.depersonalized}, статус: {doc.status.value}")

    # Извлечение сущностей
    entity = ExtractedEntity(
        id=1,
        type_="DATE",
        value="12.05.2025",
        confidence=0.98,
        start_pos=120,
        end_pos=130,
    )
    doc.entities.append(entity)
    doc.extract_text()
    print(f"Извлечено сущностей: {len(doc.get_entities())}, "
          f"статус: {doc.status.value}")

    # Структурирование и индексация
    doc.structure()
    doc.index()
    print(f"Индекс построен, итоговый статус: {doc.status.value}")

    # Поиск
    query = SearchQuery(
        id=1,
        query_text="договор поставки",
        filters="type=pdf;date>=2025-01-01",
    )
    result = SearchResult(
        document=doc,
        score=0.93,
        snippet="...договор поставки №42...",
    )
    print(
        f"Запрос: '{query.query_text}' → найдено: 1, "
        f"score={result.get_score()}, "
        f"документ='{result.get_document().title}'"
    )

    # Задача обработки (демонстрация жизненного цикла ProcessingTask)
    task = ProcessingTask(id=1, type_="FULL_PIPELINE")
    task.execute()
    print(f"Задача обработки #{task.id}: статус={task.status}, "
          f"стартовала={task.started_at}")
from fastapi import FastAPI

_DESCRIPTION = """
Пример решений задания для Backend-разработчика Школы IT 🚀.

## Пользователи

Для работы с пользователями можно:
* **создать запись** ;
* **получить список** с возможностью фильтрации по полу и заданием лимита.
"""

app = FastAPI(title="task-backend--example",
              description=_DESCRIPTION,
              version="1.0.0",
              redoc_url=None)

if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app)

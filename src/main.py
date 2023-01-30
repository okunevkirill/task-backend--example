from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from src.users.routes import router
from src.database import init_models

_DESCRIPTION = """
Пример решений задания для Backend-разработчика Школы IT 🚀.

## Пользователи

Для работы с пользователями можно:
* **создать пользователя** ;
* **получить список** с возможностью фильтрации по полу и заданием лимита.
"""

init_models()
app = FastAPI(title="task-backend--example",
              description=_DESCRIPTION,
              version="1.0.0",
              redoc_url=None)


@app.get("/", response_class=HTMLResponse, tags=["Main"])
async def root():
    """Представление страницы приветствия."""
    html_content = """
    <html>
        <head>
            <title>task-backend--example</title>
        </head>
        <body>
            <h1>Пример решения задания для Backend-разработчика Школы IT</h1>
            <div>
                ✍ <a href="/docs">Документация приведена по данному адресу</a> 
            </div>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content)


# Регистрация маршрутов от функциональных модулей
app.include_router(router)

if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app)

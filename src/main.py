from fastapi import FastAPI
from fastapi.responses import HTMLResponse

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


@app.get("/", response_class=HTMLResponse, tags=["Main"])
async def root():
    """Обработчик  **ГЛАВНОГО** пути"""
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


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app)

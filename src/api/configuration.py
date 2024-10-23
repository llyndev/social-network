from tortoise.contrib.fastapi import register_tortoise
from fastapi import FastAPI
from src.api.routes import users, home, post

def configure_routes(app: FastAPI):
    app.include_router(users.router)
    app.include_router(home.router)
    app.include_router(post.router)

def configure_db(app: FastAPI):
    register_tortoise (
        app=app,
        config={
            'connections': {
                'default': 'sqlite://db.sqlite3'
            },
            'apps': {
                'models': {
                    'models': [
                        'src.datalayer.models.user',
                        'src.datalayer.models.post',
                    ],
                    'default_connection': 'default',
                }
            }
        },
        generate_schemas=True,
        add_exception_handlers=True,
    )
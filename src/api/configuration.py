from tortoise.contrib.fastapi import register_tortoise
from fastapi import FastAPI
from src.api.routes import users, home, post
from fastapi.middleware.cors import CORSMiddleware

ALLOWED_HOSTS = [
    "http://127.0.0.1:3000",
]

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
    
def configure_middlewares(app):
    
    app.add_middleware(
        CORSMiddleware,
        allow_origins=ALLOWED_HOSTS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
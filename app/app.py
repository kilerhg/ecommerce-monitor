from fastapi import FastAPI
from app.routes.ecommerce import router as router_ecommerce

app = FastAPI()


app.include_router(router_ecommerce)


if __name__ == '__main__':
    app.run()
from fastapi import FastAPI
from gradio import mount_gradio_app

from app import demo

app = FastAPI()

app = mount_gradio_app(app, demo, path="/")
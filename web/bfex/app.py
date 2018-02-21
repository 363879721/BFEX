import os
from flask import Flask
from bfex.blueprints.data_ingestion import data_ingestion_bp as data_ingestion
from bfex.models import initialize_models


def create_app():
    from elasticsearch_dsl.connections import connections
    
    app = Flask("bfex")
    
    elastic_host = os.environ["ELASTIC_HOST"]
    connections.create_connection(hosts=[elastic_host])

    initialize_models()

    app.register_blueprint(data_ingestion)

    return app

app = create_app()
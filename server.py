import logging
import asyncio
from aiocoap import resource, Context
from dotenv import dotenv_values

from core.Codec import Codec
from core.IoTApi import IoTApi, append_iot_api
from core.WebApi import WebApi, append_web_api
from core.DatabaseInterface import DatabaseSettings, create_database_handler

# Attach a logger interface.
logging.basicConfig(level=logging.INFO)
logging.getLogger("coap-server").setLevel(logging.DEBUG)

# Constants for server configuration.
COAP_HOST: str = '127.0.0.1'
COAP_PORT: int = 5683

# Database connection settings.
ENV_CONFIGS: dict = dotenv_values(".env")
database_settings = DatabaseSettings(
    name=ENV_CONFIGS['DATABASE_NAME'],
    host=ENV_CONFIGS['DATABASE_HOST'],
    port=ENV_CONFIGS['DATABASE_PORT'],
    username=ENV_CONFIGS['DATABASE_USERNAME'],
    password=ENV_CONFIGS['DATABASE_PASSWORD']
)
database_handler = create_database_handler(database_settings)

# The main function for asynchronous execution.
async def main():
    root = resource.Site()
    root = append_web_api(root)
    root = append_iot_api(root)

    await Context.create_server_context(bind=(COAP_HOST, COAP_PORT), site=root)
    await asyncio.get_running_loop().create_future()


if __name__ == "__main__":
    asyncio.run(main())

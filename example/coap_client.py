import logging
import asyncio
from aiocoap import Context, Message, PUT

from core.Codec import Codec

# Constants
COAP_URI: str = "coap://127.0.0.1/other/block"
COAP_METHOD = PUT
COAP_PAYLOAD: bytearray = Codec.encode({"message": "Example!", "version": 10})

# Enable logging interface.
logging.basicConfig(level=logging.INFO)

async def main():
    # Create a CoAP client for test purposes.
    protocol = await Context.create_client_context()
    # Create a request to send later.
    request = Message(code=COAP_METHOD, uri=COAP_URI, payload=COAP_PAYLOAD)

    try:
        # Send the request through CoAP network.
        response = await protocol.request(request).response
    except Exception as e:
        print('Failed to fetch resource:')
        print(e)
    else:
        print('Result: %s\n%r'%(response.code, response.payload))

if __name__ == "__main__":
    asyncio.run(main())
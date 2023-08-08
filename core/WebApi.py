import aiocoap.resource as resource
from core.Codec import Codec

class WebApi(resource.Resource):
    """
    This class handles the logic and the CoAP functionality for the 
    connection between web devices and the CoAP server.

    Request types:
    - GET /web/(...)
    - POST /web/(...)
    """

    def __init__(self):
        super().__init__()

    async def render_post(self, request):
        """
        Handles the POST requests from the web server.
        """
        # Get the path from the request.
        path = request.opt.uri_path
        # Get the payload from the request.
        payload = request.payload
        # Decode the payload to the object.
        payload = Codec.decode(payload)

        # Check the path and handle the request accordingly.
        if path == ['web', '(...)']:
            # Handle the prediction request.
            await self.handle_some_request(payload)
        else:
            # Handle the unknown request.
            await self.handle_unknown_request(payload)
    
    async def render_get(self, request):
        """
        Handles the GET requests from the web server.
        """
        # Get the path from the request.
        path = request.opt.uri_path

        # Check the path and handle the request accordingly.
        if path == ['iot', '(...)']:
            # Handle the last prediction request.
            await self.handle_some_request()
        else:
            # Handle the unknown request.
            await self.handle_unknown_request()

    async def handle_some_request(self, payload):
        """
        Handles some request - mocked function.
        """
 
    async def handle_unknown_request(self):
        """
        Handles the unknown request.
        """
    

def append_web_api(site_resource: resource.Site) -> resource.Site:
    """
    Creates a new instance of the WebApi class.
    """
    site_resource.add_resource(['web', '(...)'], WebApi())
    return site_resource
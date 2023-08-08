import aiocoap.resource as resource
from core.Codec import Codec

class IoTApi(resource.Resource):
    """
    This class handles the logic and the CoAP functionality for the 
    connection between IoT devices and the CoAP server.

    Request types:
    - GET /iot/last_prediction
    - POST /iot/prediction
    - POST /iot/register_device
    - POST /iot/heartbeat
    """

    def __init__(self):
        super().__init__()

    async def render_post(self, request):
        """
        Handles the POST requests from the IoT devices.
        """
        # Get the path from the request.
        path = request.opt.uri_path
        # Get the payload from the request.
        payload = request.payload
        # Decode the payload to the object.
        payload = Codec.decode(payload)

        # Check the path and handle the request accordingly.
        if path == ['iot', 'prediction']:
            # Handle the prediction request.
            await self.handle_prediction_request(payload)
        elif path == ['iot', 'register_device']:
            # Handle the register device request.
            await self.handle_register_device_request(payload)
        elif path == ['iot', 'heartbeat']:
            # Handle the heartbeat request.
            await self.handle_heartbeat_request(payload)
        else:
            # Handle the unknown request.
            await self.handle_unknown_request(payload)
    
    async def render_get(self, request):
        """
        Handles the GET requests from the IoT devices.
        """
        # Get the path from the request.
        path = request.opt.uri_path

        # Check the path and handle the request accordingly.
        if path == ['iot', 'last_prediction']:
            # Handle the last prediction request.
            await self.handle_last_prediction_request()
        else:
            # Handle the unknown request.
            await self.handle_unknown_request()

    async def handle_prediction_request(self, payload):
        """
        Handles the prediction request.
        """
    
    async def handle_register_device_request(self, payload):
        """
        Handles the register device request.
        """
    
    async def handle_heartbeat_request(self, payload):
        """
        Handles the heartbeat request.
        """
    
    async def handle_last_prediction_request(self):
        """
        Handles the last prediction request.
        """

    async def handle_unknown_request(self):
        """
        Handles the unknown request.
        """
    

def append_iot_api(site_resource: resource.Site) -> resource.Site:
    """
    Creates a new instance of the IoTApi class.
    """
    site_resource.add_resource(['iot', 'last_prediction'], IoTApi())
    site_resource.add_resource(['iot', 'prediction'], IoTApi())
    site_resource.add_resource(['iot', 'register_device'], IoTApi())
    site_resource.add_resource(['iot', 'heartbeat'], IoTApi())
    return site_resource
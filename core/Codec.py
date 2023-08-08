class Codec:
    @staticmethod
    def encode(cls, object_to_encode: dict) -> bytearray:
        """Encode a dict to Pickle object to send later."""
        pass

    @staticmethod
    def decode(cls, object_to_decode: bytearray) -> dict:
        """Decode a dict to Pickle object to send later."""
        pass
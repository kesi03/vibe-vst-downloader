import urllib.request


class HttpClient:

    def get_bytes(
        self,
        url: str,
        timeout: int = 60,
    ) -> bytes:
        
        request = urllib.request.Request(
            url,
            headers={
                "User-Agent":
                "VIBE-FM-Firmware-Manager"
            },
        )

        with urllib.request.urlopen(
            request,
            timeout=timeout,
        ) as response:

            return response.read()


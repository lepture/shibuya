from tornado.web import RequestHandler
from tornado.httpclient import AsyncHTTPClient
from livereload import Server, shell

shell("make build-docs")()


class ProxyHandler(RequestHandler):
    proxy_url = "https://shibuya.readthedocs.io/_/"

    async def get(self, path: str) -> None:
        query = self.request.query
        url = self.proxy_url + path
        if query:
            url += '?' + query
        client = AsyncHTTPClient()
        response = await client.fetch(url)
        self.set_status(response.code)
        if response.body:
            for header in response.headers:
                if header.lower() == "content-length":
                    self.set_header(header, str(max(len(response.body), int(response.headers.get(header)))))
                elif header.lower() != "transfer-encoding":
                    self.set_header(header, response.headers.get(header))
            self.write(response.body)
        self.finish()


class DebugServer(Server):
    def get_web_handlers(self, script):
        proxy = (r"/_/(.*)", ProxyHandler)
        handlers = super().get_web_handlers(script)
        return [proxy, *handlers]


app = DebugServer()
app.watch("src", shell("make build-docs"), delay=2)
app.watch("docs", shell("make build-docs"), delay=2)
app.serve(root="build/_html")

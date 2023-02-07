from livereload import Server, shell

app = Server()
app.watch("sphinx_shibuya/src", shell("make build-docs"))
app.watch("docs", shell("make build-docs"))
app.serve(root="build/_html")

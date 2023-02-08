from livereload import Server, shell

app = Server()
app.watch("src", shell("make build-docs"))
app.watch("docs", shell("make build-docs"))
app.serve(root="build/_html")

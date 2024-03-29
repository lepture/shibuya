from livereload import Server, shell

shell("make build-docs")()

app = Server()
app.watch("src", shell("make build-docs"), delay=2)
app.watch("docs", shell("make build-docs"), delay=2)
app.serve(root="build/_html")

from flask import *

full_links = {
    'sowmya': 'https://coda.io/d/Airlift-Sowmya-Darwin_dQn7W1Has1v/Todos_sutqD#_lu9QK'
}

app = Flask(__name__)

@app.route("/<shorthand>")
def redirect_shorthand(shorthand):
    if shorthand not in full_links:
        abort(404)
    return redirect(full_links[shorthand])

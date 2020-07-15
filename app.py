
import os
from notion.client import NotionClient
from flask import Flask
from flask import request


app = Flask(__name__)


def createNotionTask(token, collectionURL, content, status, description, source, category, trellourl):
    # notion
    client = NotionClient(token)
    cv = client.get_collection_view(collectionURL)
    row = cv.collection.add_row()
    row.title = content
    row.status = status
    row.description = description
    row.source = source
    row.category = category
    row.url = trellourl


@app.route('/create_todo', methods=['GET'])
def create_todo():

    todo = request.args.get('todo')
    status = request.args.get('status')
    description = request.args.get('description')
    source = request.args.get('source')
    category = request.args.get('category')
    trellourl = request.args.get('trellourl')
    token_v2 = os.environ.get("TOKEN")
    url = os.environ.get("URL")
    createNotionTask(token_v2, url, todo, status, description, source, category, trellourl)
    return f'added {todo} to Notion'

def createNotionNote(token, collectionURL, content, category, noteformat,filepath):
    # notion
    client = NotionClient(token)
    cv = client.get_collection_view(collectionURL)
    row = cv.collection.add_row()
    row.title = content
    row.category = category
    row.format = noteformat
    row.files = filepath
    
@app.route('/create_note', methods=['GET'])
def create_note():
    note = request.args.get('note')
    category = request.args.get('category')
    noteformat = request.args.get('noteformat')
    filepath = ["https://www.birdlife.org/sites/default/files/styles/1600/public/slide.jpg"]
    token_v2 = os.environ.get("TOKEN")
    url = os.environ.get("NOTE_URL")
    createNotionNote(token_v2, url, note, category, noteformat, filepath)
    return f'added {note} to Notion'


if __name__ == '__main__':
    app.debug = True
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

from flask import Flask, render_template, request, jsonify
import requests
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import dotenv_values

config = dotenv_values(".env")

app = Flask(__name__)

uri = 'mongodb+srv://' + config['DB_USER'] + ':' + config['DB_PASSWORD'] + config['DB_URI']
client = MongoClient(uri, server_api=ServerApi('1'))
db = client['GitHub_Retriever']


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/get-repos', methods=['GET'])
def get_repos():
    username = request.args['username']
    url = f'https://api.github.com/users/{username}/repos'
    headers = {'Authorization': 'token ' + config['ACCESS_TOKEN']}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        repos = response.json()[:5]
        for repo in repos:
            user_repo = {
                'username': repo['owner']['login'],
                'repo_name': repo['name'],
                'description': repo['description'],
                'language': repo['language'],
                'html_url': repo['html_url']
            }
            repo_exists = db.users_repos.find_one({
                'username': user_repo['username'],
                'repo_name': user_repo['repo_name']
            })

            if repo_exists:
                db.users_repos.update_one({
                    'username': user_repo['username'],
                    'repo_name': user_repo['repo_name']
                },
                    {'$set': user_repo}
                )
            else:
                db.users_repos.insert_one(user_repo)
        return render_template('repos.html', repos=repos)
    else:
        return 'User not found or an error occurred.'


if __name__ == '__main__':
    app.run(debug=True)

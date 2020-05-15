import uuid
from datetime import datetime
from ..services import util, sqlite, ecr

def ecr_get_all():
    return ecr.describe_repositories()

def ecr_get_repos_by_user(user_repos):
    repos = ecr_get_all()
    ret = []
    for repo in repos:
        if repo['repositoryName'] in user_repos:
            ret.append(repo)
    return ret

def ecr_get_details(repository):
    return ecr.describe_repository(repository)

def ecr_get_images(repository):
    return ecr.describe_images(repository)


"""
def add(users_id, message_text):
    query = "INSERT INTO messages (created_at, users_id, message) VALUES (?,?,?)"
    params = (datetime.utcnow().isoformat(), users_id, message_text)
    if sqlite.write(query, params):
        return True
    return False

def all():
    query = "SELECT m.id, m.created_at, m.message, u.name FROM messages AS m INNER JOIN users AS u ON m.users_id = u.id ORDER BY m.created_at DESC"
    return sqlite.read(query)
"""
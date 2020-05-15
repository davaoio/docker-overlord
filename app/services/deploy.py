import uuid
from datetime import datetime
from ..services import util, sqlite, ec2, ecr

def get_status(name):
    query = "SELECT * FROM deployed_repository WHERE repository = ?"
    params = (name,)
    ret = {}
    ret['deployed'] = sqlite.read(query, params, one=True)
    ret['details'] = ecr.describe_repository(name)
    return ret

def set_release(release):
    query = "INSERT INTO deployed_repository (repository, image_tag, released) VALUES (?,?,datetime('now')) ON CONFLICT (repository) DO UPDATE SET image_tag = ?, released = datetime('now')"
    params = (release.repository, release.image, release.image)
    if not sqlite.write(query, params):
        return False
    return True

def instance(id):
    tags = ec2.describe_tags(id)
    repository = ec2._get_tag_value(tags, 'Repository')
    return get_status(repository)

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
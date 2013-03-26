import urllib2
import json

#Settings go here
base_url = 'https://api.github.com/repos'
user = 'rails'
repository = 'rails'
filename_tags = 'tags.json'
filename_commits = 'commits.json'

def fetch_tags():
    tags = {}
    request = urllib2.urlopen('{0}/{1}/{2}/tags'.format(base_url, user, repository))
    json_data = json.loads(request.read())
    for tag in json_data:
        tags[tag['name']] = replace_url(tag['tarball_url'])
    return tags

def fetch_commits():
    commits = {}
    request = urllib2.urlopen('{0}/{1}/{2}/commits'.format(base_url, user, repository))
    json_data = json.loads(request.read())
    for commit in json_data:
        commits[commit['sha']] = replace_url_commits(commit['url'])
    return commits
    

def save_json_to_file(filename, doc):
    fp = open(filename, 'w')
    fp.write(json.dumps(doc))
    fp.close()

def replace_url(url):
    """
    This is a bit hacky. I couldn't work out how to get the actual github
    url from the api in time so I modified the tarball url to the github
    url.
    """
    url = url.replace('https://api.', 'https://')
    url = url.replace('/repos', '')
    url = url.replace('/tarball', '/tree')
    return url

def replace_url_commits(url):
    url = url.replace('https://api.', 'https://')
    url = url.replace('/repos', '')
    return url

if __name__ == "__main__":
    tags = fetch_tags()
    save_json_to_file(filename_tags, tags)
    commits = fetch_commits()
    save_json_to_file(filename_commits, commits)

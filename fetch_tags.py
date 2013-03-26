import urllib2
import json

#Settings go here
base_url = 'https://api.github.com/repos'
user = 'rails'
repository = 'rails'
filename = 'tags.json'

def fetch_tags():
    tags = {}
    request = urllib2.urlopen('{0}/{1}/{2}/tags'.format(base_url, user, repository))
    json_data = json.loads(request.read())
    for tag in json_data:
        tags[tag['name']] = replace_url(tag['tarball_url'])
    return tags

def save_tags_to_file(filename, tags):
    fp = open(filename, 'w')
    fp.write(json.dumps(tags))

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

if __name__ == "__main__":
    tags = fetch_tags()
    save_tags_to_file(filename, tags)

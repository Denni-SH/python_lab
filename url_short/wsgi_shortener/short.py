import json
import hashlib
def get_url_list():
    read_file = open('urls.json', 'r+')
    url_dict = json.load(read_file)
    read_file.close()
    return url_dict

def add_url(url_raw, url_hash):
    urls = get_url_list()
    if url_raw in urls:
        print('already')
    else:
        urls[url_raw] = url_hash
        write_file = open('urls.json', 'w')
        json.dump(urls, write_file)
        write_file.close()

def hashing(url_raw):
    return hashlib.md5(url_raw.encode('utf-8')).hexdigest()

def get_url(url_hash):
    return get_url_list().get(url_hash)

def main(url_raw):
    # url_raw = 'vikaz.com'
    url_hash = hashing(url_raw)
    add_url(url_hash,url_raw)

main()
# print(get_url(hash_hard))
# hash_hard = 'd2b6043e84b2aebc95a2faf382bde230'


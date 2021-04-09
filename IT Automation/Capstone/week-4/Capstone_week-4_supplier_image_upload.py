#!/usr/bin/env python3
import sys, os, requests

URL = "http://localhost/upload/"

def upload(img_path):
    with open(img_path, 'rb') as opened:
        r = requests.post(URL, files={'file': opened})
        print(r.status_code, r.reason)
    opened.close()

if __name__ == '__main__':
    arg = sys.argv[1:]
    path = arg[0]

    img_dir = [os.path.join(path, x) for x in os.listdir(path) if '.jpeg' in x]
    for img in img_dir:
        upload(img)
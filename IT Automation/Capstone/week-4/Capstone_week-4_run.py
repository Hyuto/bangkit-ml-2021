#!/usr/bin/env python3
import sys, os, requests

EXTERNAL_IP = '34.71.224.205'

def post(external_ip, content):
    url = 'http://{}/fruits/'.format(external_ip)
    send = requests.post(url, data = content)
    print(send.status_code, send.reason)

if __name__ == "__main__":
    arg = sys.argv[1:]
    text_path = arg[0]
    text_dirs = [(os.path.join(text_path, x), x) for x in os.listdir(text_path) if '.txt' in x]

    for path, name in text_dirs:
        with open(path) as f:
            line_data = {}
            text = f.read().split('\n')
            line_data["name"] = text[0]
            line_data["weight"] = int(text[1].split()[0])
            line_data["description"] = ' '.join(text[2:])
            line_data["image_name"] = "{}.jpeg".format(name[:-4])
            
            post(EXTERNAL_IP, line_data)
        f.close()
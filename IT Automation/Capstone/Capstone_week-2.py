#! /usr/bin/env python3
import os, sys, requests

EXTERNAL_IP = '34.72.38.165'

def extract_data_from_txt(files, path):
    data = []
    for text in files:
        with open(os.path.join(path, text)) as f:
            line = f.read().split('\n')
            line_data = {}
            line_data['title'] = line[0]
            line_data['name'] = line[1]
            line_data['date'] = line[2]
            line_data['feedback'] = ' '.join(line[3:])
            data.append(line_data)
        f.close()
    return data

def post(external_ip, content):
    url = 'http://{}/feedback/'.format(external_ip)
    send = requests.post(url, data = content)
    return send

if __name__ == "__main__":
    path = sys.argv[1]
    text_files = [x for x in os.listdir(path) if '.txt' in x]

    data = extract_data_from_txt(text_files, path)
    for line in data:
        post_data = post(EXTERNAL_IP, line)
        print('{} : {}'.format(post_data.status_code, post_data.reason))
    print("Done !")
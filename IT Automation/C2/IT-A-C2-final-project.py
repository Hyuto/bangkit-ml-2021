#!/usr/bin/env python3
import csv, re, operator

def error_matcher(word):
    res = re.search(r'ERROR.*', word)
    if res:
        res = res.group(0).split()[1:-1]
        return ' '.join(res)
    return None

def user_checker(word):
    res = re.search(r'[ERROR|INFO].*', word).group(0)
    res = res.split()
    user_name = res[-1][1:-1]
    cond = res[0]
    if cond == 'INFO':
        return user_name, [1, 0]
    else:
        return user_name, [0, 1]

f = open('syslog.log', 'r')
ERROR, USER = {}, {}
for line in f.readlines():
    line = line.strip()

    # Check Error
    is_error = error_matcher(line)
    if is_error:
        if is_error in ERROR:
            ERROR[is_error] += 1
        else:
            ERROR[is_error] = 1

    # Check User
    user_name, cond = user_checker(line)
    if user_name in USER:
        USER[user_name][0] += cond[0]
        USER[user_name][1] += cond[1]
    else:
        USER[user_name] = cond
f.close()

with open('error_message.csv', mode='w') as err_file:
    fieldnames = ['Error', 'Count']
    writer = csv.DictWriter(err_file, fieldnames=fieldnames)
    writer.writeheader()

    for line in sorted(ERROR.items(), key=operator.itemgetter(1), reverse=True):
        writer.writerow({'Error': line[0], 'Count': line[1]})
err_file.close()

with open('user_statistics.csv', mode='w') as usr_file:
    fieldnames = ['Username', 'INFO', 'Error']
    writer = csv.DictWriter(usr_file, fieldnames=fieldnames)
    writer.writeheader()

    for line in sorted(USER.items(), key=operator.itemgetter(0)):
        writer.writerow({'Username':line[0], 'INFO':line[1][0], 'Error':line[1][1]})
usr_file.close()
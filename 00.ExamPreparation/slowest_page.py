from urllib.parse import urlparse
from operator import itemgetter
import re


needed_items_dict = {}
with open(input(), encoding="utf-8") as f:
    for line in f:
        response_time_regex = re.search("resp_t=\"(.*?)\"", line)
        url_reponse_regex = re.search("url=\"(.*?)\"", line)
        url = url_reponse_regex.group(1)
        strip_url = urlparse(url)

        response_time = response_time_regex.group(1)
        url = strip_url.path
        if url not in needed_items_dict.keys():
            needed_items_dict[url] = []
            needed_items_dict[url].append(float(response_time))
        else:
            needed_items_dict[url].append(float(response_time))

needed_items_dict.pop("/student/activity/ws/")

for k,v in needed_items_dict.items():
    v_avg = sum(v)/len(v)
    needed_items_dict[k] = v_avg

maxPair = max(needed_items_dict.items(), key=itemgetter(1))

print(maxPair[0])
print("{:.3f}".format(float(maxPair[1])))

import json

from konlpy.tag import Twitter
from collections import Counter


def get_tags(text, ntags=50):
    spliter = Twitter()
    nouns = spliter.nouns(text)
    count = Counter(nouns)
    return_list = []
    for n, c in count.most_common(ntags):
        temp = {'tag': n, 'count': c}
        return_list.append(temp)
    return return_list


def main():
    noun_count = 1000
    output_file_name = "현대_자동차.csv"
    text = ""
    for i in range(10):
        with open('현대_자동차/output' + str(i) + '.json', 'r', encoding='utf-8') as f:
            array = json.load(f)
            for j in range(len(array['item'])):
                text += array['item'][0]['title']
                text += array['item'][0]['content']
    for i in range(10):
        with open('경기도/output' + str(i) + '.json', 'r', encoding='utf-8') as f:
            array = json.load(f)
            for j in range(len(array['item'])):
                text += array['item'][0]['title']
                text += array['item'][0]['content']
    for i in range(10):
        with open('경기도_골칫거리/output' + str(i) + '.json', 'r', encoding='utf-8') as f:
            array = json.load(f)
            for j in range(len(array['item'])):
                text += array['item'][0]['title']
                text += array['item'][0]['content']
    tags = get_tags(text, noun_count)
    open_output_file = open(output_file_name, 'w', -1)
    for tag in tags:
        noun = tag['tag']
        count = tag['count']
        open_output_file.write('{}, {}\n'.format(noun, count))
    open_output_file.close()


if __name__ == '__main__':
    main()

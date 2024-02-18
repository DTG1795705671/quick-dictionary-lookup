from readmdict import MDX, MDD  # pip install readmdict
from config import dictionary_url
from config import temp_worditem_save_url

'''
# 如果是windows环境，运行提示安装python-lzo，但
> pip install python-lzo
报错“please set LZO_DIR to where the lzo source lives” ，则直接从 https://www.lfd.uci.edu/~gohlke/pythonlibs/#_python-lzo 下载 "python_lzo‑1.12‑你的python版本.whl" 
> pip install xxx.whl 
装上就行了，免去编译的麻烦
'''
class dictionary:
    # 加载mdx文件
    def __init__(self):
        self.headwords = [*MDX(dictionary_url)]  # 单词名列表
        self.items = [*MDX(dictionary_url).items()]  # 释义html源码列表
        if len(self.items) == len(self.headwords):
            print(f'词典加载成功：共{len(self.headwords)}条')
        else:
            print(f'词典加载失败')

    # 查词，返回单词和html文件
    def look_up(self,word):
        try:
            wordIndex = self.headwords.index(word.encode())
            word,html = self.items[wordIndex]
            word,html = word.decode(), html.decode()
        except:
            print("查找失败")
            html = f"\"{word}\" wasn't found!"

        with open(temp_worditem_save_url, 'w', encoding='utf-8') as f:
            f.write(html)

# # # 从html中提取需要的部分，这里以the litte dict字典为例。到这一步需要根据自己查询的字典html格式，自行调整了。
# doc = pq(html)
# coca2 = doc('div[class="coca2"]').text().replace('\n','')
# meaning = doc('def,rx').text().replace('\n','').replace('🔊','')
# means = doc('sn-g').items()
#
# explains = []
# count = 0
# for item in means:
#     mean = item('def,x-gs').text().replace('\n', '').replace('🔊','')
#     explains.append(mean)
#     count = count + 1
# if count != 0:
#     dict_items.append((word,explains))
# print(coca2)
# print(meaning)


if __name__=='__main__':
    dict_ = dictionary()
    dict_.look_up('pay')
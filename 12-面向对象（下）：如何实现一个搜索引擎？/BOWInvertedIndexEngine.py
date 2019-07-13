import re
from SearchEngineBase import main
from SearchEngineBase import SearchEngineBase


class BOWInvertedIndexEngine(SearchEngineBase):
    def __init__(self):
        super(BOWInvertedIndexEngine, self).__init__()
        self.inverted_index = {}

    def process_corpus(self, id, text):
        words = self.parse_text_to_words(text)
        for word in words:
            if word not in self.inverted_index:
                self.inverted_index[word] = []
            self.inverted_index[word].append(id)

    def search(self, query):
        query_words = list(self.parse_text_to_words(query))
        query_words_index = []
        for query_word in query_words:
            query_words_index.append(0)

        """
        首先我要强调一下，这次的算法并不需要你完全理解，这里的实现有一些超出了本章知识点。但希望你不要因此退缩，这个例子会告诉你，
        面向对象编程是如何把算法复杂性隔离开来，而保留接口和其他的代码不变。
        """
        # 如果某一个查询单词的倒序索引为空，我们就立刻返回
        for query_word in query_words:
            if query_word not in self.inverted_index:
                return []

        result = []
        while True:
            # 首先，获得当前状态下所有倒序索引的 index
            current_ids = []
            for idx, query_word in enumerate(query_words):
                current_index = query_words_index[idx]
                current_inverted_list = self.inverted_index[query_word]
                # 已经遍历到了某一个倒序索引的末尾，结束 search
                if current_index >= len(current_inverted_list):
                    return result
                current_ids.append(current_inverted_list[current_index])
            # 然后，如果 current_ids 的所有元素都一样，那么表明这个单词在这个元素对应的文档中都出现了
            if all(x == current_ids[0] for x in current_ids):
                result.append(current_ids[0])
                query_words_index = [x + 1 for x in query_words_index]
                continue
            # 如果不是，我们就把最小的元素加一
            min_val = min(current_ids)
            min_val_pos = current_ids.index(min_val)
            query_words_index[min_val_pos] += 1

    @staticmethod
    def parse_text_to_words(text):
        # 使用正则表达式去除标点符号和换行符，用空格代替
        text = re.sub(r'[^\w]', ' ', text)
        # 转为小写
        text = text.lower()
        # 生成所有单词的列表
        word_list = text.split(' ')
        # 去除空白单词
        word_list = filter(None, word_list)
        # 返回单词的 set
        return set(word_list)


if __name__ == '__main__':
    search_engine = BOWInvertedIndexEngine()
    main(search_engine)

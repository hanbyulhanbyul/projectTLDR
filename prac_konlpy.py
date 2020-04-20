from collections import Counter
from konlpy.corpus import kolaw
from konlpy.tag import Okt
from konlpy.utils import concordance, pprint

def draw_zipf(count_list, filename, color='blue', marker='o'):
    sorted_list = sorted(count_list, reverse=True)

doc = kolaw.open('constitution.txt').read()
print(doc)

# pos = Okt().pos(doc)
# cnt = Counter(pos)
#
# print('nchars  :', len(doc))
# print('ntokens :', len(doc.split()))
# print('nmorphs :', len(set(pos)))
# print('\nTop 20 frequent morphemes:'); print(cnt.most_common(20))
# print('\nLocations of "대한민국" in the document:')
# concordance(u'대한민국', doc, show=True)
#

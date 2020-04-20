from konlpy.tag import Okt
lang = Okt()
print(lang.morphs(u'삼전사는 동학개미운동ㅋㅋㅋㅋ안됔ㅋㅋㅋㅋㅋ'))
print(lang.nouns(u'삼전사는 동학개미운동ㅋㅋㅋㅋ안됔ㅋㅋㅋㅋㅋ'))
print(lang.pos(u'삼전사는 동학개미운동ㅋㅋㅋㅋ안됔ㅋㅋㅋㅋㅋ'))
print(lang.pos(u'삼전사는 동학개미운동ㅋㅋㅋㅋ안됔ㅋㅋㅋㅋㅋ', norm=True))
print(lang.pos(u'삼전사는 동학개미운동ㅋㅋㅋㅋ안됔ㅋㅋㅋㅋㅋ', norm=True, stem=True))
print(lang.phrases(u'삼전사는 동학개미운동ㅋㅋㅋㅋ안됔ㅋㅋㅋㅋㅋ'))


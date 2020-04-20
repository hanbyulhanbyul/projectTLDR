from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import pandas as pd
import nltk

from collections import Counter
from konlpy.tag import Okt
from konlpy.utils import concordance, pprint
app = Flask(__name__)


@app.route('/')
def home():
   return render_template('TLDR.html')

@app.route('/fileUpload', methods=['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))
      print ("파일 이름: " + f.filename)


      file_read = pd.read_csv(f.filename)
      top_N = 10
      word_dist = nltk.FreqDist(file_read['User'])
      rslt = pd.DataFrame(word_dist.most_common(top_N), columns=['Word', 'Frequency'])
      print('=' * 60)
      print(rslt)
      print('=' * 60)
      # return 'uploads 디렉토리 -> 파일 업로드 성공!'

      # doc = file_read()
      # print(doc)
      # pos = Okt().pos(doc)
      # cnt = Counter(pos)
      #
      # print('\nTop 10 키워드:');
      # print(cnt.most_common(10))
      # print('\nLocations of "코딩" in the document:')
      # concordance(u'코딩', doc, show=True)

      return 'uploads 디렉토리 -> 파일 업로드 성공!'


      # def draw_zipf(count_list, filename, color='blue', marker='o'):
      # sorted_list = sorted(count_list, reverse=True)
      # doc = kolaw.open('constitution.txt').read()

# @app.route('/addcard', methods=['GET'])
# def add_card():
#     # 1. mystar 목록 전체를 검색합니다. ID는 제외하고 like 가 많은 순으로 정렬합니다.
#     # 참고) find({},{'_id':False}), sort()를 활용하면 굿!
#     stars = list(db.mystar.find({},{'_id':False}).sort('like',-1))
#     # 2. 성공하면 success 메시지와 함께 stars_list 목록을 클라이언트에 전달합니다.
#     return jsonify({'result': 'success','stars_list':stars})

if __name__ == '__main__':  
   app.run(debug=True)

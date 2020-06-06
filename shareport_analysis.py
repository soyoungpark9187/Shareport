import json
import pickle
from operator import eq

from flask import Blueprint, Flask
from sklearn.externals import joblib

classifier_f = open('comment_classification_model.pkl', 'rb')
cl = pickle.load(classifier_f)
classifier_f.close()


comment_list=[]
with open('shareport-e85b2-export.json', 'rt', encoding='UTF8')as json_file:
    json_data = json.load(json_file)

    key_list = list(json_data['comments'].values())

    for i in range(len(key_list)):
        comment_list.append(key_list[i]['comment'])


print(comment_list)

#긍부정 판단해서 점수 매기기
count_comment= len(comment_list);
count_pos=0;
count_neg=0;

for i in range(count_comment):
    print(comment_list[i])
    str = cl.classify(comment_list[i]);
    print(str)
    if eq(str,'긍정'):
        count_pos = count_pos+1;
    if eq(str,'부정'):
        count_neg = count_neg+1;
        

#웹에 띄워주기 (총댓글수 , 긍정 댓글 퍼센티지 띄워주기)

pos_percentage  = count_pos / count_comment * 100;

print(pos_percentage)

'''
config = {
    "apiKey": "AIzaSyBealjJBHfcbRlptxLcAoxdhpSbFswQOZg",
    "authDomain": "shareport-e85b2.firebaseapp.com",
    "databaseURL": "https://shareport-e85b2.firebaseio.com",
    "projectId": "shareport-e85b2",
    "storageBucket": "shareport-e85b2.appspot.com",g
    "messagingSenderId": "978150427508",
    "appId": "1:978150427508:web:115635132ce73e50223a21",
    "measurementId": 'G-1SB8TYEZ99'
}

firebase = firebase.initialize_app(config)

db = firebase.database()

default_app = firebase_admin.initialize_app()

app = Flask(__name__)

@app.route('/public/')

def report():
    testData = '80퍼센트가 긍정적인 답변을 하였습니다.'
    return render_template('report.html', testDataHtml=testData)

if __name__ =='__main__':
    app.run()
'''





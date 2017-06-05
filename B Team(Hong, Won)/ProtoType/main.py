# -*- coding: utf-8 -*-

#re.py

#---------------------------------

import os
from flask import Flask, request, jsonify


app = Flask(__name__)

@app.route('/keyboard')
def Keyboard():

    dataSend = {
        "type" : "buttons",
        "buttons" : ["시작하기", "도움말", "그만하기"]
    }

    return jsonify(dataSend)



@app.route('/message', methods=['POST'])
def Message():

    dataReceive = request.get_json()
    content = dataReceive['content']

    if content == u"시작하기":
        dataSend = {
            "message": {
                "text": "게임을 시작합니다. 당신의 키는 "+str(dataReceive['user_key'])
'''
                db에 유저 아이디 추가
                db에서 랜덤 단어 select >> 최근단어 DB 저장  >> 출력
'''
            }
        }

    elif content == u"그만하기":
        dataSend = {
            "message":{"text":"게임이 종료되었습니다."}

'''
                db에 유저 아이디 제거
'''
        }

    elif content == u"도움말":
        dataSend = {
            "message": {
                "text": "시작하기 : 게임 시작
                         그만하기 : 게임 종료"
            }
        }

    else:

'''
                시작하기, 그만하기, 도움말 이외에 입력받으면 최근단어 DB의 마지막 글자와 content 첫글자 비교
                위키백과에서 유효한 단어인지 비교,
                DB에서 contett 마지막 글자로 시작하는 랜덤 단어 출력 후 DB 최근단어 저장
'''
        dataSend = {
             "message": {
                "text": ""
            }
        }

    return jsonify(dataSend)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port = 5000)
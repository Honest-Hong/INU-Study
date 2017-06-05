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
        "buttons" : ["�����ϱ�", "����", "�׸��ϱ�"]
    }

    return jsonify(dataSend)



@app.route('/message', methods=['POST'])
def Message():

    dataReceive = request.get_json()
    content = dataReceive['content']

    if content == u"�����ϱ�":
        dataSend = {
            "message": {
                "text": "������ �����մϴ�. ����� Ű�� "+str(dataReceive['user_key'])
'''
                db�� ���� ���̵� �߰�
                db���� ���� �ܾ� select >> �ֱٴܾ� DB ����  >> ���
'''
            }
        }

    elif content == u"�׸��ϱ�":
        dataSend = {
            "message":{"text":"������ ����Ǿ����ϴ�."}

'''
                db�� ���� ���̵� ����
'''
        }

    elif content == u"����":
        dataSend = {
            "message": {
                "text": "�����ϱ� : ���� ����
                         �׸��ϱ� : ���� ����"
            }
        }

    else:

'''
                �����ϱ�, �׸��ϱ�, ���� �̿ܿ� �Է¹����� �ֱٴܾ� DB�� ������ ���ڿ� content ù���� ��
                ��Ű������� ��ȿ�� �ܾ����� ��,
                DB���� contett ������ ���ڷ� �����ϴ� ���� �ܾ� ��� �� DB �ֱٴܾ� ����
'''
        dataSend = {
             "message": {
                "text": ""
            }
        }

    return jsonify(dataSend)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port = 5000)
from flask import Flask, request

app = Flask(__name__)


@app.route('/verify')
def hello_world():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == '123' and password == '456':
            return 'true'
        else:
            return 'false'

    if request.method == 'GET':
        username = request.args.get('username', '')
        password = request.args.get('password', '')
        if username == '123' and password == '456':
            return 'true'
        else:
            return 'false'
    else:
        return 'use POST or GET.'

@app.route('/store')
# 存储versionName
def store_version():
    if request.method == 'POST':
        with open("version_info.txt","w") as f:
            pre_version = str(request.form['versionName'])
            f.write(pre_version)

    if request.method == 'GET':
        with open("version_info.txt","w") as f:
            pre_version = request.args.get('versionName','')
            print('request.args.get   '+pre_version)
            # app.logger.info("获取到版本号" + pre_version)
            f.write(str(pre_version))

    return "ok"




@app.route('/getPreVersion',methods=['POST','GET'])
def get_preversion():
    with open("version_info.txt", "r") as f:
        pre_version = f.read()
        return pre_version




@app.route('/download')
#读取之前的versionName,和现在的versionName进行对比，返回新版本的版本号，下载地址，apk
def download_version():
    # apkUrl = ""
    # #1,拿到旧版本的verisonMame
    # with open("version_info.txt", "w") as f:
    #     old_version = f.read();
    #
    # if request.method == 'POST':
    #     new_version = int(request.form['newVersion'])
    #
    # if request.method == 'GET':
    #     new_version = int(request.form['newVersion'])
    #
    # if new_version > old_version:
        # 返回新版本apk的下载地址
    apkUrl = "http://192.168.191.5:8000/app-debug.apk"
    return apkUrl


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')

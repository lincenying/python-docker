import os
from flask import Blueprint, render_template, request, send_from_directory, url_for, current_app

app = Blueprint('upload', __name__)

# 设置允许上传的文件类型
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg'])
# 设置上传文件存放的目录
UPLOAD_FOLDER = './uploads'

# 检查文件类型是否合法
def allowed_file(filename):
    # 判断文件的扩展名是否在配置项ALLOWED_EXTENSIONS中
    return '.' in filename and \
        filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route("/upload", methods=['GET', "POST"])
def uploadFile():
    if request.method == 'POST':
        responseType = request.args.get('type', 'html')
        # 获取上传过来的文件对象
        file = request.files['file']
        # 检查文件对象是否存在，且文件名合法
        if file and allowed_file(file.filename):
            # 去除文件名中不合法的内容
            filename = file.filename
            # 将文件保存在本地UPLOAD_FOLDER目录下
            file.save(os.path.join(current_app.config['ROOT_DIR'], UPLOAD_FOLDER, filename))
            if responseType == 'json':
                return {
                    'message': 'Upload Successfully',
                    'url': url_for('upload.uploaded_file', filename=filename)
                }
            else:
                return render_template('upload.twig', page="upload", message='Upload Successfully', url=url_for('upload.uploaded_file', filename=filename))
        else:    # 文件不合法
            if responseType == 'json':
                return {
                    'message': 'Upload Failed'
                }
            else:
                return render_template('upload.twig', page="upload", message='Upload Failed')
    else:    # GET方法
        return render_template('upload.twig', page="upload")
    
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)
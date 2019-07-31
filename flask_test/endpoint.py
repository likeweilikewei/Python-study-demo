"""
那么问题来了：为何要多此一举，为何要先把URL映射到端点上，再通过端点映射到视图函数上，为何不跳过中间的这个步骤？
原因就是采用这种方法能够使程序更高、更快、更强。例如蓝本。
蓝本允许我们把应用分割为一个个小的部分，现在admin蓝本中含有超级管理员级的资源，user蓝本中则含有用户一级的资源。
蓝本允许咱们把应用分割为一个个以命名空间区分的小部分：

"""

from flask import Flask, url_for

app = Flask(__name__)

# We can use url_for('foo_view') for reverse-lookups in templates or view functions
@app.route('/foo')
def foo_view():
    pass

# We now specify the custom endpoint named 'bufar'. url_for('bar_view') will fail!
@app.route('/bar', endpoint='bufar')
def bar_view():
    pass

with app.test_request_context('/'):
    print (url_for('foo_view'))  #/foo
    print (url_for('bufar'))  #/bar
    # url_for('bar_view') will raise werkzeug.routing.Buil

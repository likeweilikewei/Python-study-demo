"""
首先，我们导入了 Flask 类。这个类的实例将会是我们的 WSGI 应用程序。
接下来，我们创建一个该类的实例，第一个参数是应用模块或者包的名称。
如果你使用单一的模块（如本例），你应该使用 __name__ ，
因为模块的名称将会因其作为单独应用启动还是作为模块导入而有不同（ 也即是 '__main__' 或实际的导入名）。
这是必须的，这样 Flask 才知道到哪去找模板、静态文件等等。详情见 Flask 的文档。
然后，我们使用 route() 装饰器告诉 Flask 什么样的URL 能触发我们的函数。
这个函数的名字也在生成 URL 时被特定的函数采用，这个函数返回我们想要显示在用户浏览器中的信息。
最后我们用 run() 函数来让应用运行在本地服务器上。 其中 if __name__ == '__main__':
确保服务器只会在该脚本被 Python 解释器直接执行的时候才会运行，而不是作为模块导入的时候。
"""

from flask import Flask, request

app = Flask(__name__)


@app.route('/hello', methods=['get'])
def hello_world():
    data = request.values.get('data')
    print(data)
    return 'Hello World!'


if __name__ == '__main__':
    app.run()

"""
如果你禁用了 debug 或信任你所在网络的用户，你可以简单修改调用 run() 的方法使你的服务器公开可用，如下:

app.run(host='0.0.0.0')

调试模式
虽然 run() 方法适用于启动本地的开发服务器，但是你每次修改代码后都要手动重启它。这样并不够优雅，而且 Flask 可以做到更好。如果你启用了调试支持，服务器会在代码修改后自动重新载入，并在发生错误时提供一个相当有用的调试器。

有两种途径来启用调试模式。一种是直接在应用对象上设置:

app.debug = True
app.run()
另一种是作为 run 方法的一个参数传入:

app.run(debug=True)
两种方法的效果完全相同。
"""
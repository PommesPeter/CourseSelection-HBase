# 从app模块中导入app应用
from app import app
import os
# 防止被引用后执行，只有在当前模块中才可以使用
if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=9999)
# 随便改点东西

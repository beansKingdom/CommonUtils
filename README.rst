# CommonUtils

1. 修改setup中的版本

2. python setup.py sdist build

3. twine upload --skip-existing dist/*


### 项目Python版本
pip的一些操作
```bash
# 升级依赖包
pip install --upgrade BeanDateUtils

# 安装依赖包
pip install -r requirements.txt

# 更改依赖包文件
pip freeze > requirements.txt
```

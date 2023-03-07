

+ 如题

```cmd
Microsoft Windows [版本 10.0.19044.1682]
(c) Microsoft Corporation。保留所有权利。

(venv) E:\pythonProjects\moduleProject>pip list
Package    Version
---------- -------
pip        10.0.1
setuptools 39.1.0
You are using pip version 10.0.1, however version 23.0.1 is available.
You should consider upgrading via the 'python -m pip install --upgrade pip' command.
```

+ 解决

```cmd

python -m pip install --upgrade pip
```
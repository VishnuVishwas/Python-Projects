- Install VS Code
- Install pyenv
- Create virtual env with python version 3.10.6
  ```shell
    pyenv virtualenv 3.10.6 internship_python_base
  ```
- open the virtual env just created both using pyenv
  ```shell
    pyenv local internship_python_base
  ```
- For VS code you need to install extenstions
  - [python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
  - [Jupyter](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter)
  - [Markdown-Preview](https://marketplace.visualstudio.com/items?itemName=shd101wyy.markdown-preview-enhanced)
  - [Github](https://marketplace.visualstudio.com/items?itemName=GitHub.remotehub)
- In VS code at the bottom right corner, you will find the python-environment you are using. Please change to the above virtual environment by clicking it
- After opening the virtual env as mentioned you need install libraries from the requirements.txt
```shell
    pip install -r requirements.txt
```

- Please follow the [Example-Format](Example-Format) for every Chapter and Subchapter

  - I have written sample one [here](Example-Format/learnings/01_11_basic/). Please follow these structures for every folders
  - You can make any number .py files within learnings related to corresponding to chapter and subchapter.
  - Also i have provided [others](Example-Format/learnings/) where you can add your own learnings which does not correspond to any of the chapter or subchapters.
  - For assignments follow [this](Example-format/assignments/01_11_basic/)

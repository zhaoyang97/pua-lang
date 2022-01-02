
# pua-lang
PUA Programming Language written in Python.


## Installation
```
git clone https://github.com/zhaoyang97/pua-lang.git
cd pua-lang
pip install .  # or "python setup.py install"
```

PUA-lang has been released on pypi. Install it by running :arrow_down:. (Examples won't be downloaded.
```
pip install pua-lang
```


## Try pua-lang

```
pua docs\examples\斐波拉契.pua
```
Or copy the code below to `main.pua`
```pua
老板：
    张三 赋能 100
    李四 赋能 50
    打印（张三 差异 李四）
```
then run `pua main.pua`

You can try more examples in [docs\examples](docs/examples)


## Write your own PUA code
pua-lang完全基于python，将python关键词替换为pua-lang中的关键词即可写出pua代码。pua-lang与python之间的关键词映射在[keyword map](docs/keyword_map.md)表中。


## Design your OWN programming language based on this repo
将`src/config.py`中的[关键词映射](src/config.py)改为自己的字典，然后执行`pip install . `，就可以用自己设计的语言编程了。试试精灵语/祖安语/符文/波吉语？

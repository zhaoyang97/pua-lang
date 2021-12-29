

keyword = {
    # logic
    "和":"and",
    "且":"and",
    "或":"or",
    "或者":"or",
    "是的":"True",
    "非也":"False",
    "真": "True",
    "假":"False",
    "实":"True",
    "虛":"False",
    "空":"None",
    # def
    "定义":"def",
    "类":"class",
    "类別":"class",
    "我":"self",
    "自个儿":"self",
    "共用":"global",
    "全域":"global",
    # import
    "从":"from",
    "导入":"import",
    "作为":"as",
    # flow
    "返回":"return",
    "略过":"pass",
    "引发":"raise",
    "继续":"continue",
    # control
    "如果":"if",
    "假使":"elif",
    "否则如果":"elif",
    "否则":"else",
    # for loop
    "取":"for",
    "自":"in",
    "在":"in",
    "不在":"not in",
    # while loop
    "当":"while",
    "跳出":"break",
    "中断":"break",
    # try
    "尝试":"try",
    "异常":"except",
    "最后":"finally",
    "申明":"assert",
    # build in methods
    "执行":"exec",
    "函数":"lambda",
    "打印":"print",
    "伴隨":"with",
    "产生":"yield",
    # 
    "等于":"==",
    "不等于":"!=",
    "非": "not",
    "是":"is",
    "为":"is",
    "不是":"is not",
    "不为":"is not",
}

symbol = {
    "（":"(",
    "）":")",
    "：":":",
    "？":"?",
    "，":",",
    "。":".",
}

buildin_method = {
    "输入":"input",
    # build-in types
    "字符串":"str",
    "布尔":"bool",
    "列表": "list",
    "字典":"dict",
    "元组":"tuple",
    "集合":"set",
    "定集合":"frozenset",
    "符号":"chr",
    "符号转整数":"ord",
    "档案":"file",
    # number methods
    "整数":"int",
    "浮点数":"float",
    "复数":"complex",
    "十六进制":"hex",
    "绝对值":"abs",
    "比较":"cmp",
    # string methods
    "开头为":"startswith",
    "结尾为":"endswith",
    "连接":"join",
    "分离":"split",
    "代换":"replace",
    "编码":"encoding",
    "解码":"decoding",
    # list methods
    "加入":"append",
    "追加":"append",
    "扩展":"extend",
    "插入":"insert",
    "弹出":"pop",
    "下一笔":"next",
    "移除":"remove",
    "反转":"reverse",
    "计数":"count",
    "索引":"index",
    "排序":"sort",
    # dict methods
    "键列表":"keys",
    "值列表":"values",
    "项目列表":"items",
    "更新":"update",
    "拷贝":"copy",
    # set methods
    "清除":"clear",
    "加":"add",
    "丢弃":"discard",
    "联集":"union",
    "交集":"intersection",
    "差集":"difference",
    "对称差集":"symmetric_difference",
    # file methods
    "打开":"open",
    "读取":"read",
    "写入":"write",
    "读一行":"readline",
    "读多行":"readlines",
    "关闭":"close",
    # OO
    "可调用":"callable",
    "列出属性":"dir",
    "取属性":"getattr",
    "有属性":"hasattr",
    "设定属性":"setattr",
    "属性":"property",
    # build in functions
    "长度":"len",
    "最大值":"max",
    "最小值":"min",
    # build in methods
    "列举":"enumerate",
    "评估":"eval",
    "过滤":"filter",
    "映射":"map",
    "范围":"range",
    "快速范围":"xrange",
    "总和":"sum",
    "类型":"type",
    "对象":"object",
    "打包":"zip",
    "帮助":"help",
    "说明":"help",
    "区域变量":"locals",
    "全域变量":"globals",
    "类方法":"classmethod",
}

pua_word = {
    # ref: https://github.dev/flaneur2020/pua-lang/blob/master/README.md
    "老板":'if __name__=="__main__"',
    "闭环":"while",
    "三七五":"True",
    "三二五":"False",
    "赋能":"=",
    "抓手":"def",
    "反哺":"return",
    "组合拳":"list",

    "至少":">=",
    "至多":"<=",
    "迭代":"for",
    "细分":"zip",
    "对齐":"==",
    "联动":"+",
    "差异":"-",
    "倾斜":"/",
    "输出":"print",
    "淘汰":"exit",
    "量化":"//1",
}
"""
TODO: 
- pua词待转为python关键词: 组合拳, 载体, 赋能
- python关键词待转为pua词: *, 
"""


keyword_map = {}
keyword_map = dict(keyword_map, **keyword)
keyword_map = dict(keyword_map, **symbol)
keyword_map = dict(keyword_map, **buildin_method)
keyword_map = dict(keyword_map, **pua_word)


def md_generater(m=None):
    """Auto generate markdown file

    Args:
        maps: list of word map
    """
    import os.path
    cur_path = os.path.dirname(__file__)
    cur_path = cur_path.replace('src', 'docs')
    md_file = os.path.join(cur_path, 'keyword_map.md')
    if not m:
        with open(md_file, 'w', encoding='utf-8'):
            pass
        return 0
    with open(md_file, 'a+', encoding='utf-8') as file:
        file.write('\n')
        file.write('|python|pua-lang|\n')
        file.write('|---|---|\n')
        for k, v in m.items():
            file.write(f'|{v}|{k}|\n')
        file.write('\n')


if __name__ == '__main__':
    md_generater() # clear keyword_map.md
    md_generater(pua_word)
    md_generater(keyword)
    md_generater(symbol)
    md_generater(buildin_method)

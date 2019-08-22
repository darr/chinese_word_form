# Chinese word form
针对中文词语的笔画拆解，偏旁查询，拼音转换接口．  
当前的中文信息处理中，语言外部形式上的特征在各个任务中扮演着越来越重要的角色.  
本项目目的是为提供这一接口.  

# How to run?

```shell
bash run.sh
```

This command will create the environment that needed by the project.  
This project is created on the purposes of easy-on-run.  
If you want to know the details about the project, just read code.  

# reuslts

```shell
句子：自然语言处理是人工智能皇冠上的一颗明珠
笔画： ['丿丨𠃍一一一', '丿㇇丶丶一丿㇏丶丶丶丶丶', '丶㇊一丨𠃍一丨𠃍一', '丶一一一丨𠃍一', '丿㇇㇏丨丶', '一一丨㇀丨𠃍一一丨一一', '丨𠃍一一一丨一丿㇏', '丿㇏', '一丨一', '丿一一丿丶丨𠃍一丨𠃍一一', '𠃋丶丨㇆一一丿乚丿乚', '丿丨𠃍一一一一丨一', '丶㇇一一丿乚一亅丶', '丨一一', '丿丨𠃍一一丿㇆丶', '一', '丨𠃍一一一丨丿丶一丿丨𠃍丿丶', '丨𠃍一一丿㇆一一', '一一丨㇀丿一一丨丿㇏']
拼音： ['zi', 'ran', 'yu', 'yan', 'chu', 'li', 'shi', 'ren', 'gong', 'zhi', 'neng', 'huang', 'guan', 'shang', 'de', 'yi', 'ke', 'ming', 'zhu']
偏旁部首： ['自', '灬', '讠', '言', '夂', '王', '日', '人', '工', '日', '月', '白', '冖', '一', '白', '一', '页', '日', '王']


句子：在技术上，深度学习技术会越来越强，新的语言模型和编码器也会越来越好。
笔画： ['一丿丨一丨一', '一亅㇀一丨㇇㇏', '一丨丿㇏丶', '丨一一', '，', '丶丶㇀丶㇇丿丶一丨丿㇏', '丶一丿一丨丨一㇇㇏', '丶丶丿丶㇇㇇亅一', '㇆丶㇀', '一亅㇀一丨㇇㇏', '一丨丿㇏丶', '丿㇏一一𠃋丶', '一丨一丨一丿㇏一𠄌㇂丿丶', '一丶丿一丨丿㇏', '一丨一丨一丿㇏一𠄌㇂丿丶', '𠃍一㇉丨𠃍一丨𠃍一丨一丶', '，', '丶一丶丿一一亅丿丶丿丿一丨', '丿丨𠃍一一丿㇆丶', '丶㇊一丨𠃍一丨𠃍一', '丶一一一丨𠃍一', '一丨丿丶一丨丨丨𠃍一一一丿㇏', '一一丿丨丨亅一丨一', '丿一丨丿丶丨𠃍一', '𠃋𠃋㇀丶𠃍一丿丨㇆一丨丨', '一丿丨𠃍一𠃍㇉一', '丨𠃍一丨𠃍一一丿㇏丶丨𠃍一丨𠃍一', '㇆丨乚', '丿㇏一一𠃋丶', '一丨一丨一丿㇏一𠄌㇂丿丶', '一丶丿一丨丿㇏', '一丨一丨一丿㇏一𠄌㇂丿丶', '𡿨丿一㇇亅一', '。']
拼音： ['zai', 'ji', 'shu', 'shang', '，', 'shen', 'du', 'xue', 'xi', 'ji', 'shu', 'hui', 'yue', 'lai', 'yue', 'qiang', '，', 'xin', 'de', 'yu', 'yan', 'mo', 'xing', 'he', 'bian', 'ma', 'qi', 'ye', 'hui', 'yue', 'lai', 'yue', 'hao', '。']
偏旁部首： ['土', '扌', '木', '一', '，', '氵', '广', '子', '乙', '扌', '木', '人', '走', '木', '走', '弓', '，', '斤', '白', '讠', '言', '木', '土', '口', '纟', '石', '口', '乙', '人', '走', '木', '走', '女', '。']


句子：本项目是中文词语的笔画拆解，偏旁查询，拼音转换接口
笔画： ['一丨丿㇏一', '一丨㇀一丿丨𠃍丿丶', '丨𠃍一一一', '丨𠃍一一一丨一丿㇏', '丨𠃍一丨', '丶一丿㇏', '丶㇊㇆一丨𠃍一', '丶㇊一丨𠃍一丨𠃍一', '丿丨𠃍一一丿㇆丶', '丿一丶丿一丶丿一一乚', '一丨𠃍一丨一𠃊丨', '一亅㇀丿丿一丨丶', '丿㇇丿㇆一一丨㇆丿丿一一丨', '，', '丿丨丶𠃍一丿丨㇆一丨丨', '丶一丶丿丶㇇丶一㇆丿', '一丨丿㇏丨𠃍一一一', '丶㇊丿㇆丨𠃍一一', '，', '一亅㇀丶丿一一丿丨', '丶一丶丿一丨𠃍一一', '一𠃋丨㇀一一ㄣ丶', '一亅㇀丿㇇丨𠃍一丿㇏', '一亅㇀丶一丶丿一𡿨丿一', '丨𠃍一']
拼音： ['ben', 'xiang', 'mu', 'shi', 'zhong', 'wen', 'ci', 'yu', 'de', 'bi', 'hua', 'chai', 'jie', '，', 'pian', 'pang', 'cha', 'xun', '，', 'pin', 'yin', 'zhuan', 'huan', 'jie', 'kou']
偏旁部首： ['木', '工', '目', '日', '丨', '文', '讠', '讠', '白', '毛', '田', '扌', '角', '，', '亻', '方', '木', '讠', '，', '扌', '音', '车', '扌', '扌', '口']


句子：中文信息处理当中，语言外部形式上的特征在各个任务中扮演着越来越重要的角色
笔画： ['丨𠃍一丨', '丶一丿㇏', '丿丨丶一一一丨𠃍一', '丿丨𠃍一一一丶㇂丶丶', '丿㇇㇏丨丶', '一一丨㇀丨𠃍一一丨一一', '丨丶丿𠃍一一', '丨𠃍一丨', '，', '丶㇊一丨𠃍一丨𠃍一', '丶一一一丨𠃍一', '丿㇇丶丨丶', '丶一丶丿一丨𠃍一𠄎丨', '一一丿丨丿丿丿', '一一丨㇀㇂丶', '丨一一', '丿丨𠃍一一丿㇆丶', '丿一丨㇀一丨一一亅丶', '丿丿丨一丨一丨一', '一丿丨一丨一', '丿㇇㇏丨𠃍一', '丿㇏丨', '丿丨丿一丨一', '丿㇇㇏㇆丿', '丨𠃍一丨', '一亅㇀丿㇏㇆丿', '丶丶㇀丶丶㇇一丨𠃍一丨一丿丶', '丶丿一一一丿丨𠃍一一一', '一丨一丨一丿㇏一𠄌㇂丿丶', '一丶丿一丨丿㇏', '一丨一丨一丿㇏一𠄌㇂丿丶', '丿一丨𠃍一一丨一一', '一丨𠃍丨丨一𡿨丿一', '丿丨𠃍一一丿㇆丶', '丿㇇丿㇆一一丨', '丿㇇𠃍丨一乚']
拼音： ['zhong', 'wen', 'xin', 'xi', 'chu', 'li', 'dang', 'zhong', '，', 'yu', 'yan', 'wai', 'bu', 'xing', 'shi', 'shang', 'de', 'te', 'zheng', 'zai', 'ge', 'ge', 'ren', 'wu', 'zhong', 'ban', 'yan', 'zhe', 'yue', 'lai', 'yue', 'zhong', 'yao', 'de', 'jue', 'se']
偏旁部首： ['丨', '文', '亻', '心', '夂', '王', '彐', '丨', '，', '讠', '言', '夕', '阝', '彡', '弋', '一', '白', '牜', '彳', '土', '口', '人', '亻', '力', '丨', '扌', '氵', '目', '走', '木', '走', '里', '覀', '白', '角', '色']

```
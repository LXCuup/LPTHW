# -*- coding:utf-8 -*-
from urllib import urlopen
import sys,random

WORD_URL = "http://learncodethehardway.org/words.txt"  # txt链接
WORDS = []
#建立了一个描述代码句子的词典
PHRASES = {     
	"class %%%(%%%):": # 创建了一个%%%的类，它是%%%的一种
		"Make a class named %%% that is-a %%%.", 
	"class %%%(object):\n\tdef__init__(self,***)": # 类%%%有一个__init__接受self和***作为参数
		"class %%% has-a__init__that takes self and *** parameters.",
	"class %%%(object):\n\tdef ***(self,@@@)": # 类%%%有一个函数名称为***，它接收self和@@@作为参数
		"class %%% has-a function named *** that takes self and @@@ parameters.",
	"*** = %%%()": # 将***设为类%%%的一个实例
		"Set *** to an instance of class %%%.",
	"***.***(@@@)":  # 从***中找到***函数，并使用self和@@@参数调用它
		"From *** get the *** function,and call it with parameters self,@@@.",
	"***.*** = '***'": # 从***中获取***属性，并将其设为***
		"From *** get the *** attribute and set it to '***'."
}

# do they want to drill phrases first
PHRASE_FIRST = False

if len(sys.argv) == 2 and sys.argv[1] == "english": # 如果给出2个参数且第二个参数为english
	PHRASE_FIRST  = True
	print "L28_sys.argv[1]:",sys.argv[1]

# load up the words from the website
for word in urlopen(WORD_URL).readlines(): # 从链接中读取txt文档，并添加到 WORDS列表 中
	WORDS.append(word.strip())
print "L31_WORDS: ", WORDS


def convert(snippet,phrase):
	class_names = [w.capitalize() for w in random.sample(WORDS,snippet.count("%%%"))]
	print"L36_class_names: " ,class_names
	# 统计snippet 中 %%% 的数量，从 WORDS 中随机截取指定长度的片段 且首字母大写
	other_names = random.sample(WORDS,snippet.count("***"))
	print "L39_other_names: " ,other_names
	# 统计snippet 中 *** 的数量，从 WORDS 中随机截取指定长度的片段
	results = []
	print "L42_results: ",results
	param_names = []
	print "L44_param_names: ",param_names

	for i in range(0,snippet.count("@@@")):
		param_count = random.randint(1,3)
		print "L48_param_count: ",param_count
		param_names.append(','.join(random.sample(WORDS,param_count)))
		print "L50: ",param_names.append(','.join(random.sample(WORDS,param_count)))

	for sentence in snippet,phrase:
		result = sentence[:] # result 先是背赋值snippet，之后又被赋值phrase。
		print "L54_result: ",result

		# fake class names
		for word in class_names:
			result = result.replace("%%%",word,1)
			print "L59_result: ",result

		# fake other names
		for word in other_names:
			result = result.replace("***",word,1)
			print "L64_result: ",result

		#fake parameter lists
		for word in param_names:
			result = result.replace("@@@",word,1)
			print "L69_result: ",result

		results.append(result)
		print "L72_results: ",results

	return results


# keep going until they hit CTRL-D
try:
	while True:
		snippets = PHRASES.keys() # 以列表返回 PHRASES 中的所有的键
		print "L81_snippets: ",snippets
		random.shuffle(snippets) # 将列表中键的顺序打乱
		print "L83_random.shuffle(snippets): ",random.shuffle(snippets)


		for snippet in snippets:
			phrase = PHRASES[snippet] # 提取key值对应的value
			# 假设此时的snippet 为 class %%%(%%%) 此时 phrase 为 Make a class named %%% that is-a %%%.
			print "L89_phrase: ",phrase

			question,answer = convert(snippet,phrase) #代入单词
			if PHRASE_FIRST:
 
				question,answer =  answer,question

			print "L95_question: ",question
			# 传递参数
			raw_input(">")	
			print "ANSWER:  %s\n\n" %answer
			print sys.argv[0]
			print "\n"
except EOFError: #异常情况处理
	print "\nBye"
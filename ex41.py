# -*- encoding:utf-8 -*-
import random
from urllib import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

PHRASES = {
	"class %%%(%%%):":
	 "Make a class named %%% that is-a %%%.",
	"class %%%(object):\n\tdef __init__(self,***)" :
	 "class %%% has-a __init__ that takes self and *** parameters.",
	"class %%%(object):\n\tdef ***(self,@@@)":
		"class %%% has-a function named *** that takes self and @@@ parameters.",
	"*** = %%%()":
		"Set *** to an instance of class %%%",
	"***.***(@@@)":
		"From *** get the *** function, and call it with parameters self, @@@.",
	"***.*** = '***'":
		"From *** get the *** attribute and set it to '***'."
}

# do they want to drill phrases first
PHRASE_FIRST = False
if len(sys.argv) == 2 and sys.argv[1] == "english": # sys.argv就是保存命令行参数的变量，通过它你可以获取到命令行中传入的参数，从而执行不同的条件分支。或者不同的功能。
	PHRASE_FIRST = True
	
# load up the words from the website
for word in urlopen(WORD_URL).readlines(): #打开一个网页获取所有的内容，按行拆分  
	WORDS.append(word.strip()) 
	# 声明：s为字符串，rm为要删除的字符序列
	#	s.strip(rm)    删除s字符串中开头、结尾处，位于 rm删除序列的字符
	#	s.lstrip(rm)   删除s字符串中开头处，位于 rm删除序列的字符
	#	s.rstrip(rm)   删除s字符串中结尾处，位于 rm删除序列的字符
	#	注意：1. 当rm为空时，默认删除空白符（包括'\n', '\r',  '\t',  ' ')；2.这里的rm删除序列是只要边（开头或结尾）上的字符在删除序列内，就删除掉。
	

def convert(snippet, phrase):
	class_names = [w.capitalize() for w in # Python capitalize()将字符串的第一个字母变成大写,其他字母变小写。对于 8 位字节编码需要根据本地环境。
				   random.sample(WORDS, snippet.count("%%%"))] # random.sample(sequence, k)，从指定序列中随机获取指定长度的片断。sample函数不会修改原有序列
	other_names = random.sample(WORDS, snippet.count("***"))
	results = []
	param_names = []
	
	for i in range(0, snippet.count("@@@")):
		param_count = random.randint(1,3) # random.randint(a, b)，用于生成一个指定范围内的整数。其中参数a是下限，参数b是上限，生成的随机数n: a <= n <= b
		param_names.append(', '.join(random.sample(WORDS, param_count)))# Python join() 方法用于将序列中的元素以指定的字符连接生成一个新的字符串。
		
	for sentence in snippet, phrase:
		result = sentence[:]
		
		# fake class names
		for word in class_names:
			result = result.replace("%%%", word, 1) # str.replace(old, new[, max])；Python replace() 方法把字符串中的 old（旧字符串） 替换成 new(新字符串)，如果指定第三个参数max，则替换不超过 max 次。
			
		# fake other names 
		for word in other_names:
			result = result.replace("***", word, 1)
			
		# fake parameter lists
		for word in param_names:
			result = result.replace("@@@", word, 1)
			
		results.append(result)
	
	return results
	

# keep going until they hit CTRL-D
try:
	while True:
		snippets = PHRASES.keys()
		random.shuffle(snippets) # random.shuffle(x[, random])，用于将一个列表中的元素打乱。
		
		for snippet in snippets:
			phrase = PHRASES[snippet]
			question, answer = convert(snippet, phrase)
			if PHRASE_FIRST:
				question, answer = answer, question
				
			print question
			
			raw_input("> ")
			print "ANSWER: %s\n\n" % answer
except EOFError:
	print "\nBye"

a = 'hello worLD '

#字符串转换
print(a.title())
print(a.upper())
print(a.lower())

#字符串拼接
first_name = "bai yun ce "
print("hello, " + first_name.title() + "!")

#制表符 换行符
print("\tbaiyunce ")
print("\nbaiyunce ")
print("\t\nbaiyunce ")
print("\n\tbaiyunce ")#\n在前\t才能生效

#删除空白 lstrip(),rstrip(),strip()
test1 = "baiyc  "
test2 = "  sunjy"
print(test1 + test2)
print(test1.rstrip() + test2.rstrip())
print(test1.lstrip() + test2.lstrip())
print(test1.strip().upper() + test2.title().strip())


#例子
ming_yan = "You got a dream, you gotta protect it. People can't do something themselves,they wanna tell you you can't do it.If you want something, go get it."
name = " hris gardner "

print(name.title() +  'said: "' + ming_yan + '"')
print(name.title() +  "said: \"" + ming_yan + "\"")
print(name.title().strip() + 'said: "' + ming_yan + '"')
print(name.title().strip() + 'said: ' + '\n\t"' + ming_yan + '"')






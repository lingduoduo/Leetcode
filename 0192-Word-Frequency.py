tr -s ' ' '\n' < words.txt | sort | uniq -c | sort -nr | awk '{print $2, $1}'
-s参数表示如果发现连续的字符，就把它们缩减为1个，而后面的‘ ’和‘\n'就是空格和回车

grep -oE '[a-z]+' words.txt | sort | uniq -c | sort -nr | awk '{print $2" "$1}' 
-oE '[a-z]+'参数表示原文本内容变成一个单词一行的存储方式
# conding : utf-8
# author : 小猪佩奇

from urllib.parse import urlencode

str = {'name':'xiaowang','password':'123456','email':'1101253917@qqq.com'}
x= print(urlencode(str))

# for i in range (len(str)):
#     print(i)
#     if str[i]=='xiaowang':
#         print(qinaide)
for i in str:
    print(i)


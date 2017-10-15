import requests,time
from bs4 import BeautifulSoup
url = 'https://www.zhihu.com/login/phone_num'
def get_captcha(data): #保存验证码
    with open('captcha.gif','wb') as fb:
        fb.write(data)
    return input('captcha')
#
def login(username,password,oncaptcha):
    sessiona = requests.Session()
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'}
    xyz = sessiona.get('https://www.zhihu.com/#signin',headers=headers).content
    _xsrf = BeautifulSoup(sessiona.get('https://www.zhihu.com/#signin',headers=headers).content,'html.parser').find('input',attrs={'name':'_xsrf'}).get('value')
    captcha_content = sessiona.get('https://www.zhihu.com/captcha.gif?r=%d&type=login'%(time.time()*1000),headers=headers).content  #此处实时通过url获取动态验证码
    data = {
        "_xsrf":_xsrf,
        "phone_num":username,
        "password":password,
        "remember_me":True,
        "captcha":oncaptcha(captcha_content)
    }
    resp = sessiona.post('https://www.zhihu.com/login/phone_num',data,headers=headers).json()  #解析json格式
    res=sessiona.get('http://www.zhihu.com',headers=headers).text
    soup=BeautifulSoup(res,'lxml')
    titles=soup.find('.ContentItem-title >a')
 #   names=soup.find_all('a',attrs={'target':"_blank",'data-za-detail-view-element_name':"Title"})
    data={
        'titles':titles
  #      'names':names
    }
    print(resp,data)
    return resp             #此处必须返回resp否则无法提取登录后的网页

#    names=soup.find_all('a',attrs={'class'="UserLink-link"})
  #

#@?r=%d&type=login'%(time.time()*1000
if __name__ == "__main__":
    login('18271656694','xgy118',get_captcha)
#hashlib模块哈希算法
import hashlib
m = hashlib.md5()# 构建一个哈希对象,创建工场
m.update('hash3714'.encode('utf-8'))#update加密'hello'（给工厂添加原材料）

print(m.hexdigest())#输出产品


#撞库破解hash算法加密
#我们在知道hash值的情况下，可以对可能的密码进行尝试，比较哈希值，实现找到密码
pwd_list = [
    'hash3714',
    'hash1313',
    'hash94139413',
    'hash123456',
    '123456hash',
    'h123ash',
]
hash_pwd = '7af2206ac2889482833f8b3a1582fbd6'

#把pwd_list全部变成hash:要对应一个哈希值和一个密码
#把pwd_list里面的内容和hash_pwd 比较
def hashing_pwd(list):
    pwd = {}
    for i in list:
        m = hashlib.md5()
        m.update(i.encode('utf-8'))
        pwd[i] = m.hexdigest()#密码：哈希密码#注意点方法后面一般会有（）
    return pwd

def Breaking_lib(pwd_dict,hash_pwd):
    for k,v in pwd_dict.items():
        if v == hash_pwd:
            print(f'The real password is:{k}')
            real_pwd = k
    return real_pwd
            
pwd_dict = hashing_pwd(pwd_list)
pwd = Breaking_lib(pwd_dict,hash_pwd)
print(pwd)

#有撞库就有防止撞库
#hmac模块防止撞库
import hmac
h1 = hmac.new(b"hash",digestmod = 'md5')#只接受binary#创建对象并第一次加密
h1.update(b'hello')
h1.update(b'world')
print(h1.hexdigest())

h2 = hmac.new(b'hash',digestmod = 'md5')
h2.update(b'helloworld')
print(h2.hexdigest())

h3 = hmac.new(b'hash',b'helloworld',digestmod='md5')
print(h3.hexdigest())
#这三个都是一样的结果
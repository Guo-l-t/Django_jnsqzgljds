import time
import pymysql
from backend.models import User, Vote_session


def login(date):
    # username = date[0]
    # pwd = date[1]
    # u = models.user.objects.all()
    u = User.objects.filter(username=date[0])
    if len(u) == 0:
        return ['用户名错误']
    else:
        for i in u:
            if i.password == date[1]:
                r = {}
                r['danwei'] = i.danwei
                r['zkjsz'] = i.zkjsz
                r['fkjsz'] = i.fkjsz
                r['sjgjjz'] = i.sjgjjz
                r['yejjz'] = i.yejjz
                r['ssjjz'] = i.ssjjz
                r['yejjy'] = i.yejjy
                r['jggq'] = i.jggq
                r['sjb'] = i.sjb
                return [1, r]
        return ['密码错误']


def get_user_vote_state(u_name):
    u1 = User.objects.filter(username=u_name)
    r = {}
    for i in u1:
        r['danwei'] = i.danwei
        r['zkjsz'] = i.zkjsz
        r['fkjsz'] = i.fkjsz
        r['sjgjjz'] = i.sjgjjz
        r['yejjz'] = i.yejjz
        r['ssjjz'] = i.ssjjz
        r['yejjy'] = i.yejjy
        r['jggq'] = i.jggq
        r['sjb'] = i.sjb
    return r


def update_user_vote_state(date):
    if date[1] == 'danwei':
        u = User.objects.filter(username=date[0])
        u.update(danwei=1)
    elif date[1] == 'zkjsz':
        u = User.objects.filter(username=date[0])
        u.update(zkjsz=1)
    elif date[1] == 'fkjsz':
        u = User.objects.filter(username=date[0])
        u.update(fkjsz=1)
    elif date[1] == 'sjgjjz':
        u = User.objects.filter(username=date[0])
        u.update(sjgjjz=1)
    elif date[1] == 'yejjz':
        u = User.objects.filter(username=date[0])
        u.update(yejjz=1)
    elif date[1] == 'ssjjz':
        u = User.objects.filter(username=date[0])
        u.update(ssjjz=1)
    elif date[1] == 'yejjy':
        u = User.objects.filter(username=date[0])
        u.update(yejjy=1)
    elif date[1] == 'jggq':
        u = User.objects.filter(username=date[0])
        u.update(jggq=1)
    elif date[1] == 'sjb':
        u = User.objects.filter(username=date[0])
        u.update(sjb=1)
    else:
        print('------')
        print('------')
        print('------')
        print('用户' + date[0] + '没有投票类型：：：' + date[1])
        print('------')
        print('------')
        print('------')
    # models.User.objects.filter(username=uname).update(danwei='1')


def insert_user_vote_session(date):
    u_name = date[0]
    u_leixing = date[1]
    u_daan = date[2]
    t = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print(u_daan)
    for i in u_daan:
        btpr = i[0]
        voting_result = i[1]
        v = Vote_session(voter=u_name, voting_object=btpr, voting_results=voting_result,
                         voting_object_type=u_leixing, voting_time=t, voting_update_time="",
                         f1="", f2="", f3="", f4="", f5="")
        v.save()  # 调用save方法进行保存


def get_all_users():
    u = User.objects.all()
    return u



    #print('--------------------------------------')
    #print(date[2])
    #for i in u_daan:
    #    btpr = i['qname']
    #    choices = i['choices']
    #    voting_result = ''
    #    for j in choices:
    #        if j['flag'] is True:
    #            voting_result = j['flag_m']
    #            v = Vote_session(voter=u_name, voting_object=btpr, voting_results=voting_result,
    #                             voting_object_type=u_leixing, voting_time=t, voting_update_time="",
    #                             f1="", f2="", f3="", f4="", f5="")
    #            v.save()  # 调用save方法进行保存
    #    print(u_name + '对   ' + btpr + '的投票结果是：：：' + voting_result + '  ' + str(t))
    #print('--------------------------------------')

import pymysql
from backend.models import User


def login(date):
    u = User.objects.filter(username=date[0])
    print(User.objects.filter(username=date[0]).query)
    if len(u) == 0:
        return '用户名错误'
    else:
        for i in u:
            if i.password == date[1]:
                return 1
        return '密码错误'


def get_user_vote_state(date):
    u1 = User.objects.filter(username=date[0])
    print(User.objects.filter(username=date[0]).query)
    r = {}
    for i in u1:
        r['zkjsz'] = i.zkjsz
        r['jggq'] = i.jggq
    return r






# import json
#
# if __name__ == '__main__':
#     data = [
#         {'qid': 1,
#         'qname': '政治处',
#         'choices': [
#             {'cindex': 0, 'flag': True, 'flag_m': '好'},
#             {'cindex': 1, 'flag': False, 'flag_m': '较好'},
#             {'cindex': 2, 'flag': False, 'flag_m': '一般'},
#             {'cindex': 3, 'flag':False, 'flag_m': '差'}]},
#         {'qid': 2,
#          'qname': '办公室',
#          'choices': [
#              {'cindex': 0, 'flag': False, 'flag_m': '好'},
#              {'cindex': 1, 'flag': True, 'flag_m': '较好'},
#              {'cindex': 2, 'flag': False, 'flag_m': '一般'},
#              {'cindex': 3, 'flag': False, 'flag_m': '差'}]},
#         {'qid': 3,
#          'qname': '强戒一大队',
#          'choices': [
#              {'cindex': 0, 'flag': False, 'flag_m': '好'},
#              {'cindex': 1, 'flag': False, 'flag_m': '较好'},
#              {'cindex': 2, 'flag': True, 'flag_m': '一般'},
#              {'cindex': 3, 'flag': False, 'flag_m': '差'}]},
#         {'qid': 4,
#          'qname': '强戒二大队',
#          'choices': [
#              {'cindex': 0, 'flag': True, 'flag_m': '好'},
#              {'cindex': 1, 'flag': False, 'flag_m': '较好'},
#              {'cindex': 2, 'flag': False, 'flag_m': '一般'},
#              {'cindex': 3, 'flag': False, 'flag_m': '差'}]},
#         {'qid': 5,
#          'qname': '强戒三大队',
#          'choices': [
#              {'cindex': 0, 'flag': False, 'flag_m': '好'},
#              {'cindex': 1, 'flag': True, 'flag_m': '较好'},
#              {'cindex': 2, 'flag': False, 'flag_m': '一般'},
#              {'cindex': 3, 'flag': False, 'flag_m': '差'}]},
#         {'qid': 6,
#          'qname': '强戒四大队',
#          'choices': [
#              {'cindex': 0, 'flag':False, 'flag_m': '好'},
#              {'cindex': 1, 'flag': False, 'flag_m': '较好'},
#              {'cindex': 2, 'flag': True, 'flag_m': '一般'},
#              {'cindex': 3, 'flag': False, 'flag_m': '差'}]},
#         {'qid': 7,
#          'qname': '强戒五大队',
#          'choices': [
#              {'cindex': 0, 'flag': True, 'flag_m': '好'},
#              {'cindex': 1, 'flag': False, 'flag_m': '较好'},
#              {'cindex': 2, 'flag': False, 'flag_m': '一般'},
#              {'cindex': 3, 'flag': False, 'flag_m': '差'}]},
#         {'qid': 8,
#          'qname': '装备财务科',
#          'choices': [
#              {'cindex': 0, 'flag': False, 'flag_m': '好'},
#              {'cindex': 1, 'flag': True, 'flag_m': '较好'},
#              {'cindex': 2, 'flag': False, 'flag_m': '一般'},
#              {'cindex': 3, 'flag': False,'flag_m': '差'}]},
#         {'qid': 9,
#          'qname': '生活后勤科',
#          'choices': [
#              {'cindex': 0, 'flag': False, 'flag_m': '好'},
#              {'cindex': 1, 'flag': True, 'flag_m': '较好'},
#              {'cindex': 2, 'flag': False, 'flag_m': '一般'},
#              {'cindex': 3, 'flag': False, 'flag_m': '差'}]}]
#     for i in data:
#         btpr = i['qname']
#         choices = i['choices']
#         flag_m = ''
#         for j in choices:
#             if j['flag'] is True:
#                 flag_m = j['flag_m']
#         print(btpr+'的投票结果是：：：'+flag_m)
#

import json
import xlrd
from django.db import transaction
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import simplejson
from backend.models import User
from utils import user, btpr, count_youxiu
import urllib.parse


def index(request):
    return render(request, 'index.html')


def login(request):
    print('方法 loginlogin 已运行已运行')
    method = request.method
    if method == 'POST':
        print('请求请求方式方式为为     POST')
        username = request.POST.get('user',None)
        pwd = request.POST.get('pwd',None)
        date = [username, pwd]
        print(date)
        r = user.login(date)
        if r == '密码错误':
            # 提示密码错误
            return HttpResponse("密码错误")
        elif r == '用户名错误':
            # 用户名错误
            return HttpResponse("用户名错误")
        else:
            # 登录成功
            return render(request, 'zong.html')


def vx_xxx_login(request):
    print('已进入已进入   vx_xxx_login 方法方法')
    # print(WSGIRequest)
    print(request.body)

    if request.method == 'POST':
        # u_name = request.POST.get('username', None)
        # pwd = request.POST.get('pwd', None)
        # date = [u_name, pwd]
        #  req = simplejson.loads(request.body)
        req = str(request.body)
        re = req.split('&')
        u_name = re[0].split('=')[1]
        pwd = re[1].split('=')[1][:-1]
        date = [u_name, pwd]
        r = user.login(date)
        if r[0] == '密码错误':
            # 提示密码错误
            data = {
                'message': '密码错误'
            }
            return JsonResponse(json.dumps(data), safe=False)
        elif r[0] == '用户名错误':
            # 用户名错误
            data = {
                'message': '用户名错误'
            }
            return JsonResponse(json.dumps(data), safe=False)
        else:
            # 登录成功
            data = {
                'message': 'success',
                'state': r[1]
            }
            return JsonResponse(json.dumps(data), safe=False)
    else:
        # 登录成功
        data = {
            'message': 'get方法请求'
        }
        return JsonResponse(json.dumps(data), safe=False)


def vx_xxx_btpr(request):
    if request.method == 'POST':
        # req = simplejson.loads(request.body)
        req = str(request.body)
        re = req.split('&')
        u_leixing = re[0].split('=')[1][:-1]
        date = [u_leixing]
        print(date)
        r = btpr.get_btpr(date)
        count_yx = count_youxiu.getCount(date)
        date_i = []
        for i in r:
            date_i.append(i.xingming)
        for j in count_yx:
            date_i.append(j.count_youxiu)
    data = {
        'message': date_i
    }
    return JsonResponse(json.dumps(data), safe=False)
    #     elif r == '用户名错误':
    #         # 用户名错误
    #         data = {
    #             'message': '用户名错误'
    #         }
    #         return JsonResponse(json.dumps(data), safe=False)
    #     else:
    #         # 登录成功
    #         data = {
    #             'message': 'success'
    #         }
    #         return JsonResponse(json.dumps(data), safe=False)
    # else:
    #     # 登录成功
    #     data = {
    #         'message': 'get方法请求'
    #     }
    #     return JsonResponse(json.dumps(data), safe=False)


def vx_xxx_insert_tpxx(request):
    r = {}
    if request.method == 'POST':
        # req = simplejson.loads(request.body)       
        req=urllib.parse.unquote(str(request.body, encoding = "utf8"))
        print(req)
        req_a = req.split('&')
        u_leixing = req_a[0].split('=')[1]
        u_name = req_a[1].split('=')[1]
        req_aa = req_a[2][15:]        
        req_aaa = req_aa.split('#')
        u_daan = []
        for i in req_aaa:
          aaa = i.split('-')
          u_daan.append(aaa)
        del u_daan[-1] 
        date = [u_name, u_leixing]
        date_vote_session = [u_name, u_leixing, u_daan]
        user.insert_user_vote_session(date_vote_session)
        user.update_user_vote_state(date)
        r = user.get_user_vote_state(u_name)
        # count_yx = count_youxiu.getCount(date)
    return JsonResponse(json.dumps(r), safe=False)


def upload(request):
    if request.method == 'POST':
        f = request.FILES.get('file')
        excel_type = f.name.split('.')[1]
        if excel_type in ['xlsx', 'xls']:
            # 开始解析上传的excel表格
            wb = xlrd.open_workbook(filename=None, file_contents=f.read())
            table = wb.sheets()[0]
            rows = table.nrows  # 总行数

            with transaction.atomic():  # 控制数据库事务交易
                for i in range(1, rows):
                    rowVlaues = table.row_values(i)
                    print(rowVlaues)
                    # 创建Book实例化对象
                    User1 = User(username=rowVlaues[0], zhanghao=rowVlaues[1], password=rowVlaues[2], user_level='0',
                                 f1="", f2="", f3="", f4="", f5="")
                    User1.save()  # 调用save方法进行保存
                    # major = models.TMajor.objects.filter(majorid=rowVlaues[1]).first()
                    # models.TGrade.objects.create(gradeid=rowVlaues[0], major=major, gradename=rowVlaues[2],
                    #                              memo=rowVlaues[3])

            return HttpResponse("导入成功")
        else:
            print('上传文件类型错误！')
            return HttpResponse("导入失败")





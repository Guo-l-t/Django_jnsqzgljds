import json
from io import BytesIO
import xlrd
from django.db import transaction
from django.http import HttpResponse, JsonResponse, StreamingHttpResponse
from django.shortcuts import render
from xlwt import Workbook
from backend.models import User
from utils import user, btpr, count_youxiu, vote_session
import urllib.parse


def index(request):
    return render(request, 'index.html')


def login(request):
    method = request.method
    if method == 'POST':
        username = request.POST.get('user', None)
        pwd = request.POST.get('pwd', None)
        date = [username, pwd]
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
    # print(WSGIRequest)
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
        req=urllib.parse.unquote(str(request.body, encoding="utf8"))
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


def get_datatables(request):
    data_list = []
    u = user.get_all_users()
    for data_info in u:
        data_list.append({
            'username': data_info.zhanghao,
            'danwei': data_info.danwei.replace(str(1), '已测评').replace(str(0), '未测评'),
            'zkjsz': data_info.zkjsz.replace(str(1), '已测评').replace(str(0), '未测评'),
            'fkjsz': data_info.fkjsz.replace(str(1), '已测评').replace(str(0), '未测评'),
            'sjgjjz': data_info.sjgjjz.replace(str(1), '已测评').replace(str(0), '未测评'),
            # 'yejjz': data_info.yejjz.replace(str(1), '已测评').replace(str(0), '未测评'),
            'ssjjz': data_info.ssjjz.replace(str(1), '已测评').replace(str(0), '未测评'),
            # 'yejjy': data_info.yejjy.replace(str(1), '已测评').replace(str(0), '未测评'),
            'sjb': data_info.sjb.replace(str(1), '已测评').replace(str(0), '未测评'),
            'jggq': data_info.jggq.replace(str(1), '已测评').replace(str(0), '未测评'),
        })
    data_dic = {'data': data_list}
    return HttpResponse(json.dumps(data_dic))


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


def download_result(request):
    # danwei 单位 zkjsz 正科级实职 fkjsz 副科级实职  sjgjjz 四级高级警长  yejjz 一二级警长  ssjjz 三四级警长
    # yejjy 一二级警员  jggq 机关工勤  sjb 事业编
    btpr_r = ['danwei', 'zkjsz', 'fkjsz', 'sjgjjz',  'ssjjz',  'jggq', 'sjb']
    # btpr_r = ['danwei', 'zkjsz', 'fkjsz', 'sjgjjz', 'yejjz', 'ssjjz', 'yejjy', 'jggq', 'sjb']
    danwei = []
    # 正科级实职
    zkjsz = []
    # 副科级实职
    fkjsz = []
    # 四级高级警长
    sjgjjz = []
    # 一二级警长
    yejjz = []
    # 三四级警长
    ssjjz = []
    # 一二级警员
    yejjy = []
    # 机关工勤
    jggq = []
    # 事业编
    sjb = []
    for i in btpr_r:
        b = btpr.get_btpr([str(i)])
        u_btpr = ''
        u_leixing = ''
        u_result = ''
        count_a = 0
        count_b = 0
        count_c = 0
        count_d = 0
        for j in b:
            # 按照姓名查询result_session表所有结果
            v_ses = vote_session.get_vote_session([str(j.xingming)])
            for k in v_ses:
                u_result = k.voting_results
                u_btpr = k.voting_object
                u_leixing = k.voting_object_type
                if (u_result == "好") or (u_result == "优秀"):
                    count_a = count_a+1
                elif (u_result == "较好") or (u_result == "称职") or (u_result == "合格"):
                    count_b = count_b+1
                elif (u_result == "一般") or (u_result == "基本称职") or (u_result == "基本合格"):
                    count_c = count_c+1
                elif (u_result == "差") or (u_result == "不称职") or (u_result == "不合格"):
                    count_d = count_d + 1
            if u_leixing == 'danwei':
                danwei.append({
                    'u_btpr': u_btpr,
                    'u_leixing': u_leixing,
                    # 'u_result': u_result,
                    'count_a': count_a,
                    'count_b': count_b,
                    'count_c': count_c,
                    'count_d': count_d
                })
            elif u_leixing == 'zkjsz':
                zkjsz.append({
                    'u_btpr': u_btpr,
                    'u_leixing': u_leixing,
                    # 'u_result': u_result,
                    'count_a': count_a,
                    'count_b': count_b,
                    'count_c': count_c,
                    'count_d': count_d
                })
            elif u_leixing == 'fkjsz':
                fkjsz.append({
                    'u_btpr': u_btpr,
                    'u_leixing': u_leixing,
                    # 'u_result': u_result,
                    'count_a': count_a,
                    'count_b': count_b,
                    'count_c': count_c,
                    'count_d': count_d
                })
            elif u_leixing == 'sjgjjz':
                sjgjjz.append({
                    'u_btpr': u_btpr,
                    'u_leixing': u_leixing,
                    # 'u_result': u_result,
                    'count_a': count_a,
                    'count_b': count_b,
                    'count_c': count_c,
                    'count_d': count_d
                })
            elif u_leixing == 'yejjz':
                yejjz.append({
                    'u_btpr': u_btpr,
                    'u_leixing': u_leixing,
                    # 'u_result': u_result,
                    'count_a': count_a,
                    'count_b': count_b,
                    'count_c': count_c,
                    'count_d': count_d
                })
            elif u_leixing == 'ssjjz':
                ssjjz.append({
                    'u_btpr': u_btpr,
                    'u_leixing': u_leixing,
                    # 'u_result': u_result,
                    'count_a': count_a,
                    'count_b': count_b,
                    'count_c': count_c,
                    'count_d': count_d
                })
            elif u_leixing == 'yejjy':
                yejjy.append({
                    'u_btpr': u_btpr,
                    'u_leixing': u_leixing,
                    # 'u_result': u_result,
                    'count_a': count_a,
                    'count_b': count_b,
                    'count_c': count_c,
                    'count_d': count_d
                })
            elif u_leixing == 'jggq':
                jggq.append({
                    'u_btpr': u_btpr,
                    'u_leixing': u_leixing,
                    # 'u_result': u_result,
                    'count_a': count_a,
                    'count_b': count_b,
                    'count_c': count_c,
                    'count_d': count_d
                })
            elif u_leixing == 'sjb':
                sjb.append({
                    'u_btpr': u_btpr,
                    'u_leixing': u_leixing,
                    # 'u_result': u_result,
                    'count_a': count_a,
                    'count_b': count_b,
                    'count_c': count_c,
                    'count_d': count_d
                })
            # print(u_btpr+'---'+str(count_a)+'---'+str(count_b)+'---'+str(count_c)+'---'+str(count_d))
            # print(zkjsz)
            # print(fkjsz)
            u_btpr = ''
            u_leixing = ''
            u_result = ''
            count_a = 0
            count_b = 0
            count_c = 0
            count_d = 0
    # for i in danwei:
    #     print(i['u_btpr']+'---'+i['u_leixing']+'----'+str(i['count_a'])+'----'+str(i['count_b'])+'----'+str(i['count_c'])+'----'+str(i['count_d']))

    # 创建工作簿
    ws = Workbook(encoding='utf-8')
    # 单位测评sheet页
    # w = ws.add_sheet(u"单位测评结果")
    # # 写入表头
    # w.write(0, 0, u'测评单位')
    # w.write(0, 1, u'好 个数')
    # w.write(0, 2, u'较好 个数')
    # w.write(0, 3, u'一般 个数')
    # w.write(0, 4, u'差 个数')
    # # 写入数据
    # excel_row = 1
    # for i in danwei:
    #     u_btpr = i['u_btpr']
    #     u_leixing = i['u_leixing']
    #     count_a = str(i['count_a'])
    #     count_b = str(i['count_b'])
    #     count_c = str(i['count_c'])
    #     count_d = str(i['count_d'])
    #     # 写入每一行对应的数据
    #     w.write(excel_row, 0, u_btpr)
    #     w.write(excel_row, 1, count_a)
    #     w.write(excel_row, 2, count_b)
    #     w.write(excel_row, 3, count_c)
    #     w.write(excel_row, 4, count_d)
    #     excel_row += 1

    for i in btpr_r:
        excel_row = 1
        if i == 'danwei':
            w = ws.add_sheet(u"单位")
            # 写入表头
            w.write(0, 0, u'测评单位')
            w.write(0, 1, u'好(个数)')
            w.write(0, 2, u'较好(个数)')
            w.write(0, 3, u'一般(个数)')
            w.write(0, 4, u'差(个数)')
            # 写入数据
            for m in danwei:
                u_btpr = m['u_btpr']
                u_leixing = m['u_leixing']
                count_a = str(m['count_a'])
                count_b = str(m['count_b'])
                count_c = str(m['count_c'])
                count_d = str(m['count_d'])
                # 写入每一行对应的数据
                w.write(excel_row, 0, u_btpr)
                w.write(excel_row, 1, count_a)
                w.write(excel_row, 2, count_b)
                w.write(excel_row, 3, count_c)
                w.write(excel_row, 4, count_d)
                excel_row += 1
        elif i == 'zkjsz':
            w = ws.add_sheet(u"正科级实职")
            # 写入表头
            w.write(0, 0, u'姓名')
            w.write(0, 1, u'优秀(个数)')
            w.write(0, 2, u'称职(个数)')
            w.write(0, 3, u'基本称职(个数)')
            w.write(0, 4, u'不称职(个数)')
            # 写入数据
            for m in zkjsz:
                u_btpr = m['u_btpr']
                u_leixing = m['u_leixing']
                count_a = str(m['count_a'])
                count_b = str(m['count_b'])
                count_c = str(m['count_c'])
                count_d = str(m['count_d'])
                # 写入每一行对应的数据
                w.write(excel_row, 0, u_btpr)
                w.write(excel_row, 1, count_a)
                w.write(excel_row, 2, count_b)
                w.write(excel_row, 3, count_c)
                w.write(excel_row, 4, count_d)
                excel_row += 1
        elif i == 'fkjsz':
            w = ws.add_sheet(u"副科级实职")
            # 写入表头
            w.write(0, 0, u'姓名')
            w.write(0, 1, u'优秀(个数)')
            w.write(0, 2, u'称职(个数)')
            w.write(0, 3, u'基本称职(个数)')
            w.write(0, 4, u'不称职(个数)')
            # 写入数据
            for m in fkjsz:
                u_btpr = m['u_btpr']
                u_leixing = m['u_leixing']
                count_a = str(m['count_a'])
                count_b = str(m['count_b'])
                count_c = str(m['count_c'])
                count_d = str(m['count_d'])
                # 写入每一行对应的数据
                w.write(excel_row, 0, u_btpr)
                w.write(excel_row, 1, count_a)
                w.write(excel_row, 2, count_b)
                w.write(excel_row, 3, count_c)
                w.write(excel_row, 4, count_d)
                excel_row += 1
        elif i == 'sjgjjz':
            w = ws.add_sheet(u"四级高级警长")
            # 写入表头
            w.write(0, 0, u'姓名')
            w.write(0, 1, u'优秀(个数)')
            w.write(0, 2, u'称职(个数)')
            w.write(0, 3, u'基本称职(个数)')
            w.write(0, 4, u'不称职(个数)')
            # 写入数据
            for m in sjgjjz:
                u_btpr = m['u_btpr']
                u_leixing = m['u_leixing']
                count_a = str(m['count_a'])
                count_b = str(m['count_b'])
                count_c = str(m['count_c'])
                count_d = str(m['count_d'])
                # 写入每一行对应的数据
                w.write(excel_row, 0, u_btpr)
                w.write(excel_row, 1, count_a)
                w.write(excel_row, 2, count_b)
                w.write(excel_row, 3, count_c)
                w.write(excel_row, 4, count_d)
                excel_row += 1
        elif i == 'yejjz':
            w = ws.add_sheet(u"一二级警长")
            # 写入表头
            w.write(0, 0, u'姓名')
            w.write(0, 1, u'优秀(个数)')
            w.write(0, 2, u'称职(个数)')
            w.write(0, 3, u'基本称职(个数)')
            w.write(0, 4, u'不称职(个数)')
            # 写入数据
            for m in yejjz:
                u_btpr = m['u_btpr']
                u_leixing = m['u_leixing']
                count_a = str(m['count_a'])
                count_b = str(m['count_b'])
                count_c = str(m['count_c'])
                count_d = str(m['count_d'])
                # 写入每一行对应的数据
                w.write(excel_row, 0, u_btpr)
                w.write(excel_row, 1, count_a)
                w.write(excel_row, 2, count_b)
                w.write(excel_row, 3, count_c)
                w.write(excel_row, 4, count_d)
                excel_row += 1
        elif i == 'ssjjz':
            w = ws.add_sheet(u"三四级警长")
            # 写入表头
            w.write(0, 0, u'姓名')
            w.write(0, 1, u'优秀(个数)')
            w.write(0, 2, u'称职(个数)')
            w.write(0, 3, u'基本称职(个数)')
            w.write(0, 4, u'不称职(个数)')
            # 写入数据
            for m in ssjjz:
                u_btpr = m['u_btpr']
                u_leixing = m['u_leixing']
                count_a = str(m['count_a'])
                count_b = str(m['count_b'])
                count_c = str(m['count_c'])
                count_d = str(m['count_d'])
                # 写入每一行对应的数据
                w.write(excel_row, 0, u_btpr)
                w.write(excel_row, 1, count_a)
                w.write(excel_row, 2, count_b)
                w.write(excel_row, 3, count_c)
                w.write(excel_row, 4, count_d)
                excel_row += 1
        elif i == 'yejjy':
            w = ws.add_sheet(u"一二级警员")
            # 写入表头
            w.write(0, 0, u'姓名')
            w.write(0, 1, u'优秀(个数)')
            w.write(0, 2, u'称职(个数)')
            w.write(0, 3, u'基本称职(个数)')
            w.write(0, 4, u'不称职(个数)')
            # 写入数据
            for m in yejjy:
                u_btpr = m['u_btpr']
                u_leixing = m['u_leixing']
                count_a = str(m['count_a'])
                count_b = str(m['count_b'])
                count_c = str(m['count_c'])
                count_d = str(m['count_d'])
                # 写入每一行对应的数据
                w.write(excel_row, 0, u_btpr)
                w.write(excel_row, 1, count_a)
                w.write(excel_row, 2, count_b)
                w.write(excel_row, 3, count_c)
                w.write(excel_row, 4, count_d)
                excel_row += 1
        elif i == 'jggq':
            w = ws.add_sheet(u"机关工勤")
            # 写入表头
            w.write(0, 0, u'姓名')
            w.write(0, 1, u'优秀(个数)')
            w.write(0, 2, u'合格(个数)')
            w.write(0, 3, u'基本合格(个数)')
            w.write(0, 4, u'不合格(个数)')
            # 写入数据
            for m in jggq:
                u_btpr = m['u_btpr']
                u_leixing = m['u_leixing']
                count_a = str(m['count_a'])
                count_b = str(m['count_b'])
                count_c = str(m['count_c'])
                count_d = str(m['count_d'])
                # 写入每一行对应的数据
                w.write(excel_row, 0, u_btpr)
                w.write(excel_row, 1, count_a)
                w.write(excel_row, 2, count_b)
                w.write(excel_row, 3, count_c)
                w.write(excel_row, 4, count_d)
                excel_row += 1
        elif i == 'sjb':
            w = ws.add_sheet(u"事业编")
            # 写入表头
            w.write(0, 0, u'姓名')
            w.write(0, 1, u'优秀(个数)')
            w.write(0, 2, u'合格(个数)')
            w.write(0, 3, u'基本合格(个数)')
            w.write(0, 4, u'不合格(个数)')
            # 写入数据
            for m in sjb:
                u_btpr = m['u_btpr']
                u_leixing = m['u_leixing']
                count_a = str(m['count_a'])
                count_b = str(m['count_b'])
                count_c = str(m['count_c'])
                count_d = str(m['count_d'])
                # 写入每一行对应的数据
                w.write(excel_row, 0, u_btpr)
                w.write(excel_row, 1, count_a)
                w.write(excel_row, 2, count_b)
                w.write(excel_row, 3, count_c)
                w.write(excel_row, 4, count_d)
                excel_row += 1
    # 实现下载
    output = BytesIO()
    ws.save(output)
    output.seek(0)
    response = StreamingHttpResponse(output)
    response['content_type'] = 'application/vnd.ms-excel'
    response['charset'] = 'utf-8'
    response['Content-Disposition'] = 'attachment; filename="result.xls"'
    return response

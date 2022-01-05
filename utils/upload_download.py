import datetime
from venv import logger

import xlrd
from django.db import transaction
from django.shortcuts import render
from xlrd import xldate_as_datetime
from zzc_admin import settings


# 将excel数据写入mysql
def wrdb(request):
    if request.method == 'POST':
        f = request.FILES.get('file')
        excel_type = f.name.split('.')[1]
        if excel_type in ['xlsx', 'xls']:
            # 开始解析上传的excel表格
            wb = xlrd.open_workbook(filename=None, file_contents=f.read())
            table = wb.sheets()[0]
            rows = table.nrows  # 总行数
            try:
                with transaction.atomic():  # 控制数据库事务交易
                    for i in range(1, rows):
                        rowVlaues = table.row_values(i)
                        print(rowVlaues)
                        # major = models.TMajor.objects.filter(majorid=rowVlaues[1]).first()
                        # models.TGrade.objects.create(gradeid=rowVlaues[0], major=major, gradename=rowVlaues[2],
                        #                              memo=rowVlaues[3])
            except:
                logger.error('解析excel文件或者数据插入错误')
            return render(request, 'bg/success.html', {'message': '导入成功'})
        else:
            logger.error('上传文件类型错误！')
            return render(request, 'bg/failed.html', {'message': '导入失败'})
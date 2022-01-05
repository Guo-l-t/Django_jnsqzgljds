import pymysql
from backend import models


def getCount(date):
    # username = date[0]
    # pwd = date[1]
    # u = models.user.objects.all()
    count_youxiu = models.count_youxiu.objects.filter(leixing=date[0])
    if len(count_youxiu) == 0:
        return '无人员信息'
    else:
        return count_youxiu



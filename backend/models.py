from django.db import models


class User(models.Model):
    username = models.CharField(primary_key=True, max_length=255)
    zhanghao = models.CharField(max_length=255)
    password = models.CharField(max_length=100)
    user_level = models.CharField(max_length=100)  # 0普通用户、1超级用户
    danwei = models.CharField(max_length=255)  # 单位是否投票标识  0未投票、1已投票
    zkjsz = models.CharField(max_length=255)  # 正科级实职
    fkjsz = models.CharField(max_length=255)  # 副科级实职
    sjgjjz = models.CharField(max_length=255)  # 四级高级警长
    yejjz = models.CharField(max_length=255)  # 一二级警长
    ssjjz = models.CharField(max_length=255)  # 三四级警长
    yejjy = models.CharField(max_length=255)  # 一二级警员
    jggq = models.CharField(max_length=255)  # 机关工勤
    sjb = models.CharField(max_length=255)  # 事业编
    f1 = models.CharField(max_length=255)
    f2 = models.CharField(max_length=255)
    f3 = models.CharField(max_length=255)
    f4 = models.CharField(max_length=255)
    f5 = models.CharField(max_length=255)
    #  python manage.py makemigrations
    #  python manage.py migrate


class Btpr(models.Model):
    xuhao = models.CharField(max_length=10)
    xingming = models.CharField(max_length=100)
    # danwei 单位
    # zjjsz 正科级实职 fkjsz 副科级实职 yjjz 一级警长 ejjz 二级警长 sanjjz 三级警长
    # sijjz 四级警长 yjjyjyx 一级警员及以下 jggq 机关工勤 sybgzry 事业编工作人员
    leixing = models.CharField(max_length=255)
    f1 = models.CharField(max_length=255)
    f2 = models.CharField(max_length=255)
    f3 = models.CharField(max_length=255)
    f4 = models.CharField(max_length=255)
    f5 = models.CharField(max_length=255)


class count_youxiu(models.Model):
    xuhao = models.CharField(max_length=10)
    leixing = models.CharField(max_length=100)
    # danwei 单位
    # zjjsz 正科级实职 fkjsz 副科级实职 yjjz 一级警长 ejjz 二级警长 sanjjz 三级警长
    # sijjz 四级警长 yjjyjyx 一级警员及以下 jggq 机关工勤 sybgzry 事业编工作人员
    count_youxiu = models.CharField(max_length=255)
    f1 = models.CharField(max_length=255)
    f2 = models.CharField(max_length=255)
    f3 = models.CharField(max_length=255)
    f4 = models.CharField(max_length=255)
    f5 = models.CharField(max_length=255)


class Vote_session(models.Model):
    voter = models.CharField(max_length=255)  # 投票者
    voting_object = models.CharField(max_length=100)  # 被投票人
    voting_results = models.CharField(max_length=100)  # 投票结果
    voting_object_type = models.CharField(max_length=100)  # 被投票人类型
    voting_time = models.CharField(max_length=100)  # 投票时间
    voting_update_time = models.CharField(max_length=100)  # 最终投票时间
    f1 = models.CharField(max_length=255)  # 记录投票人对被投票人次数及信息
    f2 = models.CharField(max_length=255)  # 投票时间
    f3 = models.CharField(max_length=255)  # 投票时间
    f4 = models.CharField(max_length=255)  # 投票时间
    f5 = models.CharField(max_length=255)  # 投票时间

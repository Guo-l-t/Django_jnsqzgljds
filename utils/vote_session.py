import pymysql
from backend import models


def get_vote_session(date):
    # username = date[0]
    # pwd = date[1]
    # u = models.user.objects.all()
    u = models.Vote_session.objects.filter(voting_object=date[0])
    if len(u) == 0:
        return '无人员信息'
    else:
        return u



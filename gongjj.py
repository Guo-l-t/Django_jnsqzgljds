import os
import xlrd
import pymysql


def insert_3_gongzi(name):
    s = cursor.execute("SELECT * FROM sheet_3_gongzi  WHERE `姓名`=%s", name)
    selectResultList = cursor.fetchall()
    if s == 1:
        xingming = name
        # 工资级别
        gzjb = '0'
        # 档次
        dc = '0'
        # 职务岗位工资
        zwgwgz = selectResultList[0]['职务岗位工资']
        # 级别工资
        jbgz = selectResultList[0]['级别工资']
        # 合计
        heji = ''
        # 年度合计
        nianduheji = ''
        # 工作性津贴
        gzxjt = selectResultList[0]['工作性津贴']
        # 生活性补贴
        shxbt = selectResultList[0]['生活性补贴']
        # 年度合计
        nianduheji1 = ''
        # 警衔津贴
        jxjt = selectResultList[0]['警衔津贴']
        # 合计1
        heji1 = ''
        # 年度合计
        nianduheji2 = ''
        # 车补
        chebu = ''
        # 住房补贴
        zfbt = selectResultList[0]['住房补贴']
        # 改革性补贴
        ggxbt = selectResultList[0]['改革性补贴']
        # 防暑采暖费
        fscnf = selectResultList[0]['防暑采暖费']
        # 合计
        heji2 = ""
        # 年度合计
        nianduheji3 = ""
        # 奖励性补贴文明奖
        jlxbtwmj = ""
        # 奖励性补贴考核奖
        jlxbtkhj = ""
        # 合计
        heji3 = ''
        # 年终一次性奖金
        nzycxjj = ""
        zqbt_jbbt = get_zqjt_jbbt(name)

        zhiqinbutie = zqbt_jbbt[0]
        jiabanbutie = zqbt_jbbt[1]
        sql = """INSERT INTO sheet_mubiao_gongzi(`姓名`, `工资级别`, `档次`, `职务岗位工资`, `级别工资`, `合计`, `年度合计`, `工作性津贴`,`生活性补贴`, `年度合计1` , `警衔津贴`, `执勤津贴`,`加班补贴`,`合计1`, `年度合计2`, `车补`, `住房补贴`, `改革性补贴`, `防暑采暖费`, `合计2`, `年度合计3`, `f20`,`奖励性补贴文明奖`, `奖励性补贴考核奖`, `合计3`, `f24`, `年终一次性奖金`, `f26`) 
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
        # VALUES ("%s","%s",`%s`,`%s`,`%s`,`%s`,`%s`,`%s`,`%s`,`%s`,`%s`,`%s`,`%s`,`%s`,`%s`,`%s`,`%s`,`%s`,`%s`,`%s`,`%s`,`%s`,`%s`,`%s`,`%s`,`%s`)"""
        value = (xingming, gzjb, dc, zwgwgz, str(jbgz), heji, nianduheji, str(gzxjt), str(shxbt), nianduheji1, zhiqinbutie, jiabanbutie, str(jxjt), heji1, nianduheji2, chebu, str(zfbt), str(ggxbt), str(fscnf), heji2, nianduheji3, "", jlxbtwmj, jlxbtkhj, heji3, "", nzycxjj, "3月工资")
        cursor.execute(sql, value)
    else:
        print("3月工资表中不存在"+name)


def get_zqjt_jbbt(name):
    s = cursor.execute("SELECT * FROM sheet_zqjt_jbbt  WHERE `姓名`=%s", name)
    selectResultList = cursor.fetchall()
    r = []
    if s == 1:
        zqjt = selectResultList[0]['执勤津贴']
        r.append(zqjt)
        jbbt = selectResultList[0]['加班补贴']
        r.append(jbbt)
        return r
    else:
        print(name + '无执勤津贴和加班补贴')
        return [0, 0]


def insert_11_gongzi(name):
    s = cursor.execute("SELECT * FROM sheet_11_gongzi  WHERE `姓名`=%s", name)
    selectResultList = cursor.fetchall()
    if s == 1:
        xingming = name
        # 工资级别
        gzjb = '0'
        # 档次
        dc = '0'
        # 职务岗位工资
        zwgwgz = selectResultList[0]['职务岗位工资']
        # 级别工资
        jbgz = selectResultList[0]['级别工资']
        # 合计
        heji = ''
        # 年度合计
        nianduheji = ''
        # 工作性津贴
        gzxjt = selectResultList[0]['工作性津贴']
        # 生活性补贴
        shxbt = selectResultList[0]['生活性补贴']
        # 年度合计
        nianduheji1 = ''
        # 警衔津贴
        jxjt = selectResultList[0]['警衔津贴']
        # 合计1
        heji1 = ''
        # 年度合计
        nianduheji2 = ''
        # 车补
        chebu = ''
        # 住房补贴
        zfbt = selectResultList[0]['住房补贴']
        # 改革性补贴
        ggxbt = selectResultList[0]['改革性补贴']
        # 防暑采暖费
        fscnf = selectResultList[0]['防暑采暖费']
        # 合计
        heji2 = ""
        # 年度合计
        nianduheji3 = ""
        # 奖励性补贴文明奖
        jlxbtwmj = ""
        # 奖励性补贴考核奖
        jlxbtkhj = ""
        # 合计
        heji3 = ''
        # 年终一次性奖金
        nzycxjj = ""
        zqbt_jbbt = get_zqjt_jbbt(name)
        zhiqinbutie = zqbt_jbbt[0]
        jiabanbutie = zqbt_jbbt[1]
        sql = """INSERT INTO sheet_mubiao_gongzi(`姓名`, `工资级别`, `档次`, `职务岗位工资`, `级别工资`, `合计`, `年度合计`, `工作性津贴`,`生活性补贴`, `年度合计1` , `警衔津贴`, `执勤津贴`,`加班补贴`,`合计1`, `年度合计2`, `车补`, `住房补贴`, `改革性补贴`, `防暑采暖费`, `合计2`, `年度合计3`, `f20`,`奖励性补贴文明奖`, `奖励性补贴考核奖`, `合计3`, `f24`, `年终一次性奖金`, `f26`) 
                VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
        # VALUES ("%s","%s",`%s`,`%s`,`%s`,`%s`,`%s`,`%s`,`%s`,`%s`,`%s`,`%s`,`%s`,`%s`,`%s`,`%s`,`%s`,`%s`,`%s`,`%s`,`%s`,`%s`,`%s`,`%s`,`%s`,`%s`)"""
        value = (xingming, gzjb, dc, zwgwgz, str(jbgz), heji, nianduheji, str(gzxjt), str(shxbt), nianduheji1,
                 zhiqinbutie, jiabanbutie, str(jxjt), heji1, nianduheji2, chebu, str(zfbt), str(ggxbt), str(fscnf),
                 heji2, nianduheji3, "", jlxbtwmj, jlxbtkhj, heji3, "", nzycxjj, "11月工资")
        cursor.execute(sql, value)
        # sql = """INSERT INTO sheet_mubiao_gongzi(`姓名`, `工资级别`, `档次`, `职务岗位工资`, `级别工资`, `合计`, `年度合计`, `工作性津贴`,`生活性补贴`, `年度合计1` , `警衔津贴`, `合计1`, `年度合计2`, `车补`, `住房补贴`, `改革性补贴`, `防暑采暖费`, `合计2`, `年度合计3`, `f20`,`奖励性补贴文明奖`, `奖励性补贴考核奖`, `合计3`, `f24`, `年终一次性奖金`, `f26`)
        #     VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
        # # VALUES ("%s","%s",`%s`,`%s`,`%s`,`%s`,`%s`,`%s`,`%s`,`%s`,`%s`,`%s`,`%s`,`%s`,`%s`,`%s`,`%s`,`%s`,`%s`,`%s`,`%s`,`%s`,`%s`,`%s`,`%s`,`%s`)"""
        # value = (
        # xingming, gzjb, dc, zwgwgz, str(jbgz), heji, nianduheji, str(gzxjt), str(shxbt), nianduheji1, str(jxjt), heji1,
        # nianduheji2, chebu, str(zfbt), str(ggxbt), str(fscnf), heji2, nianduheji3, "", jlxbtwmj, jlxbtkhj, heji3, "",
        # nzycxjj, "11月工资")
        # cursor.execute(sql, value)
    else:
        print("11月工资表中不存在" + name)


# 奖励性补贴考核奖
def get_jlxbtkhj(name):
    s = cursor.execute("SELECT `奖励性补贴考核奖` FROM sheet_jlxbtkhj WHERE `姓名`=%s ", name)
    selectResultList = cursor.fetchall()
    if len(selectResultList) == 0:
        print(name+' 无奖励性补贴考核奖')
        return 0
    else:
        for i in range(len(selectResultList)):
            jlxbtkhj = selectResultList[i]['奖励性补贴考核奖']
            return jlxbtkhj


# 奖励性补贴文明奖
def get_jlxbtwmj(name):
    s = cursor.execute("SELECT `奖励性补贴文明奖` FROM sheet_jlxbtwmj WHERE `姓名`=%s ", name)
    selectResultList = cursor.fetchall()
    if len(selectResultList) == 0:
        print(name + ' 无奖励性补贴wwwww文明奖')
        return 0
    else:
        for i in range(len(selectResultList)):
            jlxbtkhj = selectResultList[i]['奖励性补贴文明奖']
            return jlxbtkhj


# 年终一次性奖金
def get_nzycxjj(name):
    s = cursor.execute("SELECT `年终一次性奖金` FROM sheet_nzycxjj WHERE `姓名`=%s ", name)
    selectResultList = cursor.fetchall()
    if len(selectResultList) == 0:
        print(name + ' 无年终一次性奖金')
        return 0
    else:
        for i in range(len(selectResultList)):
            jlxbtkhj = selectResultList[i]['年终一次性奖金']
            return jlxbtkhj


def update_messages(name):
    # 先查 name+3月 是否有此人，有就插入3月份的，没有就插入11月份的
    s = cursor.execute("SELECT * FROM sheet_mubiao_gongzi WHERE `姓名`=%s and `f26`=%s", (name, '3月工资'))
    jlxbtkhj = get_jlxbtkhj(name)
    jlxbtwmj = get_jlxbtwmj(name)
    nzycxjj = get_nzycxjj(name)
    # if s == 1:
    #     sql = "UPDATE sheet_mubiao_gongzi SET `奖励性补贴考核奖` = %s, `奖励性补贴文明奖` = %s, `年终一次性奖金` = %s " \
    #           "WHERE `姓名` = %s and `f26` = %s"
    #     val = (jlxbtkhj, jlxbtwmj, nzycxjj, name, '3月工资')
    #     cursor.execute(sql, val)
    #
    # else:
        # print('三月工资表中不存在'+name)
    sql = "UPDATE sheet_mubiao_gongzi SET `奖励性补贴考核奖` = %s, `奖励性补贴文明奖` = %s, `年终一次性奖金` = %s " \
          "WHERE `姓名` = %s and `f26` = %s"
    val = (jlxbtkhj, jlxbtwmj, nzycxjj, name, '11月工资')
    cursor.execute(sql, val)


def get_sy_gzjb_dc(name):
    s = cursor.execute("SELECT * FROM sheet_sy_gzjb_dc WHERE `姓名`=%s ", name)
    selectResultList = cursor.fetchall()
    if len(selectResultList) == 0:
        print(name + ' 无3月工资级别与档次')
        return 0
    else:
        for i in range(len(selectResultList)):
            r = []
            gzjb = selectResultList[i]['工资级别']
            r.append(gzjb)
            dc = selectResultList[i]['档次']
            r.append(dc)
            return r


def update_gjj_sj1(name, state):
    s = cursor.execute("SELECT * FROM sheet_shuju1 WHERE `姓名`=%s", name)
    selectResultList = cursor.fetchall()
    if len(selectResultList) == 0:
        print('数据1里不存在   '+name+'   数据')
    else:
        for i in range(len(selectResultList)):
            gjj_sj1 = selectResultList[i]['数据1']
            if state == '是':
                sql = "UPDATE sheet_mubiao SET `数据1` = %s" \
                      "WHERE `姓名` = %s and `本年末是否在职` = %s"
                val = (gjj_sj1, name, state)
                cursor.execute(sql, val)


def update_gjj_sj2(name, state):
    s = cursor.execute("SELECT * FROM sheet_shuju2 WHERE `姓名`=%s", name)
    selectResultList = cursor.fetchall()
    if len(selectResultList) == 0:
        print('数据2里不存在   '+name+'   数据')
    else:
        for i in range(len(selectResultList)):
            gjj_sj2 = selectResultList[i]['数据1']
            if state == '是':
                sql = "UPDATE sheet_mubiao SET `数据2` = %s" \
                      "WHERE `姓名` = %s and `本年末是否在职` = %s"
                val = (gjj_sj2, name, state)
                cursor.execute(sql, val)


def getNames():
    s = cursor.execute("SELECT * FROM sheet_mubiao  ")
    selectResultList = cursor.fetchall()
    for i in range(len(selectResultList)):
        name = selectResultList[i]['姓名']
        state = selectResultList[i]['本年末是否在职']
        # 查询3月工资信息插入
        # insert_3_gongzi(name)
        # 查询11月工资信息插入
        # insert_11_gongzi(name)
        # update_messages(name)
        update_gjj_sj1(name, state)
        update_gjj_sj2(name, state)


if __name__ == '__main__':
    # 1.获取连接对象
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='*3tttfv>b0U', db='zzc', charset='utf8')
    # 2.获取游标，来进行查询,这样默认查询的都为tuple列表
    # cursor = conn.cursor()
    cursor = conn.cursor(pymysql.cursors.DictCursor)  # 这样查询的为字典
    # 循环name表
    getNames()
    # 提交
    conn.commit()
    # 关闭游标
    cursor.close()
    # 关闭连接
    conn.close()
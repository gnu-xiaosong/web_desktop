from django.db import models

#用户模型
class User(models.Model):

    # 用户名
    username = models.CharField(max_length=255)

    # 密码
    passwd = models.CharField(max_length=255)

    # 状态
    status = models.IntegerField(max_length=1)

    # token
    token = models.CharField(max_length=255)

    # uuid唯一值
    uuid = models.CharField(max_length=255)

    # 创建时间
    time = models.DateTimeField()



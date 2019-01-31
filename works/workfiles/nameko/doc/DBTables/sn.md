## 网关管理数据表信息
- 数据表: auth_gateways
- 字段说明(含义|格式|特性|备注)

| 字段 | 含义 | 格式 | 特性 | 备注 |
| ---- | ---- | ---- | ---- | ---- |
| sn | 网关号 | string | 不可为空且唯一 | -- |
| uid | 所属用户id | string | -- | 对应数据库cas/passport的用户表 |
| project | 所属项目id | string | -- | 对应main_vsnproject的项目表 |
| sim | sim卡号 | string | -- | -- |
| pwd | 网关密码 | string | 不可为空 | -- |
| name | 网关别名 | string | -- | name是在将网关添加到项目时候产生的 |
| last_update | 网关最后更新时间 | Date | -- | 网关最后的更新时间, 涉及到具体硬件设备上传数据部分 |

## 备注
- 解除绑定时,应清空project, uid, name
- 网关属于具体的一个项目和此项目的创建者, 所以如果项目进行移交(即项目A的owner改变了,则网关表中project=A的网关,uid也要随之改变)

## 参考
```
{
    "_id" : ObjectId("574e8c1ba1d09b083e0b46b7"),
    "pwd" : "txpM1tIg",
    "sn" : "GAB331154111062",
    "sim" : "18612446100",
    "last_update" : ISODate("2018-05-22T17:00:31.000Z"),
    "name" : "新江海河-62",
    "uid" : "584a43c3c2de7d000680e0c3",
    "project" : "ntxjhhdq"
}
```

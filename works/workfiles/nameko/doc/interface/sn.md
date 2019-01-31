## 网关管理接口信息
- 网关管理
```
url: /admin/sn
params: {
  
}
return: {
  data: 网关数组
}
```
- 添加网关
```
url: /admin/addsn
params: {
  sn: 网关号，不可为空且唯一
  sim: sim卡号， 可为空
}
return: {
  status: 结果状态
  msg: 结果内容  
}
```
- 删除网关
```
url: /admin/delsn
params: {
  _id: 唯一标识，_id不可为空且唯一
}
return: {
  status: 结果状态
  msg: 结果内容  
}
```
- 批量删除网关
```
url: /admin/batchdelsn
params: {
  _ids: _id 列表，_ids不可为空
}
return: {
  status: 结果状态
  msg: 结果内容  
}
```
- 编辑网关
```
url: /admin/editsn
params: {
  _id: 唯一标识，_id不可为空且唯一
  sim: sim卡号， 可为空
}
return: {
  status: 结果状态
  msg: 结果内容  
}
```
- 获取网关密码
```
url: /admin/getsnpwd
params: {
  _id: 唯一标识，_id不可为空且唯一
}
return: {
  pwd: pwd
}
```
- 解绑定网关
```
url: /admin/dissolvesn
params: {
  _id: 唯一标识，_id不可为空且唯一
}
return: {
  status: 结果状态
  msg: 结果内容  
}
```
- 批量解绑定网关
```
url: /admin/batchdissolvesn
params: {
  _ids: _id 列表，_ids不可为空
}
return: {
  status: 结果状态
  msg: 结果内容  
}
```
- 获取网关用户
```
url: /admin/snuser
params: {
  sn: 网关号，不可为空且唯一
}
return: {
  user: user
}
```
- 添加网关用户
```
url: /admin/addsnuser
params: {
  sn: 网关号，不可为空且唯一
  uid: 用户id
}
return: {
  status: 结果状态
  msg: 结果内容  
}
```
- 删除网关用户
```
url: /admin/delsnuser
params: {
  uid: 用户id
  sn: 网关号，不可为空
}
return: {
  status: 结果状态
  msg: 结果内容  
}
```
- 批量删除网关用户
```
url: /admin/batchdelsnuser
params: {
  uid: 用户id
  sns: 网关号列表，不可为空
}
return: {
  status: 结果状态
  msg: 结果内容  
}
```
- 导入网关
```
url: /admin/importsn
params: {

}
return: {
  status: True
	exceptions: exceptions
	data: data
}
```
- 导出网关
```
url: /admin/exportsn
params: {
  
}
return: {
   
}
```
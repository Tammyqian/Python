## 无效数据表(data_error)
- 所在数据库: error_ + 项目代号

## 字典
| 字段 | 含义 | 类型 | 备注 |
| ---- | ---- | ---- | ---- |
| sensor_type | 传感类型 | string | - |
| node_id | 测点 | string | - |
| channel | 通道 | string | 通常为数字字符串, 也可能为x, y, z |
| gateway_id | 网关 | string | - |
| dtime | 时间 | ISODate | - |
| ts | 时间戳 | float | - |
| error | 错误信息 | string | - |

## 备注
- 由于无效数据根据项目代号存储, 所以查询情况下必须带code_name
- 数据量过大, 如果有必要, 得一页一页返回数据.
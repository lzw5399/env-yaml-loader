# env yaml loader

使用环境变量的值替换yaml原本的内容，用于配置文件的替换

## 调用方式
```shell
python env2yaml.py [xxx.yaml] [env-prefix]
```

## 调用示例
```shell
python env2yaml.py appsettings.yaml app
```

## 示例规则

### yaml
```yaml
num: 123
str: 测试
main:
    sub: true
arr:
    - 123
    - 456
```

### 假设`env-prefix = app`, 对应的环境变量值
```
app_num
app_str
app_main__sub
app_arr0
app_arr1
```

### 如果不传env-prefix对应的环境变量值
```
num
str
main__sub
arr0
arr1
```
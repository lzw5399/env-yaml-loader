#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# -*- author: lzw5399 -*-
import os
import sys

import yaml

PREFIX = "app"
if len(sys.argv) > 1:
    PREFIX = sys.argv[1]

main_dir = os.path.split(os.path.realpath(__file__))[0]
yaml_path = os.path.join(main_dir, "appsettings.yaml")

# 添加环境变量用以测试
os.environ["app_prop"] = "yttewqwwwwwwwwer"
os.environ["app_first__subv"] = "sha_ya_dssni"
os.environ["app_first__sub_tree__third"] = "ffffffffffffff"
os.environ["main__sub__third"] = "True"
os.environ["hobby[0]"] = "True"


def gen_env_key(current, dependencies):
    if dependencies is None:
        dependencies = []

    if '__'.join(dependencies) == '':
        return '{}_{}'.format(PREFIX, current).lstrip('_')
    else:
        return '{}_{}__{}'.format(PREFIX, '__'.join(dependencies), current).lstrip('_')


scalar_list = [str, bool, int, float, None]


def is_scalar(t):
    return t in scalar_list


# load setting from env recursively
def load_env_to_content(content, level=0, dependencies=None):
    for key in content.keys():
        if level == 0 or dependencies is None:
            dependencies = []

        env_key = gen_env_key(key, dependencies)
        if type(content[key]) in scalar_list and os.getenv(env_key) is not None:
            content[key] = os.getenv(env_key)
            print("yes str")

        # 对象
        elif type(content[key]) == dict:
            dependencies.append(key)
            load_env_to_content(content[key], level=level + 1, dependencies=dependencies)
            print("yes dict")

        # 基本类型数组
        elif type(content[key]) == list and content[key][0] in scalar_list:
            for i, v in enumerate(content[key]):
                print(i, v)
            print("yes list")

        # 对象数组
        elif type(content[key]) == list and type(content[key][0]) == dict:
            print("yes list")

        print(key, type(content[key]), content[key])


def resort(content, exist_keys):
    nc = {}
    for key in exist_keys:
        if key in content.keys():
            nc[key] = content[key]
    return nc


def convert_settings():
    with open(yaml_path, "r", encoding="utf-8") as f:
        content = yaml.safe_load(f)

    exist_keys = content.keys()
    load_env_to_content(content)
    content = resort(content, exist_keys)

    with open(yaml_path, "w", encoding="utf-8") as f:
        yaml.dump(content, f, allow_unicode=True)


if __name__ == '__main__':
    convert_settings()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import sys

import yaml

PREFIX = "app"
if len(sys.argv) > 1:
    PREFIX = sys.argv[1]

main_dir = os.path.split(os.path.realpath(__file__))[0]
yaml_path = os.path.join(main_dir, "appsettings.yaml")

# 添加环境变量用以测试
os.environ["name"] = "yttewqwwwwwwwwer"
os.environ["main__sha"] = "sha_ya_ni"
os.environ["main__sub__third"] = "True"
os.environ["hobby[0]"] = "True"


def gen_env_key(current, dependencies):
    if dependencies is None:
        dependencies = [current]
    else:
        dependencies.append(current)
    return '{}_{}'.format(PREFIX, '__'.join(dependencies)).lstrip('_')


scalar_list = [str, bool, int, float, None]


def is_scalar(t):
    return t in scalar_list


# load setting from env recursively
def load_env_to_content(content, level=0, dependencies=None):
    if dependencies is None:
        dependencies = [PREFIX]

    for key in content.keys():
        if type(content[key]) in scalar_list and os.getenv(key) is not None:
            content[key] = os.getenv(key)
            print("yes str")

        elif type(content[key]) == list:
            print("yes list")
        elif type(content[key]) == dict:
            print("yes dict")
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

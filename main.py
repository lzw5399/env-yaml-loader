#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

import yaml

main_dir = os.path.split(os.path.realpath(__file__))[0]
yaml_path = os.path.join(main_dir, "appsettings.yaml")


def convert_settings():
    with open(yaml_path, "r", encoding="utf-8") as f:
        content = yaml.safe_load(f)

    content["name"] = "中文"

    with open(yaml_path, "w", encoding="utf-8") as f:
        yaml.dump(content, f, allow_unicode=True)


if __name__ == '__main__':
    convert_settings()


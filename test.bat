@echo off

set app_num=modified
set app_str=modified
set app_main__sub=yet also modified
set app_main__sub20=yet also modified
set app_main__sub21=yet also modified
set app_arr0=True
set app_arr1=emmmmmm

set num=noprefix_num
set str=noprefix_str
set main__sub=noprefix_main_ddd
set main__sub20=ew
set main__sub21=78390989
set arr0=arr111
set arr1=arr222

python env2yaml.py appsettings.yaml
echo "convert done"
pause
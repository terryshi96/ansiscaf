# ansi

##Install
```
pip install ansi
```

##Usage
```
1 ansi -new [project name]
create file tree
project_name
    -->group_vars(dir)
        --> all
    -->host_vars
    -->hosts (file)
    -->site.yml(file)
    -->roles
        -->common
            -->tasks
                -->main.yml
            -->files
            -->templates
            -->handlers
            -->vars


2 ansi -add [role name]
 create role dir tree

3 ansi -rm [dir name]
delete all empty dir

4 ansi -h
help
```
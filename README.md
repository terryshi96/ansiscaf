# ansi

##Install
```
pip install ansi
```

##Usage
```
1 ansit -new [project name]
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


2 ansit -add [role name]
 create role dir tree

3 ansit -rm [dir name]
delete all empty dir

4 ansit -h
help
```
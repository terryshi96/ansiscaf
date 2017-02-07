# ansiscaf

##Install
```
pip install ansiscaf
```

##Usage
```
1 ansiscaf -new [project name]
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


2 ansiscaf -add [role name]
 create role dir tree

3 ansiscaf -rm [dir name]
delete all empty dir

4 ansiscaf -h
help
```
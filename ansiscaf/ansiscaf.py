import os
import sys
import argparse

_version_ = '0.0.1'

class scaffold():

    result = []

    def new_project(self):
        if os.path.exists(self.result.project):
            print("project has been existed")
            exit(1)
        os.mkdir(self.result.project)
        os.chdir(self.result.project)
        os.system("touch hosts.yml")
        os.system("touch sites.yml")
        dir1 = ["group_vars", "host_vars", "roles"]
        for dir in dir1:
            os.mkdir(dir)
            if dir == "group_vars":
                os.system("touch group_vars/all")
        dir2 = ["tasks", "files", "templates", "handlers", "vars"]
        os.chdir("roles")
        for dir in dir2:
            os.mkdir(dir)
            if dir == "tasks":
                os.system("touch tasks/main.yml")
        print("create project %s successfully" % self.result.project)



    def new_role(self):
        if os.path.exists(self.result.role):
            print("dir has been existed")
            exit(1)
        os.mkdir(self.result.role)
        dirs = ["tasks", "files", "templates", "handlers", "vars"]
        os.chdir(self.result.role)
        for dir in dirs:
            os.mkdir(dir)
            if dir == "tasks":
                os.system("touch tasks/main.yml")
        print("create role %s successfully" % self.result.role)

    def find_dir(self,rootdir):
        for lists in os.listdir(rootdir):
            path = os.path.join(rootdir,lists)
            if os.path.isdir(path):
                if not os.listdir(path):
                    os.rmdir(path)
                else:
                    self.find_dir(path)


    def clean_dir(self):
        print("are you sure to clean?(y)")
        flag = input()
        if flag != "y":
            exit(1)
        self.find_dir(self.result.dir)


    def parse_opt(self):
        if len(sys.argv) > 3:
            print("error argv number,please check")
            exit(1)
        parser = argparse.ArgumentParser(usage="ansiscaf [opt] [argv]",description='ansible scaffold')
        parser.add_argument('-new', action="store", dest="project",help="create file tree")
        parser.add_argument('-add', action="store", dest="role",help="create role dir tree")
        parser.add_argument('-rm', action="store", dest="dir",help="delete all empty dir")
        self.result = parser.parse_args()
        if self.result.project:
            self.new_project()
        elif self.result.role:
            self.new_role()
        elif self.result.dir:
            self.clean_dir()


if __name__ == '__main__':
    ansi = scaffold()
    ansi.parse_opt()





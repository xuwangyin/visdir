#!/usr/bin/env python
import os
import sys

class TreeNode:
    def __init__(self, name, level, children=None):
        self.name = name
        self.level = level
        self.children = children
    def __str__(self):
        space = '    '
        newline = '\n'
        comma = ','
        # has children
        if self.children:
            json = space * self.level + '{' + newline + \
                space * self.level + '"name": ' + '"' \
                + self.name + '"' + comma + newline + \
                space * self.level + '"children":[' + newline
            for childIdx, child in enumerate(self.children):
                if childIdx == len(self.children) - 1:
                    # if this is the last child, discard the comma
                    json += space * self.level + str(child) + newline
                else:
                    json += space * self.level + str(child) + comma + newline
            json += space * self.level + ' ' + ']' + newline + \
                space * self.level + '}'

        # has no children
        else:
            json = space * self.level + '{' + '"name": ' + '"' + self.name + '"' + '}'
        return json
        
        

def parseDirTree(path, level):

    find = path.rfind('/')
    # path of this kind: "path/to/example/"
    if find == len(path) - 1:
        dirname = path[: -1]
    # path of this kind: "path/to/example"
    else:
        dirname = path[path.rfind('/') + 1 : ]

    # if this is a file
    if not os.path.isdir(path):
        return TreeNode(dirname, level)
    else:
        subdirs = os.listdir(path)
        # if this is an empty path
        if len(subdirs) is 0:
            return TreeNode(dirname, level)
        # otherwise this is a path with subdirs or files
        else:
            children = []
            for subdir in subdirs:
                subdirPath = path + '/' + subdir;
                children.append(parseDirTree(subdirPath, level + 1))
            return TreeNode(dirname, level, children)

def main():
    print str(parseDirTree(sys.argv[1], level = 0))

if __name__ == "__main__":
    main()

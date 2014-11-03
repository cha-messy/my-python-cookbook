# -*- coding: utf-8 -*-

import sys
import re

def normal_way():
    # @generator
    def get_file(filenames):
        for name in filenames:
            yield open(name)

    def cat(f):
        for line in f:
            yield line

    def grep(line, pattern):
        if pattern.search(line):
            return True
        return False

    def main():
        filenames, pattern = sys.argv[1:-1], sys.argv[-1]
        pattern = re.compile(pattern)
        count = 0
        for f in get_file(filenames):
            for line in cat(f):
                if grep(line, pattern):
                    count += 1
        print count
    main()

def pipeline_way():
    # @pipline @generator
    def opener(filenames):
        for name in filenames:
            yield open(name)
    def cat(filelist):
        for f in filelist:
            for line in f:
                yield line
    def grep(lines, pattern):
        for line in lines:
            if pattern.search(line):
                yield line
    def grep_files(filenames, pattern):
        # 小函数们自然而然地(只要是一个可迭代对象)更加包容, 主函数的业务逻辑也更加清晰
        pattern = re.compile(pattern)
        files = opener(filenames)
        lines = cat(files)
        hit_lines = grep(lines, pattern)
        return hit_lines
    def main():
        filenames, pattern = sys.argv[1:-1], sys.argv[-1]
        # 清晰的调用方式
        count = 0
        for line in grep_files(filenames, pattern):
            count += 1
        print count
    main()

if __name__ == '__main__':
#    normal_way()
    pipeline_way()

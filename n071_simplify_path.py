class SimplifyPath(object):
    def simplifyPath(self, path):
        """
        :param path: str
        :return: str

        tips: "/"->root directory
              ".."->upper directory
              "."->current_directory
        """
        subDirectories = path.split('/')
        cur = '/'
        for subDirectory in subDirectories:
            if subDirectory == '..':
                if cur != '/':
                    cur = cur[:cur.rfind('/')]
                    if cur == '':
                        cur = '/'
            elif subDirectory != '.' and subDirectory != '':
                cur += '/' + subDirectory if cur != '/' else subDirectory
        return cur

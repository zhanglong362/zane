import os


def login_auth(auth_type):
    '''
    带参登录认证装饰器
    :param auth_type:
    :return:
    '''
    from core import admin, student, teacher
    def auth(func):
        def wrapper(*args, **kwargs):
            if auth_type == 'admin':
                if not admin.admin_info['name']:
                    print('请先登录')
                    admin.admin_login()
                else:
                    return func(*args, **kwargs)
            elif auth_type == 'teacher':
                if not teacher.teacher_info['name']:
                    print('请先登录')
                    teacher.teacher_login()
                else:
                    return func(*args, **kwargs)
            elif auth_type == 'student':
                if not student.student_info['name']:
                    print('请先登录')
                    student.student_login()
                else:
                    return func(*args, **kwargs)

        return wrapper

    return auth


def get_all_file(file_dir):
    '''
    获得一个文件下所有文件的名字
    ps:
    os.listdir() 方法用于返回指定的文件夹包含的文件或文件夹的名字的列表
    :param file_dir:
    :return:
    '''
    file_list = os.listdir(file_dir)
    return file_list
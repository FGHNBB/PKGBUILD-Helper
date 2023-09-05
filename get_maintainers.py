def maintainers():
    var = 1
    maintainers_list_def = []
    maintainers_list_email_def = []

    name_input_cache = input('请输入包管理员（Maintainer）的名称，输入 none 跳过：')
    if name_input_cache != 'none':
        maintainers_list_def.append(name_input_cache)
        email_input_cache = input('请输入当前包管理员的电子邮箱，，输入 none 跳过：')
        if email_input_cache != 'none':
            maintainers_list_email_def.append(email_input_cache)
        if name_input_cache != 'none':
            while var == 1:
                name_input_cache = input('你可以继续输入更多包管理员的名称，输入 none 结束：')
                if name_input_cache != 'none':
                    maintainers_list_def.append(name_input_cache)
                    email_input_cache = input('请输入当前包管理员的电子邮箱，，输入 none 跳过：')
                    if email_input_cache != 'none':
                        maintainers_list_email_def.append(email_input_cache)
                else:
                    break

    return maintainers_list_def, maintainers_list_email_def

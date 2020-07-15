from django import template

register = template.Library

# 自定义过滤器
@register.filter
def chuan_upper(val):
    return val.upper()

# 自定义标签        在分页处进行调用
@register.simple_tag
def jia(a,b):
    return int(a) + int(b)



# 分页操作
def pages_(current,pages):
    """
    已知当前页和总页数，获取
    点击页数的附近页数
    :param current:当前页
    :param pages:总页数
    :return:
    """
    start = current-5
    end = current+4

    # 如果当前页要小于6页的时候
    if current < 6:
        start = 1
        end = 10

    # 如果当前页要大于总页数的时候
    if current > pages - 4:
        start = pages - 9
        end = pages

    # 如果总页数小于10
    if pages <= 10:
        start = 1
        end = pages

    for i in range(start,end+1):
        print(i,end=" ")


pages_(29,37)











import time

def get_set_time(inf,set_name="",time_set = ""):
    context = inf
    if(set_name == "送样日期"):
        if(not '送样日期' in context.keys()):
            if(time_set == ""):
                if(not '审核日期' in context.keys()):
                    return report_time_set()
                else:
                    return context['审核日期'][0:context['审核日期'].rfind(' '):]
            else:
                return time_set
        else:
            if(context['送样日期'] != ""):
                return context['送样日期']
            else:
                return report_time_set()

def report_time_set(time_set = ""):
        if(time_set == ""):
            time_set = time.strftime('%Y-%m-%d',time.localtime(time.time()))
            return time_set
        else:
            return time_set

def date_change(input_date, change_date):
    #判定是否包含环境测试，若包含则设置为1month
    #判定是否包含emc测试，若包含则设置为2week
    #获取输入日期，根据改变的日期正负调整，格式day,week,month --数字+day,week: 1day, 1week
    pass
def global_inf(target):
  global_target_app_list = ['name1','name2','name3','name4','name5']
  global_list = ['global_target_app_list']
  for global_value in global_list:
    if target in global_value:
      target_value = global_value
      return global_target_app_list

dic = {}
while True:
  arg = input()
  if arg[:4].lower() == 'quit':
    break
  elif arg[:3] == 'def':
    if arg.find('=') == -1 or arg[arg.index('=')+1] == '=':
      print('Error: invalid command')
    else:
      var = arg[arg.index('f')+1:arg.index('=')].strip()
      value = arg[arg.index('=')+1:].strip()
      if value.isdigit():
        dic[var] = int(value)
      else:
        print('Error: invalid command')
  elif arg[:4] == 'calc':
    if '+' in arg:
      var1 = arg[arg.index('l')+2:arg.index('+')].strip()
      var2 = arg[arg.index('+')+1:].strip()
      if var1 in dic.keys() and var2 in dic.keys():
        print(dic[var1]+dic[var2])
      elif var1 in dic.keys() and var2.isdigit():
        print(dic[var1]+int(var2))
      elif var1.isdigit() and var2 in dic.keys():
        print(int(var1)+dic[var2])
      elif var1.isdigit() and var2.isdigit():
        print(int(var1)+int(var2))
      else:
        print('Error: variable is not defined')
    elif '-' in arg:
      var1 = arg[arg.index('l')+2:arg.index('-')].strip()
      var2 = arg[arg.index('-')+1:].strip()
      if var1 in dic.keys() and var2 in dic.keys():
        print(dic[var1]-dic[var2])
      elif var1 in dic.keys() and var2.isdigit():
        print(dic[var1]-int(var2))
      elif var1.isdigit() and var2 in dic.keys():
        print(int(var1)-dic[var2])
      elif var1.isdigit() and var2.isdigit():
        print(int(var1)-int(var2))
      else:
        print('Error: variable is not defined')
    elif '*' in arg:
      var1 = arg[arg.index('l')+2:arg.index('*')].strip()
      var2 = arg[arg.index('*')+1:].strip()
      if var1 in dic.keys() and var2 in dic.keys():
        print(dic[var1]*dic[var2])
      elif var1 in dic.keys() and var2.isdigit():
        print(dic[var1]*int(var2))
      elif var1.isdigit() and var2 in dic.keys():
        print(int(var1)*dic[var2])
      elif var1.isdigit() and var2.isdigit():
        print(int(var1)*int(var2))
      else:
        print('Error: variable is not defined')
    elif '/' in arg:
      var1 = arg[arg.index('l')+2:arg.index('/')].strip()
      var2 = arg[arg.index('/')+1:].strip()
      if var1 in dic.keys() and var2 in dic.keys():
        if dic[var2] == 0:
          print('Error: division by zero')
        else:
          print(round(dic[var1]/dic[var2],2))
      elif var1 in dic.keys() and var2.isdigit():
        if int(var2) == 0:
          print('Error: division by zero')
        else:
          print(round(dic[var1]/int(var2),2))
      elif var1.isdigit() and var2 in dic.keys():
        if dic[var2] == 0:
          print('Error: division by zero')
        else:
          print(round(int(var1)/dic[var2],2))
      elif var1.isdigit() and var2.isdigit():
        if int(var2) == 0:
          print('Error: division by zero')
        else:
          print(round(int(var1)/int(var2),2))
      else:
        print('Error: variable is not defined')
    else:
      print('Error: invalid command')
  elif arg[:3] == 'see':
    print('======Variables======')
    for i in dic.keys():
      print('{0} : {1}'.format(i,dic[i]))
    print('=====================')
  else:
    print('undefined')
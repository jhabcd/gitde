'''2020/4/25//IDLE + list
the code in 《head first python》
chapter one'''

movies = ["last","ok","fine"]# [0,1,2]  ，‘ " 一样
print(movies)
print(len(movies))
print(movies[1])

movies.append("bad") #add one
print(movies)

movies.pop()
'bad'      #del
print(movies)

movies.extend(["bad","good"])  #add some
print(movies)

movies.remove("ok")  #del especial
print(movies)

movies.insert(1,"sad") #add before 1
print(movies)

for each_flick in movies:
    print(each_flick)

count = 0   #another way
while count < len (movies):
    print(movies[count])
    count = count + 1

movies = ["last","ok","fine",['victory',['form','forme','malformed']]]
print(movies[3][1][1])
print(movies)

for each_flick in movies:
    print(each_flick)

a = isinstance(movies,list)
print(a)

num_movies = len(movies)
a = isinstance(num_movies,list)
print(a)    # dir(__builtins__) // output 内置方法列表

for each_flick in movies:     #output still wrong
    if isinstance(each_flick,list):
        for nexted_item in each_flick:
            print(nexted_item)
    else:
        print(each_flick)
print('***********')
for each_flick in movies:   #double
    if isinstance(each_flick,list):
        for nexted_item in each_flick:
            if isinstance(nexted_item,list):
                 for deeper_item in nexted_item:
                    print(deeper_item)
            else:
                print(nexted_item)
    else:
        print(each_flick)
#create functions for duplicate code
def print_lol (the_list):
    for each_item in the_list:
        if isinstance(each_item,list):
            print_lol(each_item)       #recursive
        else:
            print(each_item)

print(movies)
print_lol(movies)
print('***********')
# better
def print_loler (the_list,level=0):# =0 提供缺省值
    for each_item in the_list:
        if isinstance(each_item,list):
            print_loler(each_item,level+1)       #recursive
        else:
            for tab_stop in range(level):
                print("\t",end='')
            print(each_item)

print(movies)
print_loler(movies,5)
print('******1*****')

# bettter
def print_lolerr (the_list,indent=False,level=0):# =0 提供缺省值
    for each_item in the_list:
        if isinstance(each_item,list):
            print_lolerr(each_item,indent,level+1)       #recursive
        else:
            if indent:
                for tab_stop in range(level):
                    print("\t",end='')
            print(each_item)

print(movies)
print_lolerr(movies)
print_lolerr(movies,True)


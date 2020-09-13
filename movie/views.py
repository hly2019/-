from django.shortcuts import render

# Create your views here.
import json
from django.shortcuts import render,HttpResponse
from django.core.paginator import Paginator
from django.shortcuts import redirect
from datetime import datetime # class one:datetime 日期时间

from datetime import date # class two:date 日期

from datetime import time # class three:time 时间
class Actor:
    Name_ = ""
    time = 0




def test(request):
    return  render (request, 'test.html')





def main_page_movie(request,page):
    movies = []
    if request.POST:
        page = request.POST['page']
        return redirect('http://localhost:8000/movie/main_page/1?page='+str(page))
    for i in range(1,1010):
        with open("C:\\Users\\hly\\Desktop\\djangoProject\\movie\\static\\movie\\movie_info\\"+str(i)+".json" , 'r', encoding='utf8')as fp:
            temp_movie = []
            json_data = json.load(fp)
            temp_movie.append(json_data['title'])
            temp_movie.append(json_data['pic'])
            movies.append(temp_movie)
    # print(movies)
    paginator = Paginator(movies, 25)  # Show 25 contacts per page.
    size = len(movies)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    print(movies)
    return render(request, 'main_page.html', {'page_obj':page_obj,'size': size})
    # return render(request, 'main_page.html', {'movie_title': movie_title, "movie_pic": movie_pic})


def all_actors_page(request,page):
    actors_ ={}
    if request.POST:
        page = request.POST['page']
        return redirect('http://localhost:8000/movie/all_actor/1?page='+str(page))
    for i in range(1,1010):
        with open("C:\\Users\\hly\\Desktop\\djangoProject\\movie\\static\\movie\\movie_info\\"+str(i)+".json" , 'r', encoding='utf8')as fp:
            json_data = json.load(fp)
            temp_actors_dic = json_data['actors']#注意这是个字典
            # print(temp_actors_dic)
            for actname in temp_actors_dic.keys():
                actors_[actname] = temp_actors_dic[actname][1]
                # print(actors_[actname])
    # print(actors_.items())
    ans =list( actors_.items())#actors是字典
    paginator = Paginator(ans, 25)  # Show 25 contacts per page.
    size = len(ans)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    print(ans)
    return render(request, 'all_actors_page.html', {'page_obj':page_obj,'size':size})



def index_(request,name_):
    print(name_)
    target_actor = {}
    hezuo_actors = {}
    hezuo_pic = {}
    canyu_mov = {}
    for i in range(1,1010):
        with open("C:\\Users\\hly\\Desktop\\djangoProject\\movie\\static\\movie\\movie_info\\"+str(i)+".json" , 'r', encoding='utf8')as fp:
            json_data = json.load(fp)

            actors = json_data['actors']#获取所有的演员
            for key in actors:#key即演员的名字
                # print(key)
                if key == name_:
                    target_actor['name'] = key
                    target_actor['pic'] = actors[key][1]
                    target_actor['comment'] = actors[key][0]
                    mov_name = json_data['title']
                    canyu_mov[mov_name] = json_data['pic'][0]
                    #找出合作最多的演员10位
                    for hezuo in actors:
                        if (hezuo != name_) & (hezuo in hezuo_actors) :#不是要找的演员，且在当前字典里
                            hezuo_actors[hezuo] += 1

                        elif (hezuo!=name_)&(hezuo not in hezuo_actors):#不是要找的演员，而且不在字典里
                            hezuo_actors[hezuo] = 1
                            hezuo_pic[hezuo] = actors[hezuo][1]
    temp = sorted(hezuo_actors.items(),key=lambda x:x[1] , reverse=True)
    # print (sorted(hezuo_actors.items(),key=lambda x:x[1] , reverse=True))
    # print(type( sorted(hezuo_actors.items(),key=lambda x:x[1] , reverse=True)  )  )
    print(temp[1][1])
    together = temp[0:12]
    ans = {}
    for ac in together:
        name = ac[0]
        tem = []
        tem.append(ac[1])#合作次数
        tem.append(hezuo_pic[name])#照片
        ans[name] = tem
    print(ans)
    # print(hezuo_pic)
    # print(together)
    print(canyu_mov)
    return render(request,'actor_page.html',{'target_actor':target_actor,'ans':ans,'canyu_mov' :canyu_mov})







def movie_index(request,name_):
    # print(name_)
    for i in range(1, 1010):
        with open("C:\\Users\\hly\\Desktop\\djangoProject\\movie\\static\\movie\\movie_info\\" + str(i) + ".json", 'r',encoding='utf8')as fp:
            json_data = json.load(fp)
            main_actors = {}
            target_movie={}
            target_movie['name'] = name_
            temp_movie = json_data
            for i in range(1,1000):
                if name_==temp_movie['title']:
                    target_movie['comment'] = temp_movie['comment']
                    target_movie['info'] = temp_movie['info']
                    target_movie['pic'] = temp_movie['pic'][0]
                    main_actors = temp_movie['actors']
                    return render(request,'movie_page.html',{'target_movie':target_movie,'main_actors':main_actors})



#搜索电影
def search_page(request):
    related_movies = []#存相关的电影和演员
    name_=""
    # print(name_)
    if request.POST:
        name_=request.POST['movies']
        if name_=="":
            return render(request, 'search_page.html')
        select_ = request.POST['selects']
        return redirect("http://localhost:8000/movie/search_result/"+name_+"/"+select_+'/1')
    return render(request, 'search_page.html')

def search_result(request,nam,select_,page ):
    print("yesyesyeyseysyeyye")
    # print(num_)
    print(nam)
    print(select_)
    if request.POST:
        date
        page = request.POST['page']
        return redirect('http://localhost:8000/movie/search_result/'+str(nam)+'/'+select_+'/1?page='+str(page))



    if 1:
        start_m = datetime.now().microsecond
        start_s = datetime.now().second
        if select_ == "电影":#搜索电影
            print("ysyasasasasasasasasas")
            name_=nam
            # print(name_)
            actor_dic = {}
            related_movies = {}#存相关的电影和演员
            for i in range(1, 1010):
                with open("C:\\Users\\hly\\Desktop\\djangoProject\\movie\\static\\movie\\movie_info\\" + str(i) + ".json", 'r',encoding='utf8')as fp:
                    json_data = json.load(fp)
                    #先搜电影
                    movie_name = json_data['title']

                    result = name_ in movie_name
                    if result:
                        related_movies[movie_name] = json_data['pic'][0]
            for i in range(1, 1010):
                with open("C:\\Users\\hly\\Desktop\\djangoProject\\movie\\static\\movie\\movie_info\\" + str(i) + ".json", 'r',encoding='utf8')as fp:
                    json_data = json.load(fp)
                    acts = json_data['actors']
                    title = json_data['title']
                    for ac in acts:
                        if name_ in ac:
                            related_movies[title] = json_data['pic'][0]
            ans = []
            ans = list(related_movies.items())
            # ans = ans[20*(num_-1):20*num_]
            paginator = Paginator(ans, 15)  # Show 25 contacts per page.

            page_number = request.GET.get('page')
            print(type(page_number))
            print(page)
            page_obj = paginator.get_page(page_number)
            size = len(ans)
            end_m = datetime.now().microsecond
            end_s=datetime.now().second
            search_time = (end_s-start_s)+(end_m-start_m)/1000000
            return render(request,'search_result_page.html',{'ans':ans,'page_obj':page_obj,'size':size,'search_time':search_time })
        elif select_ == "演员":
            name_ = nam#注意这里是演员
            actors_dic = {}
            for i in range(1, 1010):
                with open("C:\\Users\\hly\\Desktop\\djangoProject\\movie\\static\\movie\\movie_info\\" + str(i) + ".json",'r', encoding='utf8')as fp:
                    json_data = json.load(fp)
                    for it in json_data['actors']:
                        if name_ in it:
                            actors_dic[it] = json_data['actors'][it][1]#图片和名字的对应
            for i in range(1, 1010):
                with open("C:\\Users\\hly\\Desktop\\djangoProject\\movie\\static\\movie\\movie_info\\" + str(i) + ".json",'r', encoding='utf8')as fp:
                    json_data = json.load(fp)

                    if name_ in json_data['title']:
                        for act in json_data['actors']:
                            actors_dic[act] = json_data['actors'][act][1]

            ans = []
            ans  = list(actors_dic.items())
            size = len(ans)
            paginator = Paginator(ans, 15)  # Show 25 contacts per page.
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)
            end_m = datetime.now().microsecond
            end_s=datetime.now().second
            search_time = (end_s-start_s)+(end_m-start_m)/1000000
            return  render(request,'actors_search_result.html',{'ans':ans, 'page_obj':page_obj,'size' : size,'search_time':search_time })
        elif select_ == "评论":
            name_ = nam  # 注意这里是评论
            all_comment_dic = {}
            for i in range(1, 1010):
                with open("C:\\Users\\hly\\Desktop\\djangoProject\\movie\\static\\movie\\movie_info\\" + str(i) + ".json",'r', encoding='utf8')as fp:
                    json_data = json.load(fp)
                    comment = json_data['comment']
                    title = json_data['title']
                    for com in comment:
                        if name_ in com:
                            print(title)
                            print(com)
                            print(type(all_comment_dic))
                            all_comment_dic[com] = title
            ans = list(all_comment_dic.items())
            size = len(ans)
            paginator = Paginator(ans, 15)  # Show 25 contacts per page.
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)
            end_m = datetime.now().microsecond
            end_s=datetime.now().second
            search_time = (end_s-start_s)+(end_m-start_m)/1000000
            return render(request,'comment_search_page.html',{ 'ans':ans,'page_obj':page_obj,'size':size,'search_time':search_time})






    return render(request, 'search_page.html')







def page_movie(request,num_):#实现主页的分页

    movies = []
    for i in range(20*(num_-1)+1,num_*20):
        with open("C:\\Users\\hly\\Desktop\\djangoProject\\movie\\static\\movie\\movie_info\\" + str(i) + ".json", 'r',
                  encoding='utf8')as fp:
            temp_movie = []
            json_data = json.load(fp)
            temp_movie.append(json_data['title'])
            temp_movie.append(json_data['pic'])
            movies.append(temp_movie)
        # print(movies)
    return render(request, 'slide_movie_page.html', {'movies': movies,'last':num_-1,'next':num_+1})
def page_actor(request,num_):
    actors_ ={}
    for i in range(1,1010):
        with open("C:\\Users\\hly\\Desktop\\djangoProject\\movie\\static\\movie\\movie_info\\"+str(i)+".json" , 'r', encoding='utf8')as fp:
            json_data = json.load(fp)
            temp_actors_dic = json_data['actors']#注意这是个字典
            # print(temp_actors_dic)
            for actname in temp_actors_dic.keys():
                actors_[actname] = temp_actors_dic[actname][1]
                # print(actors_[actname])
    # print(actors_.items())
    ans =list( actors_.items())#actors是字典
    print(type (actors_))
    print(type(ans))
    ans = ans[20*(num_-1) :20*num_]

    # print(ans)

    return render(request, 'slide_actor_page.html', {'actors_':ans,'next':num_+1,'last':num_-1})


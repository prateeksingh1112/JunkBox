from django.shortcuts import render , HttpResponse , redirect
import csv
from .models import Movie , Year , Rating , Genres , FeedBack , Series , Language
import random
import requests
from bs4 import BeautifulSoup
from datetime import date
# Create your views here.


def index(request):
    m = Rating.objects.get(rating = 8)
    count =0
    slidey_movie = []
    while len(slidey_movie) != 15:
        random_obj = random.choice(m)
        if random_obj.image != " " and random_obj.desc != " " and len(random_obj.year) == 4 and int(random_obj.year) > 2015:
            count = count +1
            img = random_obj.image.split(", ")[0]
            if count ==15:
                break
            slidey_movie.append([random_obj.Movie_name , img , random_obj.desc])

    featured = []
    count = 0
    while len(featured) != 6:
        random_obj = random.choice(m)
        if random_obj.poster != " " and len(random_obj.year) == 4 and int(random_obj.year) > 2015:

            if count == 6:
                break
            count = count + 1
            featured.append([random_obj.Movie_name , random_obj.poster , random_obj.year])


    popular_movie = []
    index_c = -1
    for i in range(3):
        index_c = index_c + 1
        popular_movie.append([])
        count = 0
        for i in m:
            if i.image != " ":
                img = i.image.split(", ")[0]

                if count == 6:
                    break
                count = count + 1

                popular_movie[index_c].append([i.Movie_name, img, i.year])



    return render(request, 'index.html' , {'movie_list' : slidey_movie, 'featured' : featured , 'popular' : popular_movie})



def check(request):
    m = Series.objects.all()
    count = 0
    # l = []
    # for i in m:
    #     if i.trailer == " " or i.trailer == 'N/A' or i.trailer == "None":
    #         count = count + 1
    #         l.append([i.Movie_name])
    #         print(count)
    #
    # with open('Movie_list.csv', 'w', newline='', encoding="utf-8") as file:
    #     writer = csv.writer(file, delimiter=',')
    #     writer.writerows(l)

    # for i in m:
    #     print(i.Series_name.split())
    #     if len(i.Series_name.split()) == 1 or len(i.Series_name.split()) == 2:
    #         count = count + 1
    #         print(count)

    #for years

    # for i in m:
    #     if len(i.year) == 4:
    #         y = Year.objects.get_or_create(year = i.year)[0]
    #         y.movie.add(i)
    #         y.no_of_movies = len(y.movie.all())
    #         y.save()
    #
    #
    #     count = count + 1
    #     print(count)


   #for rating
    for i in m:
        if i.poster != "N/A" and i.poster != "None" and i.poster != " ":
            # print([i.Movie_name , i.rating , len(r.movie.all())])

            count = count + 1
        print(count)


    # for i in m:
    #     if i.genres != " " and i.genres != "N/A" and i.genres != "None":
    #         if "," in i.genres:
    #             l = i.genres.split(", ")
    #         else:
    #             l = i.genres.split(" | ")
    #
    #         for j in l:
    #             g = Genres.objects.get_or_create(genres = j)[0]
    #             g.movie.add(i)
    #             g.no_of_movies = len(g.movie.all())
    #             g.save()
    #             # print([i.Movie_name , j , g.no_of_movies])
    #
    #         count = count + 1
    #         # if count == 20:
    #         #     break
    #         print(count)

    return HttpResponse(count)



def bhai(request):

    m = Movie.objects.all()
    count = 0
    # for i in m:
    #
    #     if i.year == " " and i.year == 'N/A' and i.year == 'None':
    #         r = Year.objects.get(year = i.year)
    #         r.movie.add(i)
    #         r.save()
    #     print(count)
    #     count = count + 1




    # f = open(r'C:\Users\Mr.Mg\Documents\Python\Projects\you5.csv', encoding="utf-8")
    # csv_f = csv.reader(f)
    # csv_f = [i for i in csv_f]
    # count = 0
    #
    # for i in csv_f[420:]:
    #     m = Movie.objects.get(Movie_name = i[0])
    #     m.trailer = i[1].replace('watch?v=' , 'embed/')
    #     m.save()
    #     count = count + 1
    #     print(count)



    # for s in Series_list:
    # for i in csv_f:
    #     # print(len(i))
    #     # print(14 , i[14])
    #     # print(9, i[9])
    #     # print(12, i[12])
    #     # print(11, i[11])
    #     # print(8, i[8])
    #     # print(7, i[7])
    #     # print(6, i[6])
    #     # print(5, i[5])
    #     # print(4, i[4])
    #     # print(3, i[3])
    #     # print(2, i[2])
    #     # print(1, i[1])
    #     # break
    #     if len(i) != 0:
    #         s = Movie.objects.get_or_create(Movie_name = i[0])[0]
    #         s.cast = i[1]
    #         s.awards = i[2]
    #         s.boxoffice = i[3]
    #         s.director = i[4]
    #         s.genres = i[5]
    #         s.language = i[6]
    #         s.desc = i[7]
    #         s.rating = i[8]
    #         s.release_date = i[9]
    #         s.writer = i[11]
    #         s.year = i[12]
    #         s.poster = i[14]
    #         s.save()
    #
    #     print(count)
    #     count = count + 1


    # for i in csv_f:
    #     m = Movie.objects.get_or_create(Movie_name = i[0])[0]
    #     m.language = i[1]
    #     m.save()
    #     count = count + 1
    #     print(count)

    # for i in csv_f:
    #     if bool(Movie.objects.filter(Movie_name=i[1])) == True:
    #         m = Movie.objects.get(Movie_name = i[1])
    #         l = i[5][2:-2].replace("'" , "").split(', ')[0]
    #         m.image = l
    #         count = count + 1
    #         print(count)
    #         m.save()

    # m = Movie.objects.all()
    # poster_list = []
    # for i in m:
    #     if i.poster == "None" or i.poster == " " or i.poster == "N/A":
    #         poster_list.append([i.Movie_name])
    #
    #     count = count + 1
    #     print(count)
    #
    # with open('Cast_list.csv', 'w', newline='', encoding="utf-8") as file:
    #     writer = csv.writer(file, delimiter=',')
    #     writer.writerows(poster_list)

    return HttpResponse("hogya bhaiya")



def singleMovie(request):
    try:
        name = request.GET.get('name')
        m = Movie.objects.get(Movie_name = name)
        img = m.image.split(", ")
        length = len(img)
        desc = m.desc
        genres = m.genres
        cast = m.cast
        rating = m.rating
        link = m.link.split(", ")
        poster = m.poster
        count = 1
        link_list = []
        for i in link:
            link_list.append([count , i])
            count = count + 1

        release = m.release_date
        trailer = m.trailer

        return render(request , 'single.html' , {'name':m.Movie_name , 'img':img , 'length' : length ,'desc':desc , 'genres':genres , 'cast':cast , 'rating' : rating , 'link':link_list , 'release' : release , 'trailer' : trailer , 'poster': poster})

    except:
        return render(request , 'error.html')



def genresMovie(request):
    try:
        g = request.GET.get('genres')
        m = Genres.objects.get(genres = g)
        movie_list = m.movie.all()
        page_no_list = [i for i in range(0, 5)]
        page = 1
        genres = []
        index_c = 0
        for j in range(4):
            index_c = index_c + 1
            count = 0
            l = []

            for i in movie_list[(index_c-1)*6 : index_c*6]:
                if i.rating != 'N/A' and i.rating != 'None' and i.rating != " ":
                    rating = [j for j in range(int(float(i.rating) // 2))]
                else:
                    rating = []
                l.append([i.Movie_name , i.poster , rating , i.year])
                count = count + 1
                    # print(i.poster)
                if count == 6:
                    break

            genres.append(l)
            # print(genres)

        return render(request , 'genres.html' , {"genres" : genres , 'title':g , 'page' : page_no_list , 'Prev' : page - 1 , 'Next':page })
        # return HttpResponse(genres)`


    except:
        return render(request, 'error.html')



def page_list(last_page , request_page):
    n = 6
    if (request_page + n) -1 <= last_page:
        return [i for i in range(request_page , request_page+n)]

    else:
        while True:
            if (request_page + n) <= last_page:
                return [i for i in range(request_page, request_page + n)]

            else:
                n = n - 1



def page(request):
    try:
        page = request.GET.get('no')
        g = request.GET.get('type')
        if g == "All Movies" :
            movie_list = Movie.objects.all()
            last_page = len(movie_list)//24

        elif g.isnumeric():
            m = Year.objects.get(year=g)
            movie_list = m.movie.all()
            last_page = m.no_of_movies // 24

        else:
            try:
                m = Genres.objects.get(genres=g)
                movie_list = m.movie.all()
                last_page = m.no_of_movies // 24

            except:
                print(g)
                m = Language.objects.get(language=g)
                movie_list = m.movie.all()
                last_page = m.no_of_movies // 24

        page = int(page)
        start = 24*page
        movie_list = movie_list[start : ]

        page_no = page_list(last_page , page)
        genres = []
        index_c = 0
        for i in range(4):
            index_c = index_c + 1
            count = 0
            l = []

            for i in movie_list[(index_c - 1) * 6: index_c * 6]:
                if i.rating != 'N/A' and i.rating != 'None' and i.rating != " ":
                    rating = [j for j in range(int(float(i.rating) // 2))]
                else:
                    rating = []
                l.append([i.Movie_name, i.poster, rating, i.year])
                count = count + 1

                if count == 6:
                    break

            genres.append(l)
            # print(genres)
            if page == 0:
                page = 1

        return render(request, 'genres.html', {"genres": genres, 'title': g , 'page':page_no , 'Prev' : page -1 , 'Next' : page +1})


    except:
        return render(request, 'error.html')



def AZlist(request):
    try:
        no = []
        B = []
        C = []
        D = []
        E = []
        F = []
        G =[]
        H =[]
        I =[]
        J =[]
        K =[]
        L =[]
        M =[]
        N =[]
        O =[]
        P =[]
        Q =[]
        R =[]
        S =[]
        T =[]
        U =[]
        V =[]
        W =[]
        X =[]
        Y =[]
        Z =[]
        A = []
        m = Movie.objects.all()
        for i in m[:5000]:
            if i.poster != " " and i.poster != "None" and i.poster != 'N/A':
                if i.Movie_name[0] == 'A':
                    A.append([i.Movie_name , i.poster, i.year , i.genres , i.rating])
                elif i.Movie_name[0] == 'B':
                    B.append([i.Movie_name , i.poster , i.year , i.genres , i.rating])
                elif i.Movie_name[0] == 'C':
                    C.append([i.Movie_name , i.poster , i.year , i.genres , i.rating])
                elif i.Movie_name[0] == 'D':
                    D.append([i.Movie_name , i.poster , i.year , i.genres , i.rating])
                elif i.Movie_name[0] == 'E':
                    E.append([i.Movie_name , i.poster , i.year , i.genres , i.rating])
                elif i.Movie_name[0] == 'F':
                    F.append([i.Movie_name , i.poster , i.year , i.genres , i.rating])
                elif i.Movie_name[0] == 'G':
                    G.append([i.Movie_name ,  i.poster ,i.year , i.genres , i.rating])
                elif i.Movie_name[0] == 'H':
                    H.append([i.Movie_name , i.poster , i.year , i.genres , i.rating])
                elif i.Movie_name[0] == 'I':
                    I.append([i.Movie_name , i.poster , i.year , i.genres , i.rating])
                elif i.Movie_name[0] == 'J':
                    J.append([i.Movie_name ,  i.poster ,i.year , i.genres , i.rating])
                elif i.Movie_name[0] == 'K':
                    K.append([i.Movie_name , i.poster , i.year , i.genres , i.rating])
                elif i.Movie_name[0] == 'L':
                    L.append([i.Movie_name , i.poster , i.year , i.genres , i.rating])
                elif i.Movie_name[0] == 'M':
                    M.append([i.Movie_name , i.poster , i.year , i.genres , i.rating])
                elif i.Movie_name[0] == 'N':
                    N.append([i.Movie_name ,  i.poster ,i.year , i.genres , i.rating])
                elif i.Movie_name[0] == 'O':
                    O.append([i.Movie_name , i.poster , i.year , i.genres , i.rating])
                elif i.Movie_name[0] == 'P':
                    P.append([i.Movie_name , i.poster , i.year , i.genres , i.rating])
                elif i.Movie_name[0] == 'Q':
                    Q.append([i.Movie_name , i.poster , i.year , i.genres , i.rating])
                elif i.Movie_name[0] == 'R':
                    R.append([i.Movie_name , i.poster , i.year , i.genres , i.rating])
                elif i.Movie_name[0] == 'S':
                    S.append([i.Movie_name , i.poster , i.year , i.genres , i.rating])
                elif i.Movie_name[0] == 'T':
                    T.append([i.Movie_name ,  i.poster ,i.year , i.genres , i.rating])
                elif i.Movie_name[0] == 'U':
                    U.append([i.Movie_name , i.poster , i.year , i.genres , i.rating])
                elif i.Movie_name[0] == 'V':
                    V.append([i.Movie_name , i.poster , i.year , i.genres , i.rating])
                elif i.Movie_name[0] == 'W':
                    W.append([i.Movie_name , i.poster , i.year , i.genres , i.rating])
                elif i.Movie_name[0] == 'X':
                    X.append([i.Movie_name , i.poster , i.year , i.genres , i.rating])
                elif i.Movie_name[0] == 'Y':
                    Y.append([i.Movie_name ,  i.poster ,i.year , i.genres , i.rating])
                elif i.Movie_name[0] == 'Z':
                    Z.append([i.Movie_name , i.poster , i.year , i.genres , i.rating])
                else:
                    no.append([i.Movie_name , i.poster , i.year , i.genres , i.rating])


        return render(request , 'list.html' , {'A': A , 'B' : B , 'C': C , 'D': D , 'E': E , 'F': F , 'G': G , 'H' : H , 'I': I , 'J': J , 'K' : K , 'L':L , 'M':M , 'N':N , 'O': O , 'P': P , 'Q': Q , 'R': R , 'S' : S , 'T' : T , 'U': U , 'V': V , 'W': W , 'X': X, 'Y': Y , 'Z': Z , 'no': no })

    except:
        return render(request , 'error.html')



def AllMovies(request):
    # try:
    movie_list = Movie.objects.all()
    page_no_list = [i for i in range(0, 5)]
    page = 1
    AllMovie = []
    index_c = 0
    for j in range(4):
        index_c = index_c + 1
        count = 0
        l = []

        for i in movie_list[(index_c - 1) * 6: index_c * 6]:
            if i.poster != " " and i.poster != "N/A" and i.poster != "None" and len(i.rating) == 3:

                rating = [j for j in range(int(float(i.rating) // 2))]
                l.append([i.Movie_name, i.poster, rating, i.year])
                count = count + 1
                # print(i.poster)
            if count == 6:
                break

        AllMovie.append(l)


    return render(request , 'allMovie.html' , {"AllMovie": AllMovie, 'title': "All Movies", 'page': page_no_list, 'Prev': page - 1, 'Next': page} )


    # except:
    #     return render(request, 'error.html')



def feedBackPage(request):
    return render(request , 'contact.html')



def feedBack(request):
    try:
        firstName = request.POST['firstName']
        lastName = request.POST['lastName']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']


        feedBack = FeedBack(First_Name = firstName , Last_Name = lastName)
        feedBack.email = email
        feedBack.subject = subject
        feedBack.message = message
        feedBack.save()

        return redirect(feedBackPage)


    except:
        return render(request, 'error.html')

# def yearsdemo(request):
#     y = request.GET.get('year')
#     m = Year.objects.get(year=y)
#     movie_list = m.movie.all()
#     page_no_list = [i for i in range(0, 5)]
#     page = 1
#     years = []
#     index_c = 0
#     for j in range(4):
#         index_c = index_c + 1
#         count = 0
#         l = []
#
#         for i in movie_list[(index_c - 1) * 6: index_c * 6]:
#             if i.poster != " " and i.poster != "N/A" and i.poster != "None":
#                 l.append([i.Movie_name, i.poster, i.rating, i.year])
#                 count = count + 1
#             if count == 6:
#                 break
#
#         years.append(l)
#
#     return render(request, 'years.html', {"years": years, 'title': y, 'page': page_no_list, 'Prev': page - 1, 'Next': page})


def years(request):
    try:
        g = request.GET.get('year')
        m = Year.objects.get(year=g)
        movie_list = m.movie.all()
        page_no_list = [i for i in range(0, 5)]
        page = 1
        genres = []
        index_c = 0
        for j in range(4):
            index_c = index_c + 1
            count = 0
            l = []

            for i in movie_list[(index_c - 1) * 6: index_c * 6]:
                if i.poster != " " and i.poster != "N/A" and i.poster != "None":
                    l.append([i.Movie_name, i.poster, i.rating, i.year])
                    count = count + 1
                    # print(i.poster)
                if count == 6:
                    break

            genres.append(l)
            # print(genres)

        return render(request, 'genres.html', {"genres": genres, 'title': g, 'page': page_no_list, 'Prev': page - 1, 'Next': page})

    except:
        return render(request , 'error.html')



def search(request):
    # try:
    s = request.GET.get('Search')
    m = Movie.objects.all()
    movie_list = []
    l = []
    for i in m:
        if s.lower() in i.Movie_name.lower():
            if i.rating != 'N/A' and i.rating != 'None' and i.rating != " ":
                rating = [j for j in range(int(float(i.rating)// 2))]
            else:
                rating = []
            l.append([i.Movie_name , i.poster , rating , i.year])



    count = 0
    index = 0
    print(len(l))
    while(len(l) > index):
        movie_list.append([])
        for i in range(6):
            if len(l) == index:
                break
            movie_list[count].append(l[index])
            index = index  + 1
        count = count + 1

    print(len(l))
    return render(request , 'search.html' , {'search':movie_list , 'title' : 'Search Result of ' + s , 'len' : len(l) , 'Page' : False})

    # except:
    #     return render(request , 'error.html')



def news(request):
    url = "https://www.cinemablend.com/news.php"
    list_movies = []
    c = 0
    images = []
    data1 = []
    data2= []
    name = []
    desc_link=[]
    response = requests.get(url, timeout=10)
    soup = BeautifulSoup(response.content, 'html.parser')
    for text in soup.find_all('span', attrs={'class': 'story-related-title'}):
        news_title = text.text
        name.append(news_title)
    for link in soup.find_all('span', attrs={'class': 'story-cover-image'}):
        t = link.find('img')
        if 'jpg' in t['data-src']:
            imgt = t['data-src']
        images.append(imgt)
    for link in soup.find_all('a', attrs={'class': 'story-related-story'}):
        link_desc = link['href']
        desc_link.append(link_desc)

    l = len(name)
    z = l//2
    name_list=["Himanshu", "Mohit", "Prateek"]
    for i in range(0, z, 1):
        data1.append([name[i], images[i], desc_link[i], random.randint(10000,100000), random.randint(1,12)])
    for i in range(z+1, l, 1):
        data2.append([name[i], images[i], desc_link[i], random.randint(1,12), random.choice(name_list)])
    return render(request, 'news.html', {'list1':data1, 'list2':data2, 'date':date.today()})



def language(request):
    try:
        g = request.GET.get('language')
        print(g)
        m = Language.objects.get(language = g)
        movie_list = m.movie.all()
        page_no_list = [i for i in range(0, 5)]
        page = 1
        genres = []
        index_c = 0
        for j in range(4):
            index_c = index_c + 1
            count = 0
            l = []

            for i in movie_list[(index_c-1)*6 : index_c*6]:
                if i.rating != 'N/A' and i.rating != 'None' and i.rating != " ":
                    rating = [j for j in range(int(float(i.rating) // 2))]
                else:
                    rating = []
                l.append([i.Movie_name , i.poster , rating , i.year])
                count = count + 1
                    # print(i.poster)
                if count == 6:
                    break

            genres.append(l)
            # print(genres)

        return render(request , 'genres.html' , {"genres" : genres , 'title':g , 'page' : page_no_list , 'Prev' : page - 1 , 'Next':page })
        # return HttpResponse(genres)


    except:
        return render(request, 'error.html')
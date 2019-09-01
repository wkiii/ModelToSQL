import requests


def get_movies(url):

    resp = requests.get(url)

    # print(resp.status_code)

    result = resp.json()

    movies = result.get("data")

    # print(movies)

    for movie in movies:
        print(movie.get("title"))


if __name__ == '__main__':

    for i in range(20):

        url = "https://www.vmovier.com/apiv3/post/getPostInCate?cateid=0&p=%d" % i

        get_movies(url)



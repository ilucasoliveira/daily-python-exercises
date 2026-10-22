from elasticsearch import Elasticsearch

elastic = Elasticsearch("http://localhost:9200")

info = elastic.info()
print(info["version"]["number"])  # 9.4.8 elasticsearch version in the docker-compose

elastic.index(
    index="books",
    id=1,
    document={"title": "The Hobbit", "year": 1936, "genre": "fantasy"},
)
elastic.index(
    index="books",
    id=2,
    document={"title": "Hunger Games", "year": 2006, "genre": "romance"},
)
elastic.index(
    index="books",
    id=3,
    document={"title": "Twilight", "year": 2005, "genre": "romance"},
)

elastic.indices.refresh(index="books")

result_books = elastic.search(index="books", query={"match_all": {}})

print(result_books["hits"]["total"]["value"])  # 3

for i in result_books["hits"]["hits"]:
    print(i["_source"]["title"])

result_romance = elastic.search(index="books", query={"match": {"genre": "romance"}})
for i in result_romance["hits"]["hits"]:
    print(i["_source"]["title"])

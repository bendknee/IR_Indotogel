import string

data = open('dataset.txt', 'r')
prov = ""
kamus = {}
for word in data.readlines():
    if ";" in word:
        prov = word.strip("<>;\n")
    else:
        word = word.strip().lower()
        if word not in kamus.keys():
            kamus[word] = {prov}
        else:
            kamus[word].add(prov)

query = "bungong jeumpa"


def quque(query):
    all_query_province = []
    for p in string.punctuation:
        query = query.replace(p, " ").strip(" ")
    for word in query.split():
        try:
            all_query_province.append(kamus[word])
        except KeyError:
            all_query_province.append({"Tidak Diketahui"})

    final_bobot = {}
    print(all_query_province)
    for set in all_query_province:
        for prov in set:
            bobot_di_set = list(set).count(prov) / len(set)
            if prov not in final_bobot:
                final_bobot[prov] = round(bobot_di_set / len(all_query_province), 2)
            else:
                final_bobot[prov] += round(bobot_di_set / len(all_query_province), 2)

    print(final_bobot)

quque(query)
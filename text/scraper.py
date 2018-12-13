import string


def python_writer():
    dataset = open('data/dataset.txt', 'r')
    kamus_provinsi = {}
    for word in dataset.readlines():
        if ";" in word:
            prov = word.strip("<>;\n")
            prov = prov.split()
            prov = [c.capitalize() for c in prov]
            prov = " ".join(prov)
        else:
            word = word.strip().lower()
            if word not in kamus_provinsi.keys():
                kamus_provinsi[word] = {prov}
            else:
                kamus_provinsi[word].add(prov)
    out_file = open('data/processed_data.py', 'w')
    print("kamus_provinsi = ", file=out_file, end='')
    print(kamus_provinsi, file=out_file)
    out_file.close()

query = "situmorang"


def quque(query):
    from text.data.processed_data import kamus_provinsi
    all_query_province = []
    for p in string.punctuation:
        query = query.replace(p, " ").strip(" ")
    for word in query.split():
        try:
            all_query_province.append(kamus_provinsi[word])
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

python_writer()
quque(query)
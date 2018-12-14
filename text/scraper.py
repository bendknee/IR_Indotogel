import string


def dict_writer():
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


def quque(query):
    from text.data.processed_data import kamus_provinsi
    prov_tiap_query = []
    for p in string.punctuation:
        query = query.replace(p, " ").strip(" ")
    for word in query.split():
        try:
            prov_tiap_query.append(kamus_provinsi[word])
        except KeyError:
            prov_tiap_query.append({"Tidak Dapat Diketahui"})

    final_bobot = {}
    for set in prov_tiap_query:
        for prov in set:
            bobot_di_set = list(set).count(prov) / len(set)
            if prov not in final_bobot:
                final_bobot[prov] = round(bobot_di_set / len(prov_tiap_query), 2) * 100
            else:
                final_bobot[prov] += round(bobot_di_set / len(prov_tiap_query), 2) * 100

    return final_bobot

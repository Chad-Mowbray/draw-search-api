
# import pickle


# def process(data):
#     # print(data)
#     # print(len(data))
#     x = [tuple(x) for y in data for x in y]
#     # print(x, "\n\n")
#     y = set(x)
  
#     z = list(y)
#     z.sort()
#     # print(z, "\n\n")
#     generate_summary(z)


# def generate_empty_structure():
#     starter = []
#     for i in range(101):
#         for j in range(101):
#             starter.append((i,j))
#     return starter


# def generate_summary(processed_data):
#     flat = []
#     starter = generate_empty_structure()
#     for coord in starter:
#         if coord in processed_data:
#             flat.append(1)
#         else:
#             flat.append(0)
#     # print(flat)
#     # print(len(flat))
#     pickler(flat)
#     check_pickled_file()



# def pickler(flat):
#     print('pickler called...')
#     try:
#         base = pickle.load(open("stuff.pickle", "rb"))
#         base.append(flat)
#         pickle.dump(base, open("stuff.pickle", "wb"))
#     except (OSError, IOError) as e:
#         pickle.dump([], open("stuff.pickle", "wb"))
    

# def check_pickled_file():
#     stuff = pickle.load(open("stuff.pickle", "rb"))
#     print(len(stuff))


import pickle
from sklearn.naive_bayes import GaussianNB

def process(data):
    x = [tuple(x) for y in data for x in y]
    y = set(x)
    z = list(y)
    z.sort()
    return generate_summary(z)


def generate_empty_structure():
    starter = []
    for i in range(101):
        for j in range(101):
            starter.append((i,j))
    return starter


def generate_summary(processed_data):
    flat = []
    starter = generate_empty_structure()
    for coord in starter:
        if coord in processed_data:
            flat.append(1)
        else:
            flat.append(0)

    # print(flat.reshape(1,-1))
    # print(len(flat))
    # pickler(flat)
    # check_pickled_file()
    trained_model = pickle.load(open("trained_model.pickle", "rb"))
    res = trained_model.predict([flat])
    print(res)
    return res
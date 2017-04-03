import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np


df  = pd.read_csv('Shorts.csv')


def get_titles_feature():
    title = df.title
    titles = title.tolist()
    cv = CountVectorizer()
    cv_fit=cv.fit_transform(titles).toarray()
    return cv_fit

def get_description_feature():
    description = df.description
    l = len(description)
    for i in range(l):
        if pd.isnull(description[i]):
            description.set_value(i,"Nothing")
    description = description.tolist()
    cv = CountVectorizer()
    cv_fit = cv.fit_transform(description).toarray()
    return cv_fit

def get_mrp():
    return df.mrp.tolist()

def get_family_feature():
    data_product_ids = df.productId.tolist()
    data_family_ids = df.productFamily.tolist()
    l = len(data_family_ids)
    for i in range(0,l):
        data_family_ids[i]=data_family_ids[i]+','+(data_product_ids[i])
    cv = CountVectorizer()
    cv_fit=cv.fit_transform(data_family_ids).toarray()
    return cv_fit
def get_color_feature():
    color_of_product = df.color
    l = len(color_of_product)
    for i in range(l):
        if pd.isnull(color_of_product[i]):
            color_of_product.set_value(i,"Unknown")
    color_of_product = color_of_product.tolist()
    cv = CountVectorizer()
    cv_fit = cv.fit_transform(color_of_product).toarray()
    return cv_fit

def get_key_specs():
    key_spec = df.keySpecsStr.tolist()
    l = len(key_spec)
    splitted_key_specs =[]
    for i in range(l):
        if not pd.isnull(key_spec[i]):
            split_it = key_spec[i].split(';')
            split_len = len(split_it)
            s = split_it[0]
            for j in range(1,split_len):
                s=s+' , '+split_it[j]
            splitted_key_specs.append(s)
        else:
            splitted_key_specs.append("Nothing")
    cv = CountVectorizer()
    cv_fit = cv.fit_transform(splitted_key_specs).toarray()
    return cv_fit


def get_detailed_key_specs():
    specs = df.detailedSpecsStr.tolist()
    l = len(specs)
    splitted_key_specs = []
    for i in range(l):
        if not pd.isnull(specs[i]):
            split_it = specs[i].split(';')
            split_len = len(split_it)
            s = split_it[0]
            for j in range(1,split_len):
                s = s +' , '+split_it[j]
            splitted_key_specs.append(s)
        else :
            splitted_key_specs.append('Nothing')
    cv = CountVectorizer()
    cv_fit = cv.fit_transform(splitted_key_specs).toarray()
    return cv_fit


def get_product_brand():
    brands = df.productBrand.tolist()
    cv = CountVectorizer()
    cv_fit = cv.fit_transform(brands).toarray()
    return cv_fit

titles_v = get_titles_feature()
family_v = get_family_feature()
description_v = get_description_feature()
detailed_key_v = get_detailed_key_specs()
key_v = get_key_specs()
mrp_v    = get_mrp()
color_v = get_color_feature()
product_brand_v = get_product_brand()
similarity_matrix = []

for i in range(34293):
    lis = []
    vector1 =titles_v[i]
    vector1 = np.append(vector1,family_v[i])
    vector1 = np.append(vector1,description_v[i])
    vector1 = np.append(vector1,detailed_key_v[i])
    vector1 = np.append(vector1,key_v[i])
    vector1 = np.append(vector1,color_v[i])
    vector1 = np.append(vector1,product_brand_v[i])
    for j in range(34293):
            vector2 =titles_v[j]
            vector2 = np.append(vector2,family_v[j])
            vector2 = np.append(vector2,description_v[j])
            vector2 = np.append(vector2,detailed_key_v[j])
            vector2 = np.append(vector2,key_v[j])
            vector2 = np.append(vector2,color_v[j])
            vector2 = np.append(vector2,product_brand_v[j])
            lis.append(cosine_similarity(vector1.reshape(1,-1),vector2.reshape(1,-1)))
    similarity_matrix.append(lis)
with open('feaures','wb') as f:
	f.write(similarity_matrix)
f.close()







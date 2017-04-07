# Recommended system
Similarity calculation of text:

Assumption :

    I assumed these column are useful for finding the similarity of the products
        1.Title (Similar titles products can be similar)
        2.Description('')
        3.Brand
        3. Mrp as mrp across different platform doesn’t change souseful checking both are thesame items or not)
        4. product family
        5.color
        6.key specs, detailed key specs
        
        
Vectorize all these columns so that we can find the similarity using these vectors
Note: NaN cases should be handled here


    Use cosine similarity by giving optimal weight to image vector and to text vector
    Sort the similarity score and get the top 25 similar products and print it in a json format with the similarity score
    finally we can see the similar products related to the product
    
    
Similarity calculation of image:
We can get the image feature vectors using GoogLeNet check this out 

http://www.marekrei.com/blog/transforming-images-to-feature-vectors/ 



Give some optimal weigths to the image and text similarity score

Output everything in JSON format 

Productids with the similar items and there percentage similarity


Use gpu for fasters results


Finally for getting  faster cosine similarity check this out 

https://github.com/facebookresearch/faiss







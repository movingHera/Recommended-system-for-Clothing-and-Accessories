import graphlab as gl
url ='images'
data = gl.image_analysis.load_images(url, "auto", with_path=False,recursive=True)
extractor = gl.feature_engineering.DeepFeatureExtractor(features = 'image', model='auto')
extractor = extractor.fit(data)
features_sf = extractor.transform(data)
with open('glfeatures','wb') as f:
	f.write(features_sf['deep_features_image'])
f.close()


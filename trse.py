from sklearn.feature_extraction.text import TfidfVectorizer
def word_count(w,st):
	string=st
	word=w
	a=[]
	count=0
	a=string.split(" ")
	for i in range(0,len(a)):
	      if(word==a[i]):
	            count=count+1
	return count
dic={}
inverted_list=[]
with open("movies.txt","r") as f:
    content = f.readlines()
content = [x.strip() for x in content] 
tfidf=TfidfVectorizer()
tfs=tfidf.fit_transform(content)
feature_names=tfidf.get_feature_names()
for i in range(len(content)):
	for feature in feature_names:
		if feature in content[i]:
			c=word_count(feature,content[i])
			if feature not in dic.keys():
				dic[feature]=[[str(i),c+1]]
			else:
				dic[feature].append([str(i),c+1])
		else:
			continue
for key in dic.keys():
	inverted_list.append([key,len(dic[key]),dic[key]])

for val in inverted_list:
	print(val)
	print("\n")
def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3
phrase=input("enter the phrase\n").strip()
if phrase in feature_names:
	print(dic[phrase])
else:
	try:
		p1,p2,p3=phrase.split(" ")
		print("three phrase word")
		val1=dic[p1]
		val2=dic[p2]
		val3=dic[p3]
		v1=intersection(val1,val2)
		v=intersection(v1,val3)
	except:
		print("two phrase word")
		p1,p2=phrase.split(" ")
		val1=dic[p1]
		val2=dic[p2]
		if len(val1)!= len(val2):
			v=intersection(val1,val2)
		else:
			v=val1
	for val in v:
		if phrase in content[int(val[0])]:
			print("found at doc id:",val[0])
		else:
			continue




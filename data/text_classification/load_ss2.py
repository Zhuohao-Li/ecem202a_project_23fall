import dataset

dataset = datasets.load_dataset("glue", "sst2", split='train')

# if we sample n data

n_samples = 500
X = dataset.data["sentence"].to_pylist()[:n_samples]
y = dataset.data["label"].to_pylist()[:n_samples]

#results = classifier(X) #here the classifier could be loaded llm
# 
#  
# predictions = [0 if res["label"] == "NEGATIVE" else 1 for res in results]
# print(metric.compute(predictions=predictions, references=y))


import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori,association_rules

transaction =[
    ['milk','bread','butter'],
    ['bread','butter','jam'],
    ['milk','bread','butter','jam'],
    ['milk','bread'],
    ['bread','butter'],
]

te= TransactionEncoder()
te_ary=te.fit_transform(transaction)
df=pd.DataFrame(te_ary,columns=te.columns_)
frequent_itemsets=apriori(df,min_support=0.3,use_colnames=True)
rules=association_rules(frequent_itemsets,metric="lift",min_threshold=1.2)

print("Frequent Itemsets:")
print(frequent_itemsets)
print("\nAssociation Rules:")
print(rules)

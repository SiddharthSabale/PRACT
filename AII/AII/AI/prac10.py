import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules

# Sample transactions data
transactions = [
    ['milk', 'bread', 'butter'],
    ['bread', 'butter', 'jam'],
    ['milk', 'bread', 'butter', 'jam'],
    ['milk', 'bread'],
    ['bread', 'butter'],
]

# Encoding the transactions to a one-hot encoded dataframe
te = TransactionEncoder()
te_ary = te.fit_transform(transactions)
df = pd.DataFrame(te_ary, columns=te.columns_)

# Generating frequent itemsets with apriori
frequent_itemsets = apriori(df, min_support=0.3, use_colnames=True)

# Generating association rules with a minimum lift threshold of 1.2
rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1.2)

# Output results
print("Frequent Itemsets:")
print(frequent_itemsets)

print("\nAssociation Rules:")
print(rules)

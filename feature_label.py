
import numpy as np
feature_label = [np.array(['First Class', 'Same Day', 'Second Class', 'Standard Class'],
       dtype=object),
 np.array(['Consumer', 'Corporate', 'Home Office'], dtype=object),
 np.array(['Furniture', 'Office Supplies', 'Technology'], dtype=object),
 np.array(['Accessories', 'Appliances', 'Art', 'Binders', 'Bookcases',
        'Chairs', 'Copiers', 'Envelopes', 'Fasteners', 'Furnishings',
        'Labels', 'Machines', 'Paper', 'Phones', 'Storage', 'Supplies',
        'Tables'], dtype=object),
 np.array(['Critical', 'High', 'Low', 'Medium'], dtype=object)]

# for i in feature_label:
#     # print(i)
#     for j in i:
#         print(j)

print([item for sub_array in feature_label for item in sub_array])
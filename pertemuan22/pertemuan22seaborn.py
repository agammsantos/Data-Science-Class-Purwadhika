# pip install seaborn

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sn
sn.set(style='darkgrid') # menentukan style dari grafik seaborn

dataku=sn.load_dataset('flights') # mengambil set data dari github seaborn dataset
datapivot=dataku.pivot('month','year','passengers') # merubah tampilan data menjadi tabel relasi
print(type(dataku))

# sn.relplot(
#     x='year',
#     y='passengers',
#     data=dataku,
#     # kind='line',
#     hue='month',
#     size='month'
#     # style='month'
# )

# sn.barplot(
#     x='year',
#     y='passengers',
#     data=dataku,
#     # kind='line',
#     # kind='point,
#     # hue='month',
#     # size='month'
#     # style='month'
# )

# sn.catplot(
#     x='year',
#     y='passengers',
#     data=dataku,
#     kind='bar',
#     # kind='point',
#     hue='month'
#     # size='month'
#     # style='month'
# )

# sn.lmplot( # dapat menunjukkan margin of error
#     x='year',
#     y='passengers',
#     data=dataku,
#     hue='month'
# )

sn.swarmplot(x='year',y='passengers',data=dataku)
plt.xticks(rotation=90)
plt.savefig('seaborn.png')

# sn.heatmap(datapivot,cmap='hot_r') # plot heatmap dengan color mapping hot reverse
# sn.heatmap(datapivot,cmap='BuPu', annot=True, fmt='d') # plot heatmap dengan color mapping blue purple beserta annotasi nilai dan format digit


plt.show()
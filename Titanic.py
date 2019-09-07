import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 

dataset=pd.read_csv(r'C:\Users\USER\Desktop\Dataset\train.csv')

dataset.info()

sns.factorplot('Sex',data=dataset)

sns.factorplot('Pclass',data=dataset,hue='Sex')

def male_female_child(passenger):
    age,sex=passenger
    
    if age<16:
        return 'child'
    else:
        return sex
   
dataset['person']=dataset[['Age','Sex']].apply(male_female_child,axis=1)

dataset[0:10]
sns.factorplot('Pclass',data=dataset,hue='person')
dataset['Age'].hist(bins=70)

dataset['Age'].mean()

dataset['person'].value_counts()

fig=sns.FacetGrid(dataset,hue='Sex',aspect=4)
fig.map(sns.kdeplot,'Age',shade=True)
oldest=dataset['Age'].max()
fig.set(xlim=(0,oldest))
fig.add_legend()

fig=sns.FacetGrid(dataset,hue='person',aspect=4)
fig.map(sns.kdeplot,'Age',shade=True)
oldest=dataset['Age'].max()
fig.set(xlim=(0,oldest))
fig.add_legend()

fig=sns.FacetGrid(dataset,hue='Pclass',aspect=4)
fig.map(sns.kdeplot,'Age',shade=True)
oldest=dataset['Age'].max()
fig.set(xlim=(0,oldest))
fig.add_legend()



deck=dataset['Cabin'].head()
deck=dataset['Cabin'].dropna()
deck=head()

level=[]
for level in deck:
    levels.append(level[0])

cabin_df=DataFrame(levels)
cabin_df.column=['Cabin']
sns.factorplot('Cabin',data=cabin_df,palette='Winter_d')

sns.factorplot('Embarked',data=dataset,hue='Pclass',x_order=['C','Q','S'])
dataset.head()

dataset['Alone']=dataset.SibSp + dataset.Parch
dataset['Alone']

dataset['Alone'].loc[dataset['Alone']>0]='With Family'
dataset['Alone'].loc[dataset['Alone']==0]='Alone'
  
dataset.head()
sns.factorplot('Alone',data=dataset,palette='Blues')

generations=[10,20,40,60,80]
sns.implot('Age','Survived',hue='Pclass',data=dataset,palette='winter',x_bins=generations)

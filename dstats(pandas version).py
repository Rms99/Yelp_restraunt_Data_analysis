import pandas as pd
import sys
data = sys.argv[1]
city = sys.argv[2]
import pandas as pd
def restaurant_count(data,city):
    df=pd.read_csv(data)
    df1=df[df.categories.str.contains("Restaurants", case=False)].reset_index()
    df1['category']=pd.Series()
    df1.loc[df1.categories.str.contains('American'),'category'] = 'American'
    df1.loc[df1.categories.str.contains('Mexican'), 'category'] = 'Mexican'
    df1.loc[df1.categories.str.contains('Italian'), 'category'] = 'Italian'
    df1.loc[df1.categories.str.contains('Japanese'), 'category'] = 'Japanese'
    df1.loc[df1.categories.str.contains('Chinese'), 'category'] = 'Chinese'
    df1.loc[df1.categories.str.contains('Thai'), 'category'] = 'Thai'
    df1.loc[df1.categories.str.contains('Mediterranean'), 'category'] = 'Mediterranean'
    df1.loc[df1.categories.str.contains('French'), 'category'] = 'French'
    df1.loc[df1.categories.str.contains('Vietnamese'), 'category'] = 'Vietnamese'
    df1.loc[df1.categories.str.contains('Greek'),'category'] = 'Greek'
    df1.loc[df1.categories.str.contains('Indian'),'category'] = 'Indian'
    df1.loc[df1.categories.str.contains('Korean'),'category'] = 'Korean'
    df1.loc[df1.categories.str.contains('Hawaiian'),'category'] = 'Hawaiian'
    df1.loc[df1.categories.str.contains('African'),'category'] = 'African'
    df1.loc[df1.categories.str.contains('Spanish'),'category'] = 'Spanish'
    df1.loc[df1.categories.str.contains('Middle_eastern'),'category'] = 'Middle_eastern'
    df1=df1.dropna(axis=0, subset=['category'])
    del df1['categories']
    df1=df1.reset_index(drop=True)
    df1=df1.drop_duplicates(subset="business_id")
    df2=df1.groupby(["city", "category"],as_index=False).agg({"index":"count", "review_count":"sum", "stars":"mean"}).rename(columns={"index":"restaurant_number"})
    df2.city=df2.city.str.title()
    x=df2.loc[df2['city'] == city].sort_values(by="restaurant_number",ascending=False)
    for index, row in x.iterrows():
        print(row['category'],":", row["restaurant_number"])
    print("restaurantReviewDist:---------------")
    df3=df2.groupby("category",as_index=False).agg({"review_count":"sum", "stars":"mean"})
    df3.stars=df3.stars.round(1)
    df3=df3.sort_values("review_count", ascending=False).reset_index(drop=True)
    for index, row in df3.iterrows():
        print(row['category'],":",row['review_count'],":",round(row["stars"],1))
    import matplotlib.pyplot as plt
    df4=df3.head(10)
    fig = plt.figure()
    ax = fig.add_axes([0,0,1,1])
    ax.bar(df4.category,df4.review_count)
    ax.set_xlabel("Category")
    ax.set_ylabel("Number of Restaurants")
    plt.show()

restaurant_count(data,city)


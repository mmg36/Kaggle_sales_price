import pandas as pd
import plotly.express as px
import numpy as np


def test_results():
    print("Overview of the data below: \n")
    print(sales_train_df.head())
    print("Some descriptive statistics below: \n")
    print(sales_train_df.describe())


def analysis():
    corr_1 = sales_train_df['item_cnt_day'].corr(sales_train_df['item_price'])
    print(sales_train_df.corr())
    df = sales_train_df[(sales_train_df['item_price'] > 15000) & (sales_train_df['item_price'] < 35000)]
    df = df.sort_values(by=['shop_id'])
    fig = px.scatter(df, x='item_price', y='date_block_num', facet_col='shop_id', color = 'item_id',
                     facet_col_wrap=10, facet_row_spacing=0.01, facet_col_spacing=0.01)
    fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='LightPink')
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='LightPink')
    fig.show()


if __name__ == '__main__':
    sales_train_df = pd.read_csv("./raw-data/sales_train.csv")
    analysis()
    #test_results()
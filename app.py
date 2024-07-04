import streamlit as st
import pickle
import pandas as pd
products_list=pickle.load(open('data1.pkl','rb'))
similarity=pickle.load(open('similarity.pkl','rb'))

products_names=products_list['Name'].values
st.title('Product recommender system')

# def recommend(product):
#     item_index =products_list[products_list['Name']==product].index[0]
#     similar_items = list(enumerate(cosine_similarities_content[item_index]))
#     similar_items = sorted(similar_items, key=lambda x:x[1], reverse=True)
#     top_similar_items = similar_items[1:10]
#     recommended_items_indics = [x[0] for x in top_similar_items]
#     recommended_products=[]
#     for i in top_similar_items:
#         recommended_products.append(products_list.iloc[recommended_items_indics][['Name','ReviewCount','Brand']])
#     return recommended_products
    
def recommend(product):
    try:
        item_index = products_list[products_list['Name'] == product].index[0]
        similar_items = list(enumerate(similarity[item_index]))
        similar_items = sorted(similar_items, key=lambda x: x[1], reverse=True)
        top_similar_items = similar_items[1:10]
        
        recommended_products = []
        for i in top_similar_items:
            recommended_products.append(products_list.iloc[i[0]][['Name', 'ReviewCount', 'Brand']])
        
        return recommended_products
    except Exception as e:
        st.error(f"Error in recommendation function: {e}")
        return []

selected_product = st.selectbox(
    "What would you like to purchase?",
    products_names)

st.write("You selected:", selected_product)

if st.button('Recommend'):
    recommendations=recommend(selected_product)
    for i in recommendations:
        st.write(i)
    
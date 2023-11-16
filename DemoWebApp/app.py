from flask import Flask,render_template,redirect, url_for
from flask import Flask, escape, request,flash
import requests
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import nltk
import recommendation as r
import pandas as pd
from textblob import TextBlob
import ast
import spacyRecommendation as sr
from flask import session

# recommendation based oon cosine similarity:

selected_brands_df_curu=pd.read_csv('data.csv')
username_list=list(selected_brands_df_curu.Username)

selected_brands_df_curu['Sentiment'] = selected_brands_df_curu['Reviews'].apply(lambda x: TextBlob(str(x)).sentiment.polarity)  


aggregated_df = selected_brands_df_curu.groupby(['Username', 'ProductName']).agg({'Sentiment': 'mean', 'Ratings': 'mean'}).reset_index()

sentiment_weight = 0.7  # This implies a 0.3 weight for Ratings

aggregated_df['WeightedScore'] = aggregated_df['Sentiment'] * sentiment_weight + aggregated_df['Ratings'] * (1 - sentiment_weight)

interaction_matrix = aggregated_df.pivot(index='Username', columns='ProductName', values='WeightedScore').fillna(0)

user_similarity = cosine_similarity(interaction_matrix)

user_similarity_df = pd.DataFrame(user_similarity, index=interaction_matrix.index, columns=interaction_matrix.index)

# recommendation based on most common skin concern:
data=pd.read_csv('fdata.csv')
username_list=list(data.Username)

processedData=pd.read_csv('processed.csv')
processedData['finalprocessed_set']=processedData['finalprocessed'].apply(lambda x: set(ast.literal_eval(x)))
flattened_list = {term for terms_set in processedData['finalprocessed_set'] for term in terms_set}

def getuser_reviwed_products(userName):
    prod_reviewed=set(selected_brands_df_curu[selected_brands_df_curu['Username']==userName]['ProductName'])
    return prod_reviewed

def get_product_data_dict(spacy_recommended_products):
    product_data_dict = {}
    # userName = session.get('userName')  
    for product_name in spacy_recommended_products:
        row = processedData[processedData['ProductName'] == product_name].iloc[0]
        final_processed = row['finalprocessed_set']
        product_data_dict[product_name] = final_processed
    return product_data_dict

reviewed_prod_skinConcern=set()
spacy_recommended_products = []

app=Flask(__name__)
app.secret_key = 'supersecretkey123'
@app.route('/', methods=['POST', 'GET'])
@app.route('/home', methods=['POST', 'GET'])

def home():
    global spacy_recommended_products
    
    # selected_skin_concerns = []

    if request.method == 'POST':
        # Check if 'userName' is in the form data
        userName = request.form.get('userName')
        if not userName:
            userName = session.get('userName')
        
        # selected_skin_concerns = []
        # Check if 'skinConcerns' is in the form data
        selected_skin_concerns = request.form.getlist('skinConcerns')

        if ((userName) and (selected_skin_concerns==[])) :
            selected_skin_concerns = []
            session['userName'] = userName
            cos_recommended_products = r.recommend_products(userName, user_similarity_df, interaction_matrix, n_recommendations=5)
            skinConcern_set, sp_recommended_products_df = sr.spacy_recommend_products(userName, data, processedData, 5)
            spacy_recommended_products = list(sp_recommended_products_df['ProductName'])
            reviewed_prod_skinConcern.update(skinConcern_set)
            return render_template('home2.html', userName=userName,
                                   prod_reviewed=getuser_reviwed_products(userName),
                                   cos_recommended_products=cos_recommended_products,
                                   spacy_recommended_products=spacy_recommended_products)

        elif selected_skin_concerns:            
            # reviewed_prod_skinConcern.update(selected_skin_concerns)
            sp_recommended_products_df = sr.skinconcern_recommend_products(selected_skin_concerns, processedData, 5)
            spacy_recommended_products_new = list(sp_recommended_products_df['ProductName'])
            product_data_dict = get_product_data_dict(spacy_recommended_products_new)
            text1="User Profile Skin concerns"
            
            return render_template('spacy.html', text1=text1,reviewed_prod_skinConcern=selected_skin_concerns,
                                   product_data_dict=product_data_dict)

    return render_template('home.html', username_list=username_list, flattened_list=flattened_list)




@app.route('/spacy')
def key():  
    product_data_dict = get_product_data_dict(spacy_recommended_products)
    text1="Reviewed Products Skin Concerns"
    
    return render_template('spacy.html', text1=text1,reviewed_prod_skinConcern=reviewed_prod_skinConcern,product_data_dict=product_data_dict)

if __name__ == '__main__':
    app.run(debug=True)
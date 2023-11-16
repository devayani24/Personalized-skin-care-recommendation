import pandas as pd

#from textblob import TextBlob 
 

def recommend_products(target_user, user_similarity_df, interaction_matrix, n_recommendations=5):

    if target_user not in user_similarity_df.index:

        return []


    similar_users = user_similarity_df.loc[target_user].sort_values(ascending=False)[1:].index

    target_user_rated_products = set(interaction_matrix.loc[target_user][interaction_matrix.loc[target_user] > 0].index)


    recommendations = {}

    for user in similar_users:

        user_rated_products = set(interaction_matrix.loc[user][interaction_matrix.loc[user] > 0].index)

        recommendable = user_rated_products - target_user_rated_products

        for product in recommendable:

            if product not in recommendations:

                recommendations[product] = 0

            recommendations[product] += user_similarity_df.loc[target_user, user] * interaction_matrix.loc[user, product]


    sorted_recommendations = sorted(recommendations.items(), key=lambda x: x[1], reverse=True)[:n_recommendations]

    return [product for product, score in sorted_recommendations]

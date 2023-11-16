import ast
def spacy_recommend_products(target_user,data,processedData,n_recommendation):
    prod_reviewed=list(set(data[data['Username']==target_user].ProductName))
    processed=(processedData[processedData.ProductName.isin(prod_reviewed)]['finalprocessed_set'])
    processed_set = set()
    for s in processed:
        processed_set |= s
    
    common_counts = []
    df=processedData[['ProductName','finalprocessed_set']]
    for row_set in df['finalprocessed_set']:
        common_count = len(processed_set.intersection((row_set)))
        common_counts.append(common_count)

    # Add the common counts to the DataFrame
    df['common_items_count'] = common_counts

    sorted_df=df.sort_values(by='common_items_count', ascending=False)
    # Select the top 3 rows
    top_n_recommendation_products = sorted_df.head(n_recommendation)
    return  processed_set,top_n_recommendation_products

def skinconcern_recommend_products(skinConcer_list,processedData,n_recommendation):
    skinConcern_set=set(skinConcer_list)
    common_counts = []
    df=processedData[['ProductName','finalprocessed_set']]
    for row_set in df['finalprocessed_set']:
        common_count = len(skinConcern_set.intersection((row_set)))
        common_counts.append(common_count)

    # Add the common counts to the DataFrame
    df['common_items_count'] = common_counts

    sorted_df=df.sort_values(by='common_items_count', ascending=False)
    # Select the top 3 rows
    top_n_recommendation_products = sorted_df.head(n_recommendation)
    return top_n_recommendation_products
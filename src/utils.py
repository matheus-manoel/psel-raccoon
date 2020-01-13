from functools import partial, reduce
from operator import itemgetter, gt
from datetime import datetime


def filter_by_keywords_in_field_value(list_dict, field, keywords):
    return filter(lambda x: any(keyword in x[field] for keyword in keywords), list_dict)

filter_by_promocao_in_title = partial(
    filter_by_keywords_in_field_value, field='title', keywords=['promocao']
)

filter_by_instagram_cpc_in_media = partial(
    filter_by_keywords_in_field_value, field='media', keywords=['instagram_cpc']
)

filter_by_paid_medias = partial(
    filter_by_keywords_in_field_value,
    field='media',
    keywords=['google_cpc', 'facebook_cpc','instagram_cpc']
)

def sort_by_multiple_fields(list_dict, fields):
    return sorted(list_dict, key=itemgetter(*fields))

def map_to_fields(list_dict, fields):
    return map(lambda x: {field: x[field] for field in fields}, list_dict)

def change_field_name(list_dict, old_name, new_name):
    return map(lambda x: {**x, **{new_name: x.pop(old_name)}}, list_dict)

def remove_entries_with_duplicated_field_value(list_dict, field):
    return list({
        dict_['product_id']: dict_
        for dict_ in list_dict
    }.values())

sort_by_price_and_product_id = partial(
    sort_by_multiple_fields, fields=['price', 'product_id']
)

map_to_product_id_and_price = partial(
    map_to_fields, fields=['product_id', 'price']
)

map_to_post_id_and_price = partial(
    map_to_fields, fields=['post_id', 'price']
)

change_price_to_price_field = partial(
    change_field_name, old_name='price', new_name='price_field'
)

remove_entries_with_duplicated_product_id = partial(
    remove_entries_with_duplicated_field_value, field='product_id'
)

def filter_by_field_value_comparation(list_dict, field, operator, n_to_compare):
    return filter(lambda x: operator(float(x[field]), n_to_compare), list_dict)

filter_by_likes_greater_than_700 = partial(
    filter_by_field_value_comparation, field='likes', operator=gt, n_to_compare=700
)

def _is_date_a_match(date_string, days, months, years):
    return (datetime.strptime(date_string, '%d/%m/%Y').day in days and
                datetime.strptime(date_string, '%d/%m/%Y').month in months and
                datetime.strptime(date_string, '%d/%m/%Y').year in years)

def filter_by_date(list_dict, days, months, years, datetime=datetime):
    return filter(lambda x: _is_date_a_match(x['date'], days, months, years), list_dict)

def sum_values_by_field(list_dict, field):
    return reduce(lambda a, b: a + float(b[field]), list_dict, 0)

filter_by_may_2019 = partial(
    filter_by_date, days=[*range(1, 32)], months=[5], years=[2019]
)

sum_likes = partial(
    sum_values_by_field, field='likes'
)

import requests
import json

from src import (
        get_unrepeated_ordered_promo_products_by_price_and_id,
        get_ordered_insta_posts_over_700_likes,
        get_likes_sum_of_paid_medias_posts_in_may_2019,
        get_ordered_product_errors
)


if __name__ == '__main__':
    posts_req = requests.get('https://us-central1-psel-clt-ti-junho-2019.cloudfunctions.net/psel_2019_get')
    posts = posts_req.json()['posts']
    d_posts_req = requests.get('https://us-central1-psel-clt-ti-junho-2019.cloudfunctions.net/psel_2019_get_error')
    d_posts = d_posts_req.json()['posts']

    req_answer = requests.post(
        'https://us-central1-psel-clt-ti-junho-2019.cloudfunctions.net/psel_2019_post',
        data=json.dumps({
            'full_name': 'Matheus Cabral Manoel',
            'email': 'matheuscmanoel@gmail.com',
            'code_link': 'https://github.com/matheus-manoel/psel-raccoon',
            'response_a': get_unrepeated_ordered_promo_products_by_price_and_id(posts),
            'response_b': get_ordered_insta_posts_over_700_likes(posts),
            'response_c': get_likes_sum_of_paid_medias_posts_in_may_2019(posts),
            'response_d': get_ordered_product_errors(d_posts)
        }),
        headers={'content-type': 'application/json'}
    )

    print(req_answer.json())

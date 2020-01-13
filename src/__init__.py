from .utils import (
        filter_by_promocao_in_title,
        change_price_to_price_field,
        sort_by_price_and_product_id,
        map_to_product_id_and_price,
        remove_entries_with_duplicated_product_id,
        filter_by_likes_greater_than_700,
        filter_by_instagram_cpc_in_media,
        map_to_post_id_and_price,
        sum_likes,
        filter_by_may_2019,
        filter_by_paid_medias
)


def get_unrepeated_ordered_promo_products_by_price_and_id(posts):
    promotion_posts = [*filter_by_promocao_in_title(posts)]
    return [
        *change_price_to_price_field(
            sort_by_price_and_product_id(
                map_to_product_id_and_price(
                    remove_entries_with_duplicated_product_id(promotion_posts)
                )
            )
        )
    ]

def get_ordered_insta_posts_over_700_likes(posts):
    insta_cpc_posts_with_over_700_likes = [
        *filter_by_likes_greater_than_700(
            filter_by_instagram_cpc_in_media(posts)
        )
    ]
    return [
        *change_price_to_price_field(
            map_to_post_id_and_price(
                sort_by_price_and_product_id(insta_cpc_posts_with_over_700_likes)
            )
        )
    ]

def get_likes_sum_of_paid_medias_posts_in_may_2019(posts):
    return int(
        sum_likes(
            filter_by_may_2019(
                filter_by_paid_medias(posts)
            )
        )
    )

def _is_price_diff_in_control(products_control, post):
    return (products_control.get(post['product_id']) and
                products_control.get(post['product_id']) != post['price'])

def _add_product_and_price_to_control(products_control, post):
    return {**products_control, post['product_id']: post['price']}

def get_ordered_product_errors(posts):
    products_control = {}
    products_with_error = set()

    for post in posts:
        if _is_price_diff_in_control(products_control, post):
            products_with_error = products_with_error.union({post['product_id']})
        else:
            products_control = _add_product_and_price_to_control(products_control, post)

    return sorted([*products_with_error])

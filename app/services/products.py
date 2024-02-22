import csv

dataset_path = 'dataset.csv'

def load_data():
    with open(dataset_path, 'r') as file:
        csv_reader = csv.DictReader(file)
        return list(csv_reader)


def get_top_rated_products(data):
    filtered_data = [product for product in data if product.get('rating') and product.get('rating_count') and product['rating'].replace('.', '', 1).isdigit() and product['rating_count'].replace(',', '').isdigit() and int(product['rating_count'].replace(',', '')) >= 10]
    sorted_data = sorted(filtered_data, key=lambda x: float(x['rating']), reverse=True)
    top_5_products = sorted_data[:5]
    return top_5_products


def search_products_by_category(data, category):
    products_in_category = []
    for product in data:
        if product.get('category') == category:
            product_details = {
                'product_name': product.get('product_name'),
                'rating': product.get('rating'),
                'discounted_price': product.get('discounted_price')
            }
            products_in_category.append(product_details)
    return products_in_category


def calculate_average_discount_by_category(data):
    category_discounts = {}
    for product in data:
        category = product.get('category')
        discount_percentage = product.get('discount_percentage')
        if category and discount_percentage:
            if category not in category_discounts:
                category_discounts[category] = []
            discount = float(discount_percentage.replace('%', ''))
            category_discounts[category].append(discount)
    average_discounts = {}
    for category, discounts in category_discounts.items():
        if discounts:
            average_discount = sum(discounts) / len(discounts)
            average_discounts[category] = round(average_discount, 2)
    return average_discounts
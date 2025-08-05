{
    'name': 'Product Cost Price History',
    'version': '17.0',
    'summary': 'Track and view historical product cost prices from different suppliers with filter and limit options.',
    'description': """
This module useful to show the history of the cost price for the product, you can also track the history of 
the cost price of the product for different suppliers. Easy to find rates given to you by the supplier in the
past for that product.
""",
    'category': 'purchase / account',
    'sequence': 2,
    'author': 'Namah Softech Private Limited',
    'contributors': 'Mohit Nare',
    'price': 14.99,
    'currency': 'USD',
    'website': 'http://namahsoftech.com/',
    'license': 'OPL-1',
    'support': 'support@namahsoftech.com',
    'depends': ['purchase', 'account'],
    'data': [
        'views/product_purchase_history_view.xml',
        'views/purchase_config_view.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'images': ['static/description/img/banner.png'],
}

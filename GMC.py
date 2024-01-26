from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Assuming you have credentials set up and API key obtained
# Replace 'your_api_key' with your actual API key
api_key = 'your_api_key'
service = build('content', 'v2', developerKey=api_key)

def insert_product(product):
    try:
        request = service.products().insert(merchantId='your_merchant_id', body=product)
        response = request.execute()
        print("Product inserted successfully. Product ID:", response['id'])
    except HttpError as err:
        print("Error inserting product:", err)

# Assuming your Price and ProductShipping classes are defined elsewhere
class Price:
    def __init__(self):
        self.value = None
        self.currency = None

class ProductShipping:
    def __init__(self):
        self.price = None
        self.country = None
        self.service = None

class Product:
    def __init__(self):
        self.offerId = None
        self.title = None
        self.description = None
        self.link = None
        self.imageLink = None
        self.contentLanguage = None
        self.targetCountry = None
        self.channel = None
        self.availability = None
        self.condition = None
        self.googleProductCategory = None
        self.gtin = None
        self.price = None  # Assuming Price object
        self.shipping = None  # Assuming ProductShipping object

# Create Product instance
product = Product()
product.offerId = "book123"
product.title = "A Tale of Two Cities"
product.description = "A classic novel about the French Revolution"
product.link = "http://my-book-shop.com/tale-of-two-cities.html"
product.imageLink = "http://my-book-shop.com/tale-of-two-cities.jpg"
product.contentLanguage = "en"
product.targetCountry = "GB"
product.channel = "online"
product.availability = "in stock"
product.condition = "new"
product.googleProductCategory = "Media > Books"
product.gtin = "9780007350896"

# Create Price instance for product
price = Price()
price.value = "2.50"
price.currency = "GBP"
product.price = price

# Create ProductShipping instance for product
shipping = ProductShipping()
shipping.price = Price()
shipping.price.value = "0.99"
shipping.price.currency = "GBP"
shipping.country = "GB"
shipping.service = "Standard shipping"
product.shipping = shipping

# Insert the product to Google Merchant
insert_product(product)

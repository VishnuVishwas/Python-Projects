from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home_page():
    products = [{'name': 'Iphone', 'description': 'Meet the new iPhone 15 Pro and iPhone 15. Buy now. Designed to make a difference. Get to know iPhone 15. All-day battery life. iOS 17. 5G', 'price': '100'},
    {'name': 'OnePlus 12', 'description': 'Pro-Level Hasselblad Camera System: Primary 50MP Sony\'s LYT-808 with OIS - 64 MP 3X Periscope Telephoto for studio-level portraits - 48 MP Ultra-wide 114° Fov', 'price': '200'},
    {'name': 'Redmi 12 5G', 'description': 'Snapdragon 4 Gen 2 Mobile Platform : Power efficient 4nm architecture | 12GB of RAM including 6GB Virtual', 'price': '300'},
    {'name': 'iQOO Z7 Pro 5G', 'description': 'Dimensity 7200 5g processor based on the latest 4nm energy-efficient process', 'price': '200'},
    {'name': 'Samsung Galaxy M04', 'description': 'Powerful MediaTek Helio P35 Octa Core 2.3GHz with Android 12,One UI Core 4.1', 'price': '300'},
    {'name': 'realme narzo 60 5G', 'description': 'Immerse yourself in a smooth and responsive visual experience with our vibrant 90Hz Super AMOLED display. Enjoy seamless scrolling, fluid animations, and razor-sharp image quality, bringing your content to life like never before. Whether you\'re gaming, browsing, or watching videos, every interaction will be a delight for your eyes.', 'price': '400'}
    ]
    category = 'Mobiles'

    return render_template('index.html', category=category, products=products)

@app.route('/product')
def product_page():
    return render_template('product.html')


if __name__ == '__main__':
    app.run(debug=True)
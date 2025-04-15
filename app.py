import os
import time
import numpy as np
from flask import Flask, request, render_template
from tensorflow.keras.applications import EfficientNetB0
from tensorflow.keras.applications.efficientnet import preprocess_input, decode_predictions
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from tensorflow.keras.preprocessing import image
from PIL import Image

# Initialize Flask App
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'

# Load EfficientNetB0 model
model = EfficientNetB0(weights='imagenet')

# Function to classify the uploaded image
def classify_image(img_path):
    try:
        img = Image.open(img_path).convert('RGB')
        img = img.resize((224, 224))
        img_array = np.array(img)
        img_array = np.expand_dims(img_array, axis=0)
        img_array = preprocess_input(img_array)

        predictions = model.predict(img_array)
        label = decode_predictions(predictions)
        item_name = label[0][0][1]
        print(f"✅ Classified Item: {item_name}")
        return item_name
    except Exception as e:
        print(f"❌ Error in classification: {e}")
        return None

# Function to scrape all prices from a website and return the lowest one
def scrape_price(url, platform):
    print(f"🚀 Scraping started for {platform}: {url}")
    try:
        options = Options()
        options.add_argument("--headless")
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        driver.get(url)
        time.sleep(3)

        soup = BeautifulSoup(driver.page_source, 'html.parser')
        driver.quit()

        prices = []
        if platform == "Amazon":
            price_tags = soup.find_all("span", {"class": "a-price-whole"})
        elif platform == "Flipkart":
            price_tags = soup.find_all("div", {"class": ["Nx9bqj", "Nx9bqj _4b5DiR"]})
        elif platform == "Google Shopping":
            price_tags = soup.find_all("span", class_="a8Pemb OFFNJ")
        elif platform == "Meesho":
            price_tags = soup.find_all("h5", class_="sc-eDvSVe dwCrSh")
        elif platform == "H&M":
            price_tags = soup.find_all("span", class_="aeeCde ac3d9e")
        elif platform == "Fiorella":
            price_tags = soup.find_all("span", class_="price")
        else:
            price_tags = []

        for tag in price_tags:
            price_text = tag.get_text().replace(",", "").strip().replace("₹", "").strip()
            try:
                prices.append(float(price_text))
            except ValueError:
                continue

        if prices:
            lowest_price = min(prices)
            print(f"✅ Lowest price from {platform}: ₹{lowest_price}")
            return lowest_price, url
        else:
            print(f"❌ No valid price found on {platform}")
            return None, url
    except Exception as e:
        print(f"❌ Error scraping {platform}: {e}")
        return None, url

# Functions to fetch prices from specific platforms
def fetch_price_amazon(item):
    return scrape_price(f"https://www.amazon.in/s?k={item}", "Amazon")

def fetch_price_flipkart(item):
    return scrape_price(f"https://www.flipkart.com/search?q={item}", "Flipkart")

def fetch_price_google_shopping(item):
    return scrape_price(f"https://www.google.com/search?tbm=shop&q={item}", "Google Shopping")

def fetch_price_meesho(item):
    return scrape_price(f"https://www.meesho.com/search?q={item}", "Meesho")

def fetch_price_hm(item):
    return scrape_price(f"https://www2.hm.com/en_in/search-results.html?q={item}", "H&M")

def fetch_price_fiorella(item):
    return scrape_price(f"https://www.fiorella.com/search?q={item}", "Fiorella")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files or request.files['file'].filename == '':
        return "No file uploaded"

    file = request.files['file']
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(filepath)
    print(f"✅ File uploaded: {filepath}")

    # Image classification
    item_name = classify_image(filepath)
    if not item_name:
        return "Error in image classification"

    # Fetch prices from platforms
    prices = {
        "Amazon": fetch_price_amazon(item_name),
        "Flipkart": fetch_price_flipkart(item_name),
        "Google Shopping": fetch_price_google_shopping(item_name),
        "Meesho": fetch_price_meesho(item_name),
        "H&M": fetch_price_hm(item_name),
        "Fiorella": fetch_price_fiorella(item_name),
    }

    # Filter out platforms where no price was found
    filtered_prices = {k: v for k, v in prices.items() if v[0] is not None}

    if not filtered_prices:
        return "No prices found for the item. Try another image."

    # Find the lowest price
    best_platform = min(filtered_prices.items(), key=lambda x: x[1][0])

    return render_template(
        'result.html',
        item=item_name,
        prices=filtered_prices,
        best_platform=best_platform,
        filename=file.filename
    )

if __name__ == "__main__":
    app.run(debug=True)

# 🛒✨ Price Comparison Application  
A smart AI-powered platform that helps users **upload a product image**, automatically **identify the item**, and fetch **best prices across multiple e-commerce websites** like Amazon, Flipkart, Ajio, Myntra, etc.

---

## 📌 **📖 Project Overview**

The **Price Comparison Application** is built to simplify online shopping.  
When a user uploads a product image:

1. 🧠 **AI Model identifies the item name**  
2. 🌐 The system **scrapes multiple e-commerce platforms**  
3. 💶 Compares prices  
4. 🔗 Provides the **best available price** along with the **direct product link**

This helps users save time, effort, and money while shopping online.

---

## 🚀 **✨ Key Features**

✔ Upload any product image  
✔ AI-based product identification  
✔ Fetch price details from multiple websites  
✔ Compare prices and display the cheapest product  
✔ Clean UI using HTML templates  
✔ Saves uploaded images inside static/uploads  
✔ Easy to run locally

---

## 🛠️ **🧰 Technologies Used**

| Technology | Purpose |
|-----------|---------|
| 🐍 **Python** | Backend logic |
| 🔥 **Flask** | Web framework |
| 🤖 **TensorFlow / VGG16** | Image recognition (Transfer Learning) |
| 🌐 **BeautifulSoup / Requests** | Web scraping |
| 🎨 **HTML, CSS** | Frontend & UI |
| 📦 **OpenCV** | Image processing |

---

## 📁 **📂 Project File Structure**

```

Price-comparison-Application/
│
├── app.py                     # Main Flask application
│
├── static/
│   └── uploads/               # Uploaded images stored here
│
└── templates/
├── index.html             # Upload page
└── result.html            # Price result display page

```

---

## ▶️ **🧪 How to Run the Project Locally**

### **1️⃣ Clone the Repository**
```

git clone [https://github.com/07bhuvana/Price-comparison-Application.git](https://github.com/07bhuvana/Price-comparison-Application.git)
cd Price-comparison-Application

```

### **2️⃣ Install Dependencies**
Make sure you have Python installed.

```

pip install -r requirements.txt

```

If you don’t have a requirements file, install manually:

```

pip install flask tensorflow opencv-python requests beautifulsoup4

```

### **3️⃣ Start the Server**
```

python app.py

```

### **4️⃣ Open in Browser**
Go to:

```

[http://127.0.0.1:5000/](http://127.0.0.1:5000/)

```

Now you can upload product images and get the best price!

---

## 🌱 **Future Enhancements**

✨ Add real-time price update  
✨ Add more e-commerce sites  
✨ Add mobile app support  
✨ Add OCR to read product text from images  
✨ Add currency converter  
✨ Add user history & login system  

---

## 🏁 **💡 Conclusion**

This project demonstrates how **AI + Web Scraping + Flask** can be combined to build a smart and practical real-world application. It helps users compare prices instantly and make better shopping decisions.

---

### ❤️ Developed by *Bhuvanaeswari N*
```

---


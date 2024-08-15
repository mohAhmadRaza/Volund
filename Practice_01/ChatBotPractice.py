import streamlit as st
import openai as OpenAI
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set up OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

faqs = {
    "What is this chatbot about?": "This chatbot is designed to assist users with information about our products and services.",
    "Can I contact customer support through this chatbot?": "No, You cannot, but if you want to contact with customer support, you can Email at the given emails.",
    "Why am I seeing an error message?": "You are getting this error because you are pasting instead of typing, don't paste.",
    "Is there a cost to use this service?": "No, this service is free to use.",
    "What are the operating hours of customer support?": "Customer Support is not availaible, contact us on the provided emails.",
    "Is there a warranty for Product you advising?": "No, our task is just to show you the products details and way to buy, that sit."
}

# Custom CSS for styling FAQs
custom_css = """
<style>
.faq-container {
    background-color: white;
    padding: 20px;
    margin-bottom: 10px;
    border-radius: 5px;
}

.faq-answer {
    font-color : #000066;
    font-size: 16px;
    line-height: 1.5;
}

.initial-message {
    color:  black;
    padding: 5px;  /* Padding around the content */
    font-size: 17px;  /* Larger font size */
    line-height: 1.5;  /* Slightly increased line height for readability */
    text-align : center;
    margin-bottom : 10px;
    margin-top : 10px;
}

.title {
    font-color:  #000066;
    font-size: 30px;  /* Larger font size */
    font-weight: bold;
    margin-bottom : -35px;
}

.subtitle {
    color:  #FFF2D7;
    font-size: 25px;  /* Larger font size */
    margin-bottom : 5px;
}
</style>
"""

# Render FAQs with custom HTML and CSS
st.markdown(custom_css, unsafe_allow_html=True)

# Add FAQ section to sidebar
f = "FAQs"
st.sidebar.markdown(f"<div class='title'>{f}", unsafe_allow_html=True)

# Create a select box or list of FAQ questions
selected_faq = st.sidebar.selectbox(" ", list(faqs.keys()))

# Display selected FAQ answer in the main content area
if selected_faq:
    st.sidebar.title(selected_faq)
    st.sidebar.markdown(f"<div class='faq-container'><div class='faq-answer'>{faqs[selected_faq]}</div></div>", unsafe_allow_html=True)
else:
    st.sidebar.write("Select an FAQ question from the sidebar")


def initial_message():
    return "Hi, I am Volund. Your AI Partner to help make an informed decision to buy anything. Let's get to know you a bit before looking into your product."


def gather_user_information(country, city, product, brand, budget):
    user_input = ", ".join([country, city, product, brand, budget])

    # Start a chat session (model selection might be handled differently)
    prompt = f"""
    You are a product assistant, skilled in explaining product details alongwith prices, website hyperlinks and brands.
    Generate detailed fictional product information for {product} within a budget of {budget}. 
    Include the model, price, color, posted date, and website name. Ensure results are 
    formatted in a descriptive, list-based format with clear and clickable hyperlinks. 
    Assume the information is from the last 2 months and within the user's budget.Format the response in a descriptive, list-based format with clear and clickable hyperlinks."""

    completion = client.completion.create(
        model="gpt-3.5-turbo-1106",
        prompt=prompt,
        max_tokens=150
    )

    return completion.choices[0].text.strip()

# Streamlit UI components
st.markdown("""
<div style="background-color: #000066; text-align: center; padding: 10px;border-radius : 5px">
  <h1 style="color: white; font-size: 70px; margin-bottom: -40px;">Volund</h1>
  <h2 style="color: white; font-size: 20px; margin-top: 5px;">An AI chatbot</h2>
</div>
""", unsafe_allow_html=True)


# Display the initial message
st.markdown(f"<div class= 'initial-message'>{initial_message()}", unsafe_allow_html=True)

# Input fields
country = st.text_input("What country are you from?")
city = st.text_input("Which city do you want to buy your product in?")
product = st.selectbox("What are you looking to purchase today?", ['iPhone 14', 'Samsung Galaxy S22', 'MacBook Pro',
                                                                     'Dell XPS 13', 'Sony WH-1000XM4', 'Google Pixel 6',
                                                                     'OnePlus 10 Pro', 'Xiaomi Mi 11', "iPhone 14",
                                                                     "Samsung Galaxy S22", "Google Pixel 7",
                                                                     "OnePlus 9",
                                                                     "Sony Xperia 5", "Huawei P50", "Xiaomi Mi 11",
                                                                     "Oppo Find X3", "Nokia 8.3", "Asus ROG Phone 5",
                                                                     "MacBook Pro", "Dell XPS 13", "HP Spectre x360",
                                                                     "Lenovo ThinkPad X1", "Microsoft Surface Laptop 4",
                                                                     "Acer Swift 3", "Asus ZenBook 14",
                                                                     "Razer Blade 15",
                                                                     "LG Gram 17", "Samsung Galaxy Book Pro",
                                                                     "Sony WH-1000XM4", "Bose QuietComfort 35 II",
                                                                     "Apple AirPods Pro", "JBL Charge 5",
                                                                     "Anker Soundcore Flare 2", "Beats Pill+",
                                                                     "Marshall Stanmore II", "UE Boom 3", "Sonos One",
                                                                     "Harman Kardon Onyx Studio 6",
                                                                     "Canon Pixma TR150", "HP Envy 6055",
                                                                     "Epson EcoTank ET-4760", "Brother HL-L2350DW",
                                                                     "Samsung Xpress M2020W", "Xerox Phaser 6510",
                                                                     "Lexmark MB2236adw", "Dell E310dw",
                                                                     "Kyocera Ecosys P5026cdw", "Ricoh SP 330DN",
                                                                     "Apple Watch Series 7", "Samsung Galaxy Watch 4",
                                                                     "Garmin Fenix 6", "Fitbit Charge 5",
                                                                     "Fossil Gen 5",
                                                                     "Huawei Watch GT 2", "Amazfit Bip U Pro",
                                                                     "Suunto 9",
                                                                     "TicWatch Pro 3", "Withings Steel HR",
                                                                     "Sony Alpha a7 III", "Canon EOS R5", "Nikon Z6 II",
                                                                     "Fujifilm X-T4", "Panasonic Lumix S5",
                                                                     "Olympus OM-D E-M10 Mark IV", "Leica Q2",
                                                                     "GoPro Hero9 Black", "DJI Osmo Pocket 2",
                                                                     "Insta360 One X2",
                                                                     "iPad Pro", "Samsung Galaxy Tab S7",
                                                                     "Microsoft Surface Pro 7", "Amazon Fire HD 10",
                                                                     "Lenovo Tab P11 Pro", "Huawei MatePad Pro",
                                                                     "Xiaomi Pad 5", "Asus ROG Flow X13",
                                                                     "Acer Chromebook Spin 713", "Dell Latitude 9510",
                                                                     "Logitech MX Master 3", "Razer DeathAdder V2",
                                                                     "Corsair K95 RGB Platinum", "SteelSeries Apex Pro",
                                                                     "Apple Magic Keyboard",
                                                                     "Microsoft Sculpt Ergonomic Keyboard",
                                                                     "HP Omen Sequencer", "Asus ROG Claymore II",
                                                                     "Logitech G Pro X Superlight",
                                                                     "HyperX Pulsefire Haste",
                                                                     "NVIDIA GeForce RTX 3080", "AMD Radeon RX 6800 XT",
                                                                     "Intel Core i9-11900K", "AMD Ryzen 9 5900X",
                                                                     "ASUS ROG Strix X570-E", "Gigabyte AORUS Master",
                                                                     "Corsair Vengeance LPX 32GB",
                                                                     "Samsung 970 EVO Plus 1TB",
                                                                     "Seagate Barracuda 4TB",
                                                                     "Western Digital Black SN850",
                                                                     "Oculus Quest 2", "Sony PlayStation 5",
                                                                     "Microsoft Xbox Series X", "Nintendo Switch OLED",
                                                                     "Valve Index", "HTC Vive Pro 2",
                                                                     "Razer Blade Stealth 13", "Alienware m15 R4",
                                                                     "MSI GS66 Stealth", "Gigabyte Aero 15",
                                                                     "iPhone 14",
                                                                     "Samsung Galaxy S22", "MacBook Pro", "Dell XPS 13",
                                                                     "Sony WH-1000XM4",
                                                                     "PlayStation 5", "Xbox Series X", "Apple Watch",
                                                                     "Kindle Paperwhite", "GoPro Hero 10",
                                                                     "Nike Air Max", "Adidas Ultraboost",
                                                                     "Levi's 501 Jeans",
                                                                     "Ray-Ban Sunglasses", "Fitbit Charge 5",

                                                                     "AirPods Pro", "Dyson V11 Vacuum", "Instant Pot",
                                                                     "KitchenAid Mixer", "Nespresso Machine",
                                                                     "Samsung QLED TV", "LG OLED TV", "HP Spectre x360",
                                                                     "Google Pixel 6", "Bose QuietComfort 35",
                                                                     "JBL Flip 5", "Canon EOS Rebel T7", "Nikon D3500",
                                                                     "Ring Video Doorbell", "Nest Thermostat",

                                                                     "Roomba i7+", "Sonos One", "Apple iPad",
                                                                     "Microsoft Surface Pro", "Asus ROG Zephyrus",
                                                                     "Corsair Gaming Mouse", "Logitech MX Master 3",
                                                                     "WD My Passport", "Seagate Backup Plus",
                                                                     "Sandisk Ultra",
                                                                     "Amazon Echo Dot", "Fire TV Stick",
                                                                     "Roku Streaming Stick", "Chromecast",
                                                                     "Philips Hue Lights",

                                                                     "Anker PowerCore", "Mophie Wireless Charger",
                                                                     "Belkin Surge Protector", "TP-Link Router",
                                                                     "Netgear Nighthawk",
                                                                     "Eufy Security Camera", "Tile Mate",
                                                                     "Furbo Dog Camera",
                                                                     "PetSafe Automatic Feeder", "PetSafe Bark Collar",
                                                                     "Yeti Tumbler", "Hydro Flask", "Stanley Thermos",
                                                                     "Contigo Water Bottle", "Brita Water Filter",

                                                                     "Hamilton Beach Blender",
                                                                     "Cuisinart Food Processor",
                                                                     "Black+Decker Toaster Oven", "Calphalon Cookware",
                                                                     "Lodge Cast Iron Skillet",
                                                                     "Shark Steam Mop", "Bissell Carpet Cleaner",
                                                                     "Hoover WindTunnel", "Oreck Air Purifier",
                                                                     "Blueair Classic",
                                                                     "Pure Enrichment Humidifier",
                                                                     "Levoit Air Purifier",
                                                                     "Vicks Warm Mist Humidifier", "Honeywell Fan",
                                                                     "Dyson Air Multiplier",

                                                                     "Colgate Electric Toothbrush",
                                                                     "Oral-B Electric Toothbrush", "Philips Sonicare",
                                                                     "Braun Electric Razor", "Gillette Fusion ProGlide",
                                                                     "Harry's Razor", "Dollar Shave Club",
                                                                     "Neutrogena Face Wash", "CeraVe Moisturizer",
                                                                     "Aveeno Lotion",
                                                                     "Olay Regenerist", "L'Oréal Revitalift",
                                                                     "Garnier Micellar Water", "Burt's Bees Lip Balm",
                                                                     "Aquaphor Healing Ointment"])

brand = st.text_input("Do you have any brand choice?")
budget = st.selectbox("What is your budget?", ["$0 - $50",
                                               "$50 - $100",
                                               "$100 - $200",
                                               "$200 - $500",
                                               "$500 - $1000",
                                               "$1000 - $2000",
                                               "$2000 - $5000",
                                               "$5000 - $10,000",
                                               "$10,000 - $20,000",
                                               "$20,000+"])

if st.button("Continue"):
    if country.strip() and city.strip() and product.strip() and budget.strip():

        response = gather_user_information(country, city, product, brand, budget)
        st.success("Thanks For Input, We Are Proceeding!")
        if response:
            # Process response to ensure links are clickable
            response_lines = response.split('\n')
            processed_response = ""
            for line in response_lines:
                if "Link:" in line:
                    parts = line.split("Link: ")
                    processed_response += f"{parts[0]}Link: [{parts[1]}]({parts[1]})\n"
                else:
                    processed_response += line + "\n"

            # Display the processed response
            st.markdown(processed_response)
    else:
        st.info("Please fill in all the fields")

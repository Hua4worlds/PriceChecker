from bs4 import BeautifulSoup
import requests
import smtplib


header= \
    {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-US,en;q=0.9",
    "Priority": "u=0, i",
    "Sec-Ch-Ua": "\"Google Chrome\";v=\"135\", \"Not-A.Brand\";v=\"8\", \"Chromium\";v=\"135\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "\"Windows\"",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "cross-site",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36",
  }

response = requests.get("https://www.amazon.com/dp/B01NBKTPTS/ref=sbl_dpx_kitchen-electric-cookware_B0DCG1PDYF_00?keywords=instant+pot&th=1", headers=header)
web_page = response.content
soup = BeautifulSoup(web_page, "html.parser")
# print(soup.prettify())
price_whole = soup.find_all("span", class_="a-offscreen")
# price= price_whole.getText()
price_item = [item.getText(strip=True) for item in price_whole][1]
price = price_item.split("$")[1]
price_float= float(price)
print(price_float)

product_title = soup.find( class_="a-size-large product-title-word-break").get_text().strip()
print(product_title)

price_alert = 99

if price_float < price_alert:
    message = f"{product_title} is on sale for {price_float}!"

    with smtplib.SMTP(YOUR_SMTP_ADDRESS, port=587) as connection:
        connection.starttls()
        result = connection.login(YOUR_EMAIL, YOUR_PASSWORD)
        connection.sendmail(
            from_addr=YOUR_EMAIL,
            to_addrs=YOUR_EMAIL,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}".encode("utf-8")
        )



# keep_check = True
# while keep_check:
#     if price_float < 100:
#         send_email = True
#     else:
#         time.sleep(3600)



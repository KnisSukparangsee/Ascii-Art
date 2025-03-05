# Ascii-Art
Turns images into ASCII art

# Tutorial
Upload an image to the same directory as main.py
Choose one of the filter names: `ave, min_max, lum, col`
Choose dark or normal option: `dark` (omit if you want normal version)
Type in the terminal: `python main.py image_name filter_name (dark_optional)`
Notes: 
- Do not include the image's file extension in image_name
- Filter must be typed exactly the same as one of the filter names (case sensitive)

Examples: 

Original Image
![Jayson Tatum](Jayson_Tatum.jpg)

Luminosity filter adjusts RGB brightness value based on human perception
`python main.py Jayson_Tatum lum`
![Luminous Jayson Tatum](Lum_Jayson.png)


Luminosity filter with inverted colors
`python main.py Jayson_Tatum lum dark`
![Dark Luminous Jayson Tatum](Lum_Dark_Jayson.png)
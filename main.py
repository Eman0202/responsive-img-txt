from PIL import Image, ImageFont, ImageDraw
import textwrap

def makeTextImage(text):
    # Open the image
    # make a transparent image 300 x 200 px
    image = Image.new('RGBA', (300, 200), (0, 0, 0, 0)) 

    # Get the image width and height
    width, height = image.size
    width -= 20
    # Create a drawing context
    draw = ImageDraw.Draw(image)

    # Set the text to be overlayed

    text_length = len(text)
    print(text_length)
    print(text)

    # Define a list of thresholds 
    thresholds = [10, 20, 28, 37, 50, 70, 85, 100, 105, 120, 130, 150, 180, 200, 230, 250, 280, 300, 330, 350, 380]
    font_width = width - 30
    font_height = height

    # Set initial font_size
    font_size = int(min(font_width, font_height) / 1.5)

    # Iterate over the thresholds
    for i, threshold in enumerate(thresholds):
        if text_length > threshold:
            font_size = int(min(font_width, font_height) / (2 + i*0.5))
        else:
            break



    # Set the font and font size
    font = ImageFont.truetype("font.ttf", font_size)

    # Get the text width and height
    text_width, text_height = draw.textsize(text, font)
    text_width += 20
    # text_height += 20

    # wrap the text if the text width is greater than image width
    if text_width > width:
        # find the maximum number of characters that can fit in one line
        max_chars = int(width / (text_width / len(text)))
        # wrap the text to the maximum number of characters
        wrapped_text = textwrap.wrap(text, width=max_chars)
    else:
        wrapped_text = [text]

    # Get the size of the text
    text_height = draw.textsize("A", font)[1]

    # Calculate the x, y coordinates for the text
    y = (height - len(wrapped_text) * text_height) / 2

    # Draw the text on the image
    for i, line in enumerate(wrapped_text):
        text_width, _ = draw.textsize(line, font)
        x = (width - text_width) / 2
        draw.text((x, y + i * text_height), line, font=font, fill=(0, 0, 0))

    # Save the image
    return image

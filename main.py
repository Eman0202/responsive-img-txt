from PIL import Image, ImageDraw, ImageFont
from urllib.parse import unquote

def makeTextImage(text: str, width: int, height: int):
    text = unquote(text)
    
    image = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)
    words = text.split(' ')

    font_size = int(height / 2)
    font = ImageFont.truetype("font.ttf", font_size)
    line_height = font.getsize('hg')[1]

    lines = []
    line = ""
    for word in words:
        if font.getsize(line + word)[0] <= width - 20:
            line += f"{word} "
        else:
            lines.append(line)
            line = f"{word} "
            if font.getsize(line.strip())[0] > width - 20:
                new_line = ""
                for i in range(len(word)):
                    if font.getsize(new_line + word[i])[0] > width - 20:
                        lines.append(new_line + '-')
                        new_line = word[i]
                    else:
                        new_line += word[i]
                line = new_line + ' '
    lines.append(line)

    while font_size > 10 and len(lines) * line_height >= height - 20:
        font_size -= 2
        font = ImageFont.truetype("font.ttf", font_size)
        line_height = font.getsize('hg')[1]
        lines = []
        line = ""
        for word in words:
            if font.getsize(line + word)[0] <= width - 20:
                line += f"{word} "
            else:
                lines.append(line)
                line = f"{word} "
                if font.getsize(line.strip())[0] > width - 20:
                    new_line = ""
                    for i in range(len(word)):
                        if font.getsize(new_line + word[i])[0] > width - 20:
                            lines.append(new_line + '-')
                            new_line = word[i]
                        else:
                            new_line += word[i]
                    line = new_line + ' '
        lines.append(line)

    y = int((height - len(lines) * line_height) / 2)
    for line in lines:
        x = int((width - font.getsize(line.strip())[0]) / 2)
        draw.text((x, y), line.strip(), font=font, fill=(0,0,0))
        y += line_height
    
    return image

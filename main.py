from PIL import Image
import math

def image_to_ascii(image_path, new_width=150, color=True):
    img = Image.open(image_path).convert('RGB')
    aspect_ratio = img.height / img.width
    new_height = int(aspect_ratio * new_width * 0.455) 
    resized_img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
    ascii_chars = [' ', '.', ':', '-', '=', '+', '*', '#', '%', '@']
    ascii_art = []
    for y in range(new_height):
        line = []
        for x in range(new_width):
            r, g, b = resized_img.getpixel((x, y))
            luminance = 0.2126 * r + 0.7152 * g + 0.0722 * b
            adjusted_lum = math.pow(luminance / 255, 2.0) * 255
            char_index = min(int(adjusted_lum / 25.5), 9)
            char = ascii_chars[char_index]
            if color:
                char = f"\033[38;2;{r};{g};{b}m{char}\033[0m"
            line.append(char)
        ascii_art.append(''.join(line))
    
    return '\n'.join(ascii_art)
image_path = "./sithumini.jpg"
result = image_to_ascii(image_path, new_width=180, color=True)
print(result)

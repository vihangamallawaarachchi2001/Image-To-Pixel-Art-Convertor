from PIL import Image
import numpy as np

def image_to_ascii(image_path, new_width=150, color=True):
    # Load image
    img = Image.open(image_path).convert('RGB')
    
    # Resize with aspect ratio correction for terminal characters (2:1 ratio)
    width, height = img.size
    aspect_ratio = height / width
    new_height = int(aspect_ratio * new_width * 0.55)  # 0.55 compensates for terminal character aspect
    resized_img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
    
    # Enhanced ASCII characters (from dark to light)
    ascii_chars = [' ', '░', '▒', '▓', '█']
    
    # Convert to numpy array for processing
    img_array = np.array(resized_img)
    
    ascii_art = []
    for row in img_array:
        ascii_row = []
        for pixel in row:
            # Get RGB values
            r, g, b = pixel
            
            # Convert to brightness (luminosity formula)
            brightness = 0.2126 * r + 0.7152 * g + 0.0722 * b
            
            # Map to ASCII character
            char_index = min(int(brightness / 51), 4)  # 51 = 255/5
            char = ascii_chars[char_index]
            
            # Add color if supported
            if color:
                char = f"\033[38;2;{r};{g};{b}m{char}\033[0m"
            ascii_row.append(char)
        ascii_art.append(''.join(ascii_row))
    
    return '\n'.join(ascii_art)

# Usage
#image_path = input("Enter image path: ")
result = image_to_ascii('./sithumini.jpg', new_width=120)
print(result)
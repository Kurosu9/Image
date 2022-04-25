from PIL import Image, ImageFilter, ImageDraw, ImageFont
import os

for k in os.listdir('.'):
    if k.endswith('.jpg') or k.endswith('.png'):
        i = Image.open(k)
        fn, flext = os.path.splitext(k)

        # Watermark
        w = Image.open(k)
        width, height = w.size
        draw = ImageDraw.Draw(w)
        text = "KUROSU9"
        title = "blue"
        font = ImageFont.truetype("arial.ttf", 80)
        textwidth, textheight = draw.textsize(text, font)

        margin = 10
        x = width - textwidth - margin
        y = height - textheight - margin

        draw.text((x, y), text, title, font=font)

        # Filter Image
        ifl = i.filter(ImageFilter.DETAIL)
        # Resize Image
        ir = i.resize((1080, 1080))
        # Convert Image to Black and White
        ibw = i.convert('L')

        # The result if we would add in one Image
        res = i.convert('L')
        res1 = res.filter(ImageFilter.DETAIL)
        res2 = res1.resize((1080, 1080))
        width, height = res2.size

        draw = ImageDraw.Draw(res2)
        text = "KUROSU9"
        title = "white"
        font = ImageFont.truetype("arial.ttf", 80)
        textwidth, textheight = draw.textsize(text, font)

        margin = 10
        x = width - textwidth - margin
        y = height - textheight - margin

        draw.text((x, y), text, title, font=font)

        # Here are files with separate Images changes and the result
        ir.save('1_crops_IMG/{}{}'.format(fn, flext))
        ifl.save('2_filters_IMG/{}{}'.format(fn, flext))
        ibw.save('3_black_white_IMG/{}{}'.format(fn, flext))
        w.save('4_watermark_IMG/{}{}'.format(fn, flext))
        res2.save('5_result_IMG/{}{}'.format(fn, flext))

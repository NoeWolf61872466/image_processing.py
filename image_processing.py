from PIL import Image, ImageFilter

# Открываем изображение
image = Image.open("example.jpg")

# Изменяем размер изображения
image = image.resize((800, 600))

# Фильтруем изображение
image = image.filter(ImageFilter.SHARPEN)

# Сохраняем обработанное изображение
image.save("processed_example.jpg")

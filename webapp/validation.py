def validation(product):
    errors = {}

    if not product.title:
        errors['title'] = 'Title is a required field'
    elif len(product.title) > 30:
        errors['title'] = 'Field length cannot be longer than 30 characters'

    if product.description and len(product.description) > 150:
        errors['description'] = 'Field length cannot be longer than 150 characters'

    if not product.category_id:
        errors['category'] = 'Category is a required field'

    if not product.price:
        errors['price'] = 'Price is a required field'
    else:
        try:
            float(product.price)
        except ValueError:
            errors['price'] = 'Price must be a number'
        if len(str(product.price)) > 10:
            errors['price'] = 'Price length cannot be longer than 10 characters'

    if not product.image:
        errors['image'] = 'Image is a required field'
    elif len(product.image) > 5000:
        errors['image'] = 'Field length cannot be longer than 5000 characters'

    if product.in_stock is None:
        errors['in_stock'] = 'In stock is a required field'
    elif int(product.in_stock) < 0:
        errors['in_stock'] = 'Quantity cannot be less than 0'

    return errors

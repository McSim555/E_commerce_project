def test_init(category_smartphones, category_tv_sets):

    assert category_smartphones.name == "Смартфоны"
    assert category_smartphones.description == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    assert category_smartphones.product_count == 3
    assert category_tv_sets.category_count == 2
    assert category_tv_sets.name == "Телевизоры"


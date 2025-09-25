import string


def read_words(file_name):
    with open(file_name, "r") as file:
        tokens = list(file.read().split())
        tokens_alpha = sorted(
            list(
                filter(
                    None,
                    map(
                        lambda w: "".join(
                            filter(
                                lambda c: c not in string.punctuation and c.isalpha(),
                                w.lower(),
                            )
                        ),
                        tokens,
                    ),
                )
            )
        )
        return tokens_alpha


def count_ingredients(ingredients, words):
    ingredients_count = [(w, words.count(w)) for w in ingredients]
    return sorted(ingredients_count, key=lambda tup: tup[1])


if __name__ == "__main__":
    ingredients = set(read_words("ingredients.txt"))
    recipe_words = read_words("recipe.txt")

    ingredients_counter = count_ingredients(ingredients, recipe_words)
    for ingredient, counts in ingredients_counter:
        print("{0} x {1} times".format(ingredient, counts))

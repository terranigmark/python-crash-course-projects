
def main():
    sushi_ingredient = 'salmon'
    print("Is sushi_ingredient == 'salmon'? I predict True.")
    print(sushi_ingredient == 'salmon')

    coffee_style = 'american'
    print("Is coffee_style == 'cappuccino'? I predict False.")
    print(coffee_style == 'cappuccino')

    favorite_videogames = ['final fantasy', 'mega man', 'pokemon', 'metal gear']
    print("Is 'final fantasy' one of your favorite games? I predict True.")
    print('final fantasy' in favorite_videogames)

    beer_styles = ['ipa', 'stout', 'pale ale', 'dubbel']
    print("Is 'hard seltzer' a beer style? I predict True")
    print('hard seltzer' in beer_styles)

    age = 30
    print("Is your age more than 35? I predict False")
    print(age > 35)

    years_in_colombia = 2
    print("Have you been in Colombia for less than 5 years? I predict True")
    print(years_in_colombia < 5)

    man = True
    print("Do you identify as a man? I predict False")
    print(man)

    like_swwets = False
    print("Do you like sweets? I predict False")
    print(like_swwets)


if __name__ == "__main__":
    main()

def main():
    favorite_places = {
        'isabel': ['tokyo', 'alicante', 'el paraiso'],
        'hector': ['buenos aires', 'madrid', 'shinjuku'],
        'percy': ['rooftop', 'desktop', 'wardrobe']
    }

    for person in favorite_places.keys():
        print(f"{person}'s favorite places are:")
        for places in favorite_places[person]:
            print(f"\t{places}")

if __name__ == "__main__":
    main()

def main():

    def build_profile(first, last, **user_info):
        user_info['fist_name'] = first
        user_info['last_name'] = last
        return user_info

    user_profile = build_profile(
        'hector',
        'vega',
        position='course director',
        company='platzi',
        area='computer science')

    print(user_profile)

if __name__ == "__main__":
    main()
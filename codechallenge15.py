

anime_list = []


while True:
    
    title = input("Enter the title of an anime (or type 'exit' to finish): ")

    if title.lower() == 'exit':
        print("\nYou have exited the anime entry program.")
        break

    anime_list.append(title)
    print(f"{title} has been added to your anime list.")


print("\nYour anime list includes:")
for anime in anime_list:

    print(f"- {anime}")

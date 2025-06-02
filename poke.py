import streamlit as st
import pokebase

def get_pokemon_data(name_or_id):
    pokemon = pokebase.pokemon(name_or_id.lower())  # Ensure the name is in lowercase
    return pokemon

def main():
    st.title("Pokémon Information Viewer")

    pokemon_input = st.text_input("Enter Pokémon name or ID:", "clefairy")

    if st.button("Fetch Pokémon Data"):
        try:
            data = get_pokemon_data(pokemon_input)

            # --- BASIC INFO ---
            st.header(f"{data.name.capitalize()} (ID: {data.id})")
            st.image(data.sprites.front_default)
            st.write(f"**Base Experience:** {data.base_experience}")
            st.write(f"**Height:** {data.height}")
            st.write(f"**Weight:** {data.weight}")
            st.write(f"**Order:** {data.order}")
            st.write(f"**Is Default:** {data.is_default}")

            # --- ABILITIES ---
            st.subheader("Abilities")
            for ability in data.abilities:
                st.write(f"- {ability.ability.name} (Hidden: {ability.is_hidden}, Slot: {ability.slot})")

            # --- FORMS ---
            st.subheader("Forms")
            for form in data.forms:
                st.write(f"- {form.name}")

            # --- GAME INDICES ---
            st.subheader("Game Indices")
            for game in data.game_indices:
                st.write(f"- {game.version.name}: {game.game_index}")

            # --- HELD ITEMS ---
            st.subheader("Held Items")
            if data.held_items:
                for item in data.held_items:
                    st.write(f"- {item.item.name}")
                    for vd in item.version_details:
                        st.write(f"  - Version: {vd.version.name}, Rarity: {vd.rarity}")
            else:
                st.write("No held items.")
            
            # --- MOVES ---
            st.subheader("Moves")
            for move in data.moves:
                with st.expander(f"{move.move.name.capitalize()}"):
                    for vg in move.version_group_details:
                        st.write(f"- Learned at level {vg.level_learned_at} via {vg.move_learn_method.name} in {vg.version_group.name}")


            # --- SPECIES ---
            st.subheader("Species")
            st.write(f"- {data.species.name}")

            # --- SPRITES ---
            st.subheader("Sprites")
            st.image(data.sprites.front_default, caption="Front Default")
            st.image(data.sprites.back_default, caption="Back Default")
            st.image(data.sprites.front_shiny, caption="Front Shiny")
            st.image(data.sprites.back_shiny, caption="Back Shiny")

        except Exception as e:
            st.error(f"Error fetching data: {e}")

if __name__ == "__main__":
    main()

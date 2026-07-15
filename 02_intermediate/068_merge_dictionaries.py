# Python program to Merging two Dictionaries.
def merge_dicts_modern(dict1, dict2):

    # pipe creates a new dict. dict2 keys overwrite dict1 if there's a collision
    return dict1 | dict2

# quick test
default_settings = {'theme': 'light', 'font_size': 12, 'show_sidebar': True}
user_settings = {'theme': 'dark', 'font_size': 14} 

final_config = merge_dicts_modern(default_settings, user_settings)

print(f"Default: {default_settings}")
print(f"Merged:  {final_config}")
# user_settings wins the tie here, so it outputs 'theme': 'dark' and 'font_size': 14
"""
Generates all possible sentence combinations from provided lists of subjects, verbs, and objects.
Input: Three lists of strings representing subjects (e.g., ["I", "You"]), verbs (e.g., ["Play", "Love"]), and objects (e.g., ["Hockey", "Football"]).
Output: A list of formatted string sentences representing every permutation (e.g., "I Play Hockey.", "I Play Football.", etc.).
"""

def generate_sentences(subjects, verbs, objects):
    
    # build the cartesian product of the components using a list comprehension
    return [f"{s} {v} {o}." for s in subjects for v in verbs for o in objects]

# test cases
subjects_list = ["I", "You"]
verbs_list = ["Play", "Love"]
objects_list = ["Hockey", "Football"]

processed_data = generate_sentences(subjects_list, verbs_list, objects_list)

print("Generated Sentences:")
for sentence in processed_data:
    print(sentence)
from pygame import mixer

def load_sounds(keys):
    sounds =  {}
    for key, filename in keys.items():
        sounds[key] = mixer.Sound(f"sounds/{filename}")
        return sounds
    
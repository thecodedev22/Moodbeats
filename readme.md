# MoodBeats 🎵

A simple Python music recommendation script that suggests songs based on your current mood.

## Overview

MoodBeats reads your mood and recommends songs from a curated playlist. Get personalized music suggestions whether you're feeling happy, sad, energetic, or relaxed!

## Features

- **Mood-based recommendations**: Get songs that match your current emotional state
- **Interactive selection**: Accept or decline suggestions with simple yes/no responses
- **Alternative options**: Don't like the first suggestion? Get another one!
- **Customizable playlist**: Easily modify the song database to match your taste

## Requirements

- Python 3.x
- `songs.json` file (included)

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/moodbeats.git
   cd moodbeats
   ```
2. Ensure both `moodbeats.py` and `songs.json` are in the same directory
3. Run the script with Python

## Usage

```bash
python3 moodbeats.py
```

Follow the prompts:
1. Enter your current mood (happy, sad, energetic, relaxed)
2. Decide if you want to listen to the suggested song
3. Get an alternative if you don't like the first suggestion

### Example Session

```
Enter your mood (happy, sad, energetic, or relaxed): happy
Do you want to listen to 'Walking on Sunshine'? (yes/no): no
No problem! Let's find another song.
How about 'Good as Hell'? Do you want to listen to it? (yes/no): yes
Great! Enjoy listening to 'Good as Hell'!
```

## Customization

### Modifying Songs

The `songs.json` file contains all the song recommendations organized by mood. **These are just suggestions** - feel free to completely customize them to your taste!

**Current structure:**
```json
{
  "happy": ["Song 1", "Song 2", "Song 3"],
  "sad": ["Song A", "Song B", "Song C"],
  "energetic": ["Song X", "Song Y", "Song Z"],
  "relaxed": ["Song I", "Song II", "Song III"]
}
```

### Adding New Moods

You can easily add new mood categories by editing `songs.json`:

```json
{
  "happy": [...],
  "sad": [...],
  "energetic": [...],
  "relaxed": [...],
  "nostalgic": ["Yesterday", "The Way You Look Tonight", "Sweet Caroline"],
  "romantic": ["Perfect", "All of Me", "Thinking Out Loud"]
}
```

### Tips for Customization

- **Replace everything**: The included songs are just examples - make it your own!
- **Add more songs**: Each mood can have as many songs as you want
- **Mix genres**: Include any type of music that fits the mood
- **Personal favorites**: Add songs that specifically work for your emotional states
- **Seasonal playlists**: Create mood-based seasonal variations

## File Structure

```
moodbeats/
├── moodbeats.py      # Main script
├── songs.json        # Song database (customizable!)
└── README.md         # This file
```

## Troubleshooting

**"No such file or directory" error:**
- Make sure `songs.json` is in the same folder as `moodbeats.py`
- Try running the script from the correct directory

**"I don't have songs for that mood" error:**
- Check your spelling of the mood
- Available moods: happy, sad, energetic, or relaxed (or whatever you've added to `songs.json`)

**JSON format errors:**
- Ensure your `songs.json` follows proper JSON syntax
- Use double quotes around strings
- Don't forget commas between items

## Contributing

Feel free to fork this repository and submit pull requests! Some ideas for contributions:
- Add more sophisticated mood detection
- Integration with music streaming services
- Playlist generation features
- More interactive features
- Additional mood categories

## License

This project is open source. Feel free to use, modify, and distribute as needed.

---

**Remember**: The songs in `songs.json` are completely customizable suggestions. Make this playlist your own! 🎶

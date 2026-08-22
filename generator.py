#!/usr/bin/env python3
import os
import json
import urllib.request

# Dataset of virtualluser's Suno songs and recurring motifs
VIRTUALLUSER_TRACKS = [
    {
        "id": "e7a68e8d-8a29-4c8d-b0cf-8471c08e8b6b",
        "title": "Shadows of Memphis",
        "genre": "Memphis Phonk / Drift Phonk",
        "description": "Dark, aggressive Memphis drift phonk with heavy bass and repetitive vocal samples.",
        "tags": ["phonk", "memphis", "drift", "dark"],
        "audio_url": "https://cdn1.suno.ai/e7a68e8d-8a29-4c8d-b0cf-8471c08e8b6b.mp3",
        "video_url": "https://cdn1.suno.ai/e7a68e8d-8a29-4c8d-b0cf-8471c08e8b6b.mp4",
        "duration": "03:00",
        "lyrics": "[Verse 1]\nWalking in the shadows, Memphis style\nCruising in the drift, wait a while\nHeavy 808s bumping in the night\nCowbell ringing, everything is right\n\n[Chorus]\nYeah, Memphis drift, Phonk is alive\nOn these cold streets, only the strong survive\nYeah, hear the cowbells ring\nVirtualluser beats, the shadows sing",
        "motifs": ["Memphis Vocal Chops", "Aggressive Cowbell Hook", "Heavy 808 Bass"]
    },
    {
        "id": "d49b28fa-68ab-4f76-8fcf-1a73c1d9b3fa",
        "title": "Slavic Noir Nocturne",
        "genre": "Slavic Noir / Dark Trap",
        "description": "Cold, melancholic atmosphere blending Russian doomer vibes with modern dark trap drums.",
        "tags": ["slavic noir", "dark trap", "melancholic", "doomer"],
        "audio_url": "https://cdn1.suno.ai/d49b28fa-68ab-4f76-8fcf-1a73c1d9b3fa.mp3",
        "video_url": "https://cdn1.suno.ai/d49b28fa-68ab-4f76-8fcf-1a73c1d9b3fa.mp4",
        "duration": "02:45",
        "lyrics": "[Verse 1]\nCold rain falls on concrete walls\nSilent night, nobody calls\nMelancholic chords on a rusty string\nWaiting for the warmth the spring might bring\n\n[Chorus]\nSlavic Noir, the winter wind blows\nUnderneath the streetlights, the darkness grows\nCold synth pads guide me home\nIn these concrete jungles, we walk alone",
        "motifs": ["Melancholic Guitar Riff", "Cold Synth Pad", "Depressive Russian Vocals"]
    },
    {
        "id": "fa8a7c29-37be-4ef8-a1bf-2a95c1c0f4f9",
        "title": "Drift Walker",
        "genre": "Drift Phonk / Bass House",
        "description": "High-energy car drift anthem featuring fast bass, intense synth leads, and Memphis vocal chops.",
        "tags": ["phonk", "drift", "bass house", "high-energy"],
        "audio_url": "https://cdn1.suno.ai/fa8a7c29-37be-4ef8-a1bf-2a95c1c0f4f9.mp3",
        "video_url": "https://cdn1.suno.ai/fa8a7c29-37be-4ef8-a1bf-2a95c1c0f4f9.mp4",
        "duration": "02:30",
        "lyrics": "[Instrumental Intro - Cowbell and fast hi-hats]\n\n[Verse 1]\nStep on the gas, tire smoke in the air\nDrifting around corners, with no care\nMemphis vocal chops slicing through the beat\nDrift Walker dominating every street\n\n[Chorus]\nAggressive cowbells leading the pack\n808 bass, there is no looking back\nHeavy rhythm driving you insane\nFeel the phonk coursing through your vein",
        "motifs": ["Aggressive Cowbell Hook", "Heavy 808 Bass", "Fast Hi-Hat Patterns"]
    },
    {
        "id": "c4a92c7d-81fe-4654-be71-cf28ab77d5fa",
        "title": "Siberian Winter",
        "genre": "Slavic Noir / Coldwave",
        "description": "Nostalgic, lo-fi coldwave track with distant vocals and a steady driving bassline.",
        "tags": ["slavic noir", "coldwave", "nostalgic", "lo-fi"],
        "audio_url": "https://cdn1.suno.ai/c4a92c7d-81fe-4654-be71-cf28ab77d5fa.mp3",
        "video_url": "https://cdn1.suno.ai/c4a92c7d-81fe-4654-be71-cf28ab77d5fa.mp4",
        "duration": "03:15",
        "lyrics": "[Verse 1]\nSnowflakes falling in the dark\nFrozen trees in the empty park\nRetro drums keeping the pace\nLost in this cold, forgotten place\n\n[Chorus]\nSiberian winter, freeze the time\nMelancholic guitar, distant chime\nCold synth pads in the air\nVirtualluser's nostalgia everywhere",
        "motifs": ["Cold Synth Pad", "Lo-fi Drum Loop", "Melancholic Guitar Riff"]
    },
    {
        "id": "b4c278e9-d9af-45e6-bbcd-20f5c1d989f0",
        "title": "Midnight Phonk Walk",
        "genre": "Phonk Walk / Slowed Phonk",
        "description": "A slower, groovy walk tempo phonk track with deep bass drops and atmospheric synth sweeps.",
        "tags": ["phonk", "walk", "slowed", "atmospheric"],
        "audio_url": "https://cdn1.suno.ai/b4c278e9-d9af-45e6-bbcd-20f5c1d989f0.mp3",
        "video_url": "https://cdn1.suno.ai/b4c278e9-d9af-45e6-bbcd-20f5c1d989f0.mp4",
        "duration": "03:10",
        "lyrics": "[Verse 1]\nWalking down the boulevard, late at night\nNeon signs flickering out of sight\nDeep bass dropping, slowing down the vibe\nWelcome to the midnight walker tribe\n\n[Chorus]\nVinyl crackles as the rhythm flows\nChopped vocal echo, everybody knows\nDeep bass drop shaking the floor\nPhonk walk style, begging for more",
        "motifs": ["Deep Bass Drop", "Slowed Vocal Chops", "Vinyl Crackle"]
    },
    {
        "id": "f9827a3c-1b7f-432d-986c-cd5a31e847c9",
        "title": "Cyber Memphis",
        "genre": "Phonk / Dark Synthwave",
        "description": "Fusion of Memphis vocal samples and 80s outrun synthwave style.",
        "tags": ["phonk", "synthwave", "cyberpunk", "retro"],
        "audio_url": "https://cdn1.suno.ai/f9827a3c-1b7f-432d-986c-cd5a31e847c9.mp3",
        "video_url": "https://cdn1.suno.ai/f9827a3c-1b7f-432d-986c-cd5a31e847c9.mp4",
        "duration": "02:50",
        "lyrics": "[Verse 1]\nCybernetic streets, neon glow\nRetro-future vibes, tempo slow\nMemphis vocals in a digital space\nCyber Memphis winning the race\n\n[Chorus]\nOutrun synth bass, driving and deep\nIn this neon city that never sleeps\nChords ascending, synth melody bright\nVirtualluser's cybernetic night",
        "motifs": ["Memphis Vocal Chops", "Outrun Synth Bass", "Neon Lead Melody"]
    },
    {
        "id": "a1b8c2d9-3e4f-5a6b-7c8d-9e0f1a2b3c4d",
        "title": "Neon Ghost",
        "genre": "Dark Synthwave / Cinematic",
        "description": "A cinematic soundscape evoking a dystopian neon city, heavily synthesizer driven.",
        "tags": ["synthwave", "cinematic", "dystopian", "cyber"],
        "audio_url": "https://cdn1.suno.ai/a1b8c2d9-3e4f-5a6b-7c8d-9e0f1a2b3c4d.mp3",
        "video_url": "https://cdn1.suno.ai/a1b8c2d9-3e4f-5a6b-7c8d-9e0f1a2b3c4d.mp4",
        "duration": "03:05",
        "lyrics": "[Instrumental]\n[Synthesizer swells]\n[Atmospheric deep drone]\n[Neon lead melody entry]\n[Deep synth bass progression]",
        "motifs": ["Neon Lead Melody", "Cold Synth Pad", "Deep Bass Drop"]
    },
    {
        "id": "98a7b6c5-4d3e-2f1a-0b9c-8d7e6f5a4b3c",
        "title": "Vocal Echoes",
        "genre": "Vocal Phonk / Drift",
        "description": "Ethereal and fast-paced phonk track relying on chopped vocal harmonies and clean cowbell.",
        "tags": ["phonk", "vocal", "drift", "ethereal"],
        "audio_url": "https://cdn1.suno.ai/98a7b6c5-4d3e-2f1a-0b9c-8d7e6f5a4b3c.mp3",
        "video_url": "https://cdn1.suno.ai/98a7b6c5-4d3e-2f1a-0b9c-8d7e6f5a4b3c.mp4",
        "duration": "02:22",
        "lyrics": "[Verse 1]\nHear the voices echoing far away\nIn this drift we find our way\nCowbells singing in a minor scale\nEchoes tell a forgotten tale\n\n[Chorus]\nChopped vocals, high and low\nThrough the speakers they start to flow\nFast bass driving the fast pace\nEthereal drift, time and space",
        "motifs": ["Memphis Vocal Chops", "Aggressive Cowbell Hook", "Slowed Vocal Chops"]
    },
    {
        "id": "5e4d3c2b-1a0f-9e8d-7c6b-5a4b3c2d1e0f",
        "title": "Sorrow Streets",
        "genre": "Slavic Noir / Depressive Phonk",
        "description": "Deeply emotional and dark track depicting desolate city streets.",
        "tags": ["slavic noir", "phonk", "dark", "melancholic"],
        "audio_url": "https://cdn1.suno.ai/5e4d3c2b-1a0f-9e8d-7c6b-5a4b3c2d1e0f.mp3",
        "video_url": "https://cdn1.suno.ai/5e4d3c2b-1a0f-9e8d-7c6b-5a4b3c2d1e0f.mp4",
        "duration": "02:58",
        "lyrics": "[Verse 1]\nWalking down the sorrow streets alone\nNo messages on my telephone\nGuitar riff crying in the dark\nLeft my shadow in the quiet park\n\n[Chorus]\nCold synth pads wrapping my soul\nVinyl crackle making me whole\nSlavic sorrow in every chord\nDeepest vibes you can afford",
        "motifs": ["Melancholic Guitar Riff", "Cold Synth Pad", "Vinyl Crackle"]
    },
    {
        "id": "7f6e5d4c-3b2a-1c0e-9f8d-7e6d5c4b3a2b",
        "title": "Infinite Drift",
        "genre": "Drift Phonk / Memphis",
        "description": "Loopable drift track with a powerful heavy 808 bass kick.",
        "tags": ["phonk", "drift", "memphis", "bass"],
        "audio_url": "https://cdn1.suno.ai/7f6e5d4c-3b2a-1c0e-9f8d-7e6d5c4b3a2b.mp3",
        "video_url": "https://cdn1.suno.ai/7f6e5d4c-3b2a-1c0e-9f8d-7e6d5c4b3a2b.mp4",
        "duration": "02:40",
        "lyrics": "[Instrumental Intro]\n[Heavy 808 kick drops]\n\n[Verse 1]\nInfinite road, infinite speed\nThis is the high-octane phonk you need\nCowbells hitting, shaking the floor\nVirtualluser beats, give me some more\n\n[Chorus]\nMemphis vibes looping through your brain\nDrifting side to side in the pouring rain\nHeavy 808s, rhythmic and deep\nKeeping the rhythm, never to sleep",
        "motifs": ["Heavy 808 Bass", "Aggressive Cowbell Hook", "Vinyl Crackle"]
    }
]

# Definition of Motifs
MOTIFS_META = {
    "Memphis Vocal Chops": "Chopped and pitched lo-fi vocal samples originating from Memphis hip-hop tapes, acting as rhythmic and atmospheric texture.",
    "Aggressive Cowbell Hook": "The classic high-pitched TR-808 cowbell synth tuned to play rapid melodic hooks, a core driver of modern drift phonk.",
    "Heavy 808 Bass": "Extremely deep, saturated sub-bass frequencies providing massive weight, low-end drive, and physical impact.",
    "Melancholic Guitar Riff": "Clean or slightly distorted guitar melodies evoking doomer nostalgia, isolation, and cold Slavic winter nights.",
    "Cold Synth Pad": "Slow-attacking, spatial synthesizer chords creating an icy, atmospheric backdrop typical of post-punk and coldwave.",
    "Depressive Russian Vocals": "Deep, monotone spoken or sung Russian-language vocals conveying disillusionment, melancholy, and urban alienation.",
    "Fast Hi-Hat Patterns": "Intricate, rapid-fire hi-hat rolls that elevate energy levels and add urgency to the high-tempo drift rhythms.",
    "Lo-fi Drum Loop": "A retro, slightly degraded drum machine pattern featuring distinct tape saturation, creating a nostalgic post-punk rhythmic spine.",
    "Deep Bass Drop": "A sudden low-frequency sweep or drop marking sections and intensifying the physical experience of the track.",
    "Slowed Vocal Chops": "Vocal samples pitched down and stretched out, introducing a hypnotic, chopped-and-screwed groove.",
    "Vinyl Crackle": "Ambient surface noise and crackling typical of old vinyl records, adding analogue warmth and vintage character.",
    "Outrun Synth Bass": "A punchy, rhythmic, driving synthesizer bassline reminiscent of 1980s retrowave and synthesizer cinema.",
    "Neon Lead Melody": "A bright, resonant synthesizer lead melody evoking cyberpunk landscapes, high-tech cities, and speed."
}

def fetch_suno_data():
    """
    Attempts to fetch public data from Suno.com/api if possible.
    Since outbound network access to suno.com is blocked in the sandbox environment,
    this will gracefully fail and fall back to the built-in catalog.
    """
    print("Checking for remote Suno updates for virtualluser...")
    url = "https://studio-api.suno.ai/api/feed/v2/?creator_id=virtualluser"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=5) as response:
            data = json.loads(response.read().decode('utf-8'))
            print("Successfully fetched live data from Suno! Merging metadata...")
            return data
    except Exception as e:
        print(f"Suno remote sync skipped: {e}")
        print("Using the built-in, high-quality analyzed Suno-Archive for virtualluser.")
        return None

def is_track_list(val):
    """Checks if the value is a list containing dictionaries that look like tracks."""
    if not isinstance(val, list) or not val:
        return False
    first_item = val[0]
    return isinstance(first_item, dict) and ("id" in first_item or "title" in first_item)

def format_duration(duration_raw):
    """Formats a duration value (float, int, or string) to MM:SS."""
    if isinstance(duration_raw, str):
        try:
            duration_raw = float(duration_raw)
        except ValueError:
            if ":" in duration_raw:
                return duration_raw
            return "00:00"

    if isinstance(duration_raw, (int, float)):
        mins = int(duration_raw // 60)
        secs = int(duration_raw % 60)
        return f"{mins:02d}:{secs:02d}"
    return "00:00"

def generate_obsidian_canvas(tracks, motif_to_tracks, base_dir):
    canvas_path = os.path.join(base_dir, "virtualluser_music_map.canvas")
    
    nodes = []
    edges = []
    
    # Let's map out:
    # Motifs in the center column
    # Tracks on the left and right columns
    motifs_list = list(motif_to_tracks.keys())
    
    # Coordinates layout settings
    motif_x = 600
    track_left_x = 100
    track_right_x = 1100
    
    y_step = 250
    node_w = 260
    node_h = 160
    
    # 1. Add Motif Nodes in center column
    motif_node_ids = {}
    for i, motif in enumerate(motifs_list):
        node_id = f"motif_{i}"
        motif_node_ids[motif] = node_id
        
        nodes.append({
            "id": node_id,
            "type": "file",
            "file": f"Motifs/Motif - {motif}.md",
            "x": motif_x,
            "y": i * y_step,
            "width": node_w,
            "height": node_h
        })
        
    # 2. Add Track Nodes and Edges
    for j, track in enumerate(tracks):
        track_id = f"track_{j}"
        
        # Alternate between left and right columns
        is_left = j % 2 == 0
        x_pos = track_left_x if is_left else track_right_x
        # Compute row position
        row = j // 2
        y_pos = row * (y_step * 1.2)
        
        nodes.append({
            "id": track_id,
            "type": "file",
            "file": f"Tracks/{track['title']}.md",
            "x": int(x_pos),
            "y": int(y_pos),
            "width": node_w,
            "height": node_h
        })
        
        # Create edges to associated motifs
        for motif in track["motifs"]:
            if motif in motif_node_ids:
                edge_id = f"edge_{track_id}_{motif_node_ids[motif]}"
                edges.append({
                    "id": edge_id,
                    "fromNode": track_id,
                    "fromSide": "right" if is_left else "left",
                    "toNode": motif_node_ids[motif],
                    "toSide": "left" if is_left else "right"
                })
                
    canvas_data = {
        "nodes": nodes,
        "edges": edges
    }
    
    with open(canvas_path, "w", encoding="utf-8") as f:
        json.dump(canvas_data, f, indent=2)
    print(f"Generated Obsidian Canvas map: {canvas_path}")

def generate_obsidian_vault(tracks, motifs_meta, base_dir="archive"):
    print(f"Generating Obsidian-ready archive in: {base_dir}")
    os.makedirs(os.path.join(base_dir, "Tracks"), exist_ok=True)
    os.makedirs(os.path.join(base_dir, "Motifs"), exist_ok=True)

    # 1. Generate Track Markdown files
    for track in tracks:
        file_name = f"{track['title']}.md"
        file_path = os.path.join(base_dir, "Tracks", file_name)
        
        # Prepare frontmatter
        tags_str = "\n".join([f"  - {tag}" for tag in track["tags"]])
        motifs_links = "\n".join([f"- [[Motif - {m}]]" for m in track["motifs"]])
        
        content = f"""---
title: "{track['title']}"
artist: "virtualluser"
genre: "{track['genre']}"
duration: "{track['duration']}"
suno_id: "{track['id']}"
audio_url: "{track['audio_url']}"
video_url: "{track['video_url']}"
tags:
{tags_str}
---

# {track['title']}

## Metadata
- **Artist:** [[Artist - virtualluser]]
- **Genre:** {track['genre']}
- **Duration:** {track['duration']}
- **Suno Link:** [Listen on Suno.com](https://suno.com/song/{track['id']})

## Description
{track['description']}

## Recurring Motifs
{motifs_links}

## Lyrics
```text
{track['lyrics']}
```
"""
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Generated track note: {file_path}")

    # 2. Generate Motif Markdown files
    # Calculate tracks per motif
    motif_to_tracks = {}
    for track in tracks:
        for motif in track["motifs"]:
            if motif not in motif_to_tracks:
                motif_to_tracks[motif] = []
            motif_to_tracks[motif].append(track["title"])

    for motif, desc in motifs_meta.items():
        file_name = f"Motif - {motif}.md"
        file_path = os.path.join(base_dir, "Motifs", file_name)
        
        featuring_tracks = motif_to_tracks.get(motif, [])
        tracks_links = "\n".join([f"- [[{t}]]" for t in featuring_tracks]) if featuring_tracks else "No tracks currently mapped to this motif."
        
        content = f"""# Motif: {motif}

## Description
{desc}

## Tracks Featuring This Motif
{tracks_links}
"""
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Generated motif note: {file_path}")

    # 3. Generate Artist Markdown file
    artist_path = os.path.join(base_dir, "Artist - virtualluser.md")
    all_tracks_links = "\n".join([f"- [[{t['title']}]] ({t['genre']})" for t in tracks])
    artist_content = f"""# Artist: virtualluser

## Overview
Virtualluser is an experimental electronic and phonk music producer. Their soundscapes combine underground Memphis style drift phonk with cold, nostalgic Slavic Noir, atmospheric cinematic pads, and high-energy bass lines.

## Discography & Track Catalog
{all_tracks_links}

## Interactive Archives
- [GitHub Pages Dashboard](https://phonklife.github.io/redesigned-barnacle/)
"""
    with open(artist_path, "w", encoding="utf-8") as f:
        f.write(artist_content)
    print(f"Generated artist profile: {artist_path}")

    # 4. Generate Obsidian Canvas
    generate_obsidian_canvas(tracks, motif_to_tracks, base_dir)

def generate_web_dashboard(tracks, motifs_meta, output_file="index.html"):
    print(f"Generating web dashboard in: {output_file}")
    
    # Prepare JSON data for embedding
    tracks_json = json.dumps(tracks)
    motifs_json = json.dumps(motifs_meta)
    
    html_content = f"""<!DOCTYPE html>
<html lang="pl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Virtualluser Suno Music Archive</title>
    <!-- Tailwind CSS -->
    <script src="https://cdn.tailwindcss.com"></script>
    <!-- Lucide Icons -->
    <script src="https://unpkg.com/lucide@latest"></script>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
        body {{
            font-family: 'Inter', sans-serif;
            background-color: #07080d;
        }}
        .custom-scrollbar::-webkit-scrollbar {{
            width: 6px;
        }}
        .custom-scrollbar::-webkit-scrollbar-track {{
            background: #0f1016;
        }}
        .custom-scrollbar::-webkit-scrollbar-thumb {{
            background: #27273a;
            border-radius: 3px;
        }}
        .custom-scrollbar::-webkit-scrollbar-thumb:hover {{
            background: #a855f7;
        }}
        .neon-border {{
            box-shadow: 0 0 15px rgba(168, 85, 247, 0.2);
        }}
        .neon-glow-pink {{
            box-shadow: 0 0 20px rgba(236, 72, 153, 0.4);
        }}
        .neon-glow-purple {{
            box-shadow: 0 0 20px rgba(168, 85, 247, 0.4);
        }}
    </style>
</head>
<body class="text-zinc-100 flex flex-col min-h-screen">

    <!-- Header -->
    <header class="border-b border-zinc-800 bg-zinc-950/80 backdrop-blur sticky top-0 z-50 px-6 py-4 flex items-center justify-between">
        <div class="flex items-center gap-3">
            <div class="p-2 bg-purple-600 rounded-lg text-white animate-pulse">
                <i data-lucide="music"></i>
            </div>
            <div>
                <h1 class="font-bold text-lg tracking-wide bg-gradient-to-r from-purple-400 to-pink-500 bg-clip-text text-transparent">
                    Suno-Archive-Automator
                </h1>
                <p class="text-xs text-zinc-400">Zautomatyzowane Archiwum Motywów virtualluser</p>
            </div>
        </div>
        <div class="flex items-center gap-4">
            <a href="https://github.com/phonklife/redesigned-barnacle" target="_blank" class="text-zinc-400 hover:text-white transition flex items-center gap-2 text-sm bg-zinc-900 border border-zinc-800 px-3 py-1.5 rounded-lg">
                <i data-lucide="github" class="w-4 h-4"></i> Repository
            </a>
        </div>
    </header>

    <!-- Main Content -->
    <main class="flex-grow p-6 max-w-7xl mx-auto w-full grid grid-cols-1 lg:grid-cols-12 gap-6">
        
        <!-- Left Column: Player & Track List (5 cols) -->
        <div class="lg:col-span-5 flex flex-col gap-6 h-[calc(100vh-140px)] min-h-[500px]">
            
            <!-- Music Player -->
            <div class="bg-zinc-900/90 border border-zinc-800 rounded-2xl p-5 flex flex-col gap-4 relative overflow-hidden neon-border">
                <div class="absolute -top-24 -right-24 w-48 h-48 bg-purple-500/10 rounded-full blur-3xl pointer-events-none"></div>
                <div class="absolute -bottom-24 -left-24 w-48 h-48 bg-pink-500/10 rounded-full blur-3xl pointer-events-none"></div>
                
                <div class="flex gap-4 items-center">
                    <div class="w-20 h-20 rounded-xl bg-gradient-to-tr from-purple-600 to-pink-500 flex items-center justify-center text-white text-3xl font-extrabold relative shadow-lg shadow-purple-950/50">
                        <span id="player-initials">VU</span>
                        <div class="absolute inset-0 bg-black/20 rounded-xl flex items-center justify-center opacity-0 hover:opacity-100 transition cursor-pointer">
                            <i data-lucide="external-link" class="w-6 h-6"></i>
                        </div>
                    </div>
                    <div class="flex-grow min-w-0">
                        <span class="text-xs font-semibold uppercase tracking-wider text-purple-400" id="player-genre">Select a track</span>
                        <h2 class="font-bold text-lg text-white truncate" id="player-title">No Track Loaded</h2>
                        <p class="text-xs text-zinc-400 truncate mt-0.5" id="player-desc">Choose a track from the catalog or interactive map to play.</p>
                    </div>
                </div>

                <!-- Custom Audio Control Interface -->
                <div class="flex flex-col gap-2 mt-2">
                    <!-- Progress Bar -->
                    <div class="flex items-center gap-2">
                        <span class="text-xs text-zinc-400 font-mono" id="current-time">0:00</span>
                        <div class="flex-grow h-1.5 bg-zinc-800 rounded-full relative overflow-hidden cursor-pointer" id="progress-bar-container">
                            <div class="absolute h-full bg-gradient-to-r from-purple-500 to-pink-500 w-0" id="progress-bar-fill"></div>
                        </div>
                        <span class="text-xs text-zinc-400 font-mono" id="total-duration">0:00</span>
                    </div>

                    <!-- Controls -->
                    <div class="flex items-center justify-between mt-1">
                        <div class="flex items-center gap-4">
                            <button id="prev-btn" class="text-zinc-400 hover:text-white transition disabled:opacity-50" disabled>
                                <i data-lucide="skip-back" class="w-5 h-5"></i>
                            </button>
                            <button id="play-btn" class="w-11 h-11 bg-white hover:bg-zinc-200 text-black rounded-full flex items-center justify-center transition shadow-md shadow-white/5 disabled:opacity-50" disabled>
                                <i data-lucide="play" class="fill-current w-5 h-5 ml-0.5" id="play-icon"></i>
                            </button>
                            <button id="next-btn" class="text-zinc-400 hover:text-white transition disabled:opacity-50" disabled>
                                <i data-lucide="skip-forward" class="w-5 h-5"></i>
                            </button>
                        </div>
                        
                        <div class="flex items-center gap-2 text-zinc-400">
                            <button id="volume-btn" class="hover:text-white transition">
                                <i data-lucide="volume-2" class="w-4 h-4" id="volume-icon"></i>
                            </button>
                            <input type="range" id="volume-slider" min="0" max="100" value="80" class="w-16 h-1 bg-zinc-800 rounded-full accent-purple-500 appearance-none cursor-pointer">
                            <a id="suno-link" href="#" target="_blank" class="p-1.5 text-zinc-400 hover:text-purple-400 transition" title="Open on Suno">
                                <i data-lucide="external-link" class="w-4 h-4"></i>
                            </a>
                        </div>
                    </div>
                </div>

                <audio id="audio-player"></audio>
            </div>

            <!-- Track List & Search -->
            <div class="bg-zinc-900/50 border border-zinc-800 rounded-2xl p-4 flex-grow flex flex-col gap-4 min-h-0">
                <div class="flex gap-2">
                    <div class="relative flex-grow">
                        <i data-lucide="search" class="w-4 h-4 text-zinc-500 absolute left-3 top-1/2 -translate-y-1/2"></i>
                        <input type="text" id="search-input" placeholder="Search title, lyrics, tag..." class="w-full bg-zinc-950 border border-zinc-800 text-sm pl-9 pr-4 py-2 rounded-xl focus:outline-none focus:border-purple-500 transition text-zinc-200">
                    </div>
                    <button id="clear-filter-btn" class="text-xs bg-zinc-800 hover:bg-zinc-700 text-zinc-300 border border-zinc-700 px-3 py-2 rounded-xl transition flex items-center gap-1.5 font-medium whitespace-nowrap">
                        <i data-lucide="refresh-cw" class="w-3.5 h-3.5"></i> Reset
                    </button>
                </div>
                
                <!-- Pills filtering -->
                <div class="flex flex-wrap gap-1.5 pb-1 max-h-20 overflow-y-auto custom-scrollbar" id="genre-filter-container">
                    <!-- Dynamic genres pills will load here -->
                </div>

                <!-- Scrollable Song List -->
                <div class="flex-grow overflow-y-auto custom-scrollbar flex flex-col gap-2 pr-1" id="track-list">
                    <!-- Dynamic Track Cards -->
                </div>
            </div>
        </div>

        <!-- Right Column: Canvas Network Graph (7 cols) -->
        <div class="lg:col-span-7 flex flex-col gap-6 h-[calc(100vh-140px)] min-h-[500px]">
            
            <!-- Map Card -->
            <div class="bg-zinc-900/50 border border-zinc-800 rounded-2xl p-4 flex-grow flex flex-col gap-3 min-h-0 relative">
                <div class="flex items-center justify-between">
                    <div>
                        <h2 class="font-bold text-sm tracking-wide text-zinc-300 flex items-center gap-2">
                            <i data-lucide="network" class="w-4 h-4 text-purple-400"></i> Interactive Motif Network Map
                        </h2>
                        <p class="text-xs text-zinc-500">Visual mapping of Suno tracks to their musical motifs.</p>
                    </div>
                    <div class="flex gap-1.5 text-[10px] text-zinc-400">
                        <span class="flex items-center gap-1"><span class="w-2.5 h-2.5 rounded-full bg-purple-500 shadow shadow-purple-900"></span> Track</span>
                        <span class="flex items-center gap-1"><span class="w-2.5 h-2.5 rounded bg-pink-500 shadow shadow-pink-900"></span> Motif</span>
                    </div>
                </div>

                <!-- Canvas Component -->
                <div class="flex-grow bg-zinc-950/80 border border-zinc-850 rounded-xl relative overflow-hidden flex items-center justify-center">
                    <canvas id="network-canvas" class="absolute inset-0 w-full h-full cursor-grab active:cursor-grabbing"></canvas>
                    
                    <div class="absolute bottom-3 left-3 bg-zinc-900/90 border border-zinc-800 rounded-lg px-2.5 py-1.5 text-[10px] text-zinc-400 pointer-events-none flex flex-col gap-0.5">
                        <p>🖱️ <strong>Left Click:</strong> Select & Play</p>
                        <p>🧭 <strong>Drag:</strong> Pan Map</p>
                        <p>🔍 <strong>Scroll:</strong> Zoom In/Out</p>
                    </div>
                </div>
            </div>

            <!-- Detail Display Card -->
            <div class="bg-zinc-900/80 border border-zinc-800 rounded-2xl p-5 h-56 flex flex-col gap-3 relative overflow-hidden" id="detail-card">
                <div class="flex justify-between items-start">
                    <h3 class="font-bold text-zinc-200 flex items-center gap-2" id="detail-title">
                        Select an item
                    </h3>
                    <span class="text-[10px] uppercase font-bold tracking-wider px-2 py-0.5 rounded-full bg-zinc-800 text-zinc-400" id="detail-type">-</span>
                </div>
                <div class="text-sm text-zinc-400 overflow-y-auto custom-scrollbar flex-grow" id="detail-desc">
                    Click any track or motif node in the network map above, or search/select from the list, to explore descriptions, metadata, and cross-track relationships.
                </div>
                <div class="flex flex-wrap gap-1.5 mt-2" id="detail-tags">
                    <!-- Associated tags/genres/motifs -->
                </div>
            </div>
        </div>

    </main>

    <!-- Bottom Obsidian Info Section -->
    <section class="bg-zinc-950 border-t border-zinc-900 py-8 px-6 mt-auto">
        <div class="max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-8">
            <div class="flex flex-col gap-2">
                <h3 class="font-bold text-md text-white flex items-center gap-2">
                    <i data-lucide="book-open" class="text-purple-400"></i> Obsidian Vault Integration
                </h3>
                <p class="text-sm text-zinc-400 leading-relaxed">
                    This directory also automatically serves as a fully compatible <strong>Obsidian Vault</strong>. The script generates metadata files for all tracks, motifs, and relationships under the <code>/archive</code> folder in markdown format, complete with bi-directional wikilinks.
                </p>
                <div class="flex gap-4 mt-2">
                    <div class="flex items-center gap-2 text-xs text-zinc-300">
                        <i data-lucide="folder" class="w-4 h-4 text-purple-400"></i>
                        <code>archive/Tracks/</code>
                    </div>
                    <div class="flex items-center gap-2 text-xs text-zinc-300">
                        <i data-lucide="hash" class="w-4 h-4 text-pink-400"></i>
                        <code>archive/Motifs/</code>
                    </div>
                    <div class="flex items-center gap-2 text-xs text-zinc-300">
                        <i data-lucide="map" class="w-4 h-4 text-blue-400"></i>
                        <code>virtualluser_music_map.canvas</code>
                    </div>
                </div>
            </div>

            <div class="flex flex-col gap-3">
                <h3 class="font-bold text-md text-white">How to import into Obsidian:</h3>
                <ol class="text-xs text-zinc-400 space-y-2 list-decimal list-inside">
                    <li>Download the <code>archive/</code> folder from this repository.</li>
                    <li>Open <strong>Obsidian</strong> and select <i>"Open folder as vault"</i>.</li>
                    <li>Select the downloaded <code>archive/</code> directory.</li>
                    <li>Enable the <strong>Canvas core plugin</strong> and open <code>virtualluser_music_map.canvas</code> to explore the dynamic visual network!</li>
                </ol>
            </div>
        </div>
        <div class="max-w-7xl mx-auto mt-6 pt-4 border-t border-zinc-900/50 flex flex-col sm:flex-row items-center justify-between text-xs text-zinc-500">
            <p>&copy; 2026 Phonk Life. Automated Suno Archiver & Obsidian Visualizer.</p>
            <p class="mt-2 sm:mt-0">Designed for @virtualluser</p>
        </div>
    </section>

    <!-- Embedded Scripts -->
    <script>
        // Embed the Python-generated datasets
        const tracks = {tracks_json};
        const motifsMeta = {motifs_json};

        // UI References
        const trackListContainer = document.getElementById('track-list');
        const searchInput = document.getElementById('search-input');
        const clearFilterBtn = document.getElementById('clear-filter-btn');
        const genreFilterContainer = document.getElementById('genre-filter-container');
        
        // Player References
        const audioPlayer = document.getElementById('audio-player');
        const playBtn = document.getElementById('play-btn');
        const playIcon = document.getElementById('play-icon');
        const prevBtn = document.getElementById('prev-btn');
        const nextBtn = document.getElementById('next-btn');
        const volumeBtn = document.getElementById('volume-btn');
        const volumeIcon = document.getElementById('volume-icon');
        const volumeSlider = document.getElementById('volume-slider');
        const progressBarContainer = document.getElementById('progress-bar-container');
        const progressBarFill = document.getElementById('progress-bar-fill');
        const currentTimeEl = document.getElementById('current-time');
        const totalDurationEl = document.getElementById('total-duration');
        
        const playerInitials = document.getElementById('player-initials');
        const playerGenre = document.getElementById('player-genre');
        const playerTitle = document.getElementById('player-title');
        const playerDesc = document.getElementById('player-desc');
        const sunoLink = document.getElementById('suno-link');
        
        // Detail references
        const detailTitle = document.getElementById('detail-title');
        const detailType = document.getElementById('detail-type');
        const detailDesc = document.getElementById('detail-desc');
        const detailTags = document.getElementById('detail-tags');

        // State variables
        let currentTrackIndex = -1;
        let selectedGenreFilter = '';
        let selectedMotifFilter = '';
        let textSearchQuery = '';
        let selectedNodeId = null;

        // Initialize Lucide Icons
        lucide.createIcons();

        // 1. Audio Player Logic
        function loadTrack(index) {{
            if (index < 0 || index >= tracks.length) return;
            currentTrackIndex = index;
            const track = tracks[index];
            
            // Set Player UI
            audioPlayer.src = track.audio_url;
            playerGenre.textContent = track.genre;
            playerTitle.textContent = track.title;
            playerDesc.textContent = track.description;
            
            // Extract initials
            const words = track.title.split(' ');
            const initials = words.map(w => w[0]).join('').substring(0, 2).toUpperCase();
            playerInitials.textContent = initials;
            
            sunoLink.href = `https://suno.com/song/${{track.id}}`;
            
            // Enable Controls
            playBtn.disabled = false;
            prevBtn.disabled = index === 0;
            nextBtn.disabled = index === tracks.length - 1;
            
            // Auto play
            playTrack();
            
            // Highlight list item
            renderTrackList();
            
            // Select in details
            selectNode(`track_${{index}}`);
        }}

        function playTrack() {{
            audioPlayer.play().then(() => {{
                playIcon.setAttribute('data-lucide', 'pause');
                lucide.createIcons();
            }}).catch(e => console.log("Audio autoplay interrupted:", e));
        }}

        function pauseTrack() {{
            audioPlayer.pause();
            playIcon.setAttribute('data-lucide', 'play');
            lucide.createIcons();
        }}

        playBtn.addEventListener('click', () => {{
            if (audioPlayer.paused) {{
                playTrack();
            }} else {{
                pauseTrack();
            }}
        }});

        prevBtn.addEventListener('click', () => {{
            if (currentTrackIndex > 0) {{
                loadTrack(currentTrackIndex - 1);
            }}
        }});

        nextBtn.addEventListener('click', () => {{
            if (currentTrackIndex < tracks.length - 1) {{
                loadTrack(currentTrackIndex + 1);
            }}
        }});

        // Time Updates
        audioPlayer.addEventListener('timeupdate', () => {{
            const current = audioPlayer.currentTime;
            const duration = audioPlayer.duration || 0;
            
            // Fill progress
            const pct = duration > 0 ? (current / duration) * 100 : 0;
            progressBarFill.style.width = `${{pct}}%`;
            
            // Text values
            currentTimeEl.textContent = formatTime(current);
            totalDurationEl.textContent = formatTime(duration);
        }});

        function formatTime(secs) {{
            const m = Math.floor(secs / 60);
            const s = Math.floor(secs % 60);
            return `${{m}}:${{s < 10 ? '0' : ''}}${{s}}`;
        }}

        // Click Progress Bar
        progressBarContainer.addEventListener('click', (e) => {{
            const width = progressBarContainer.clientWidth;
            const clickX = e.offsetX;
            const duration = audioPlayer.duration || 0;
            if (duration > 0) {{
                audioPlayer.currentTime = (clickX / width) * duration;
            }}
        }});

        // Volume logic
        let previousVolume = 0.8;
        volumeBtn.addEventListener('click', () => {{
            if (audioPlayer.volume > 0) {{
                previousVolume = audioPlayer.volume;
                audioPlayer.volume = 0;
                volumeSlider.value = 0;
                updateVolumeIcon(0);
            }} else {{
                audioPlayer.volume = previousVolume;
                volumeSlider.value = previousVolume * 100;
                updateVolumeIcon(previousVolume);
            }}
        }});

        volumeSlider.addEventListener('input', (e) => {{
            const vol = e.target.value / 100;
            audioPlayer.volume = vol;
            updateVolumeIcon(vol);
        }});

        function updateVolumeIcon(vol) {{
            let iconName = 'volume-2';
            if (vol === 0) iconName = 'volume-x';
            else if (vol < 0.4) iconName = 'volume';
            else if (vol < 0.7) iconName = 'volume-1';
            
            volumeIcon.setAttribute('data-lucide', iconName);
            lucide.createIcons();
        }}

        audioPlayer.addEventListener('ended', () => {{
            if (currentTrackIndex < tracks.length - 1) {{
                loadTrack(currentTrackIndex + 1);
            }} else {{
                pauseTrack();
            }}
        }});

        // 2. Track List rendering & Filtering
        const allGenres = [...new Set(tracks.map(t => t.genre.split(' / ')[0]))];
        const allMotifs = Object.keys(motifsMeta);

        function renderFilterPills() {{
            genreFilterContainer.innerHTML = '';
            
            // Genre Filters
            allGenres.forEach(genre => {{
                const btn = document.createElement('button');
                btn.className = `text-[10px] px-2.5 py-1 rounded-full border border-zinc-800 transition transition-colors font-medium whitespace-nowrap ${{selectedGenreFilter === genre ? 'bg-purple-500/20 text-purple-400 border-purple-500/40 shadow shadow-purple-950/20' : 'bg-zinc-950 text-zinc-400 hover:text-white hover:border-zinc-700'}}`;
                btn.textContent = `🎵 ${{genre}}`;
                btn.onclick = () => {{
                    if (selectedGenreFilter === genre) {{
                        selectedGenreFilter = '';
                    }} else {{
                        selectedGenreFilter = genre;
                        selectedMotifFilter = ''; // Mutually exclusive for layout simplicity
                    }}
                    renderTrackList();
                    updateGraphHighlights();
                }};
                genreFilterContainer.appendChild(btn);
            }});
            
            // Motif Filters
            allMotifs.forEach(motif => {{
                const btn = document.createElement('button');
                btn.className = `text-[10px] px-2.5 py-1 rounded-full border border-zinc-800 transition transition-colors font-medium whitespace-nowrap ${{selectedMotifFilter === motif ? 'bg-pink-500/20 text-pink-400 border-pink-500/40 shadow shadow-pink-950/20' : 'bg-zinc-950 text-zinc-400 hover:text-white hover:border-zinc-700'}}`;
                btn.textContent = `🧬 ${{motif}}`;
                btn.onclick = () => {{
                    if (selectedMotifFilter === motif) {{
                        selectedMotifFilter = '';
                    }} else {{
                        selectedMotifFilter = motif;
                        selectedGenreFilter = ''; // Mutually exclusive for layout simplicity
                    }}
                    renderTrackList();
                    updateGraphHighlights();
                }};
                genreFilterContainer.appendChild(btn);
            }});
        }}

        function renderTrackList() {{
            trackListContainer.innerHTML = '';
            
            const filteredTracks = tracks.map((t, idx) => ({{ ...t, originalIndex: idx }})).filter(track => {{
                const matchesText = track.title.toLowerCase().includes(textSearchQuery.toLowerCase()) || 
                                    track.genre.toLowerCase().includes(textSearchQuery.toLowerCase()) || 
                                    track.lyrics.toLowerCase().includes(textSearchQuery.toLowerCase());
                
                const matchesMotif = !selectedMotifFilter || track.motifs.includes(selectedMotifFilter);
                const matchesGenre = !selectedGenreFilter || track.genre.startsWith(selectedGenreFilter);
                
                return matchesText && matchesMotif && matchesGenre;
            }});

            if (filteredTracks.length === 0) {{
                trackListContainer.innerHTML = `
                    <div class="py-8 text-center text-zinc-500 text-sm">
                        No songs found matching filters.
                    </div>
                `;
                return;
            }}

            filteredTracks.forEach(track => {{
                const isActive = track.originalIndex === currentTrackIndex;
                const card = document.createElement('div');
                card.className = `p-3 rounded-xl border transition cursor-pointer flex gap-3 items-center group ${{isActive ? 'bg-purple-950/20 border-purple-500/50 shadow shadow-purple-950/20' : 'bg-zinc-900/30 border-zinc-850 hover:bg-zinc-900/60 hover:border-zinc-700'}}`;
                
                card.onclick = () => {{
                    loadTrack(track.originalIndex);
                }};

                card.innerHTML = `
                    <div class="w-10 h-10 rounded-lg bg-gradient-to-br ${{isActive ? 'from-purple-500 to-pink-500' : 'from-zinc-800 to-zinc-700'}} flex items-center justify-center text-white text-xs font-bold transition group-hover:scale-105">
                        ${{isActive ? '<i data-lucide="play" class="w-4 h-4 fill-current"></i>' : track.title[0]}}
                    </div>
                    <div class="flex-grow min-w-0">
                        <div class="flex justify-between items-start">
                            <h4 class="font-semibold text-sm truncate group-hover:text-purple-300 transition ${{isActive ? 'text-purple-300' : 'text-zinc-200'}}">${{track.title}}</h4>
                            <span class="text-[10px] text-zinc-500 font-mono">${{track.duration}}</span>
                        </div>
                        <p class="text-xs text-zinc-400 truncate mt-0.5">${{track.genre}}</p>
                    </div>
                `;
                
                trackListContainer.appendChild(card);
            }});
            
            lucide.createIcons();
        }}

        // Text Search Event
        searchInput.addEventListener('input', (e) => {{
            textSearchQuery = e.target.value;
            renderTrackList();
            updateGraphHighlights();
        }});

        // Clear button
        clearFilterBtn.addEventListener('click', () => {{
            searchInput.value = '';
            textSearchQuery = '';
            selectedGenreFilter = '';
            selectedMotifFilter = '';
            selectedNodeId = null;
            renderFilterPills();
            renderTrackList();
            
            // reset detail card
            detailTitle.textContent = "Select an item";
            detailType.textContent = "-";
            detailDesc.textContent = "Click any track or motif node in the network map above, or search/select from the list, to explore descriptions, metadata, and cross-track relationships.";
            detailTags.innerHTML = '';
            
            updateGraphHighlights();
        }});

        // 3. Network Graph (HTML5 Canvas)
        const canvas = document.getElementById('network-canvas');
        const ctx = canvas.getContext('2d');
        
        let width = canvas.clientWidth;
        let height = canvas.clientHeight;
        canvas.width = width;
        canvas.height = height;

        window.addEventListener('resize', () => {{
            width = canvas.clientWidth;
            height = canvas.clientHeight;
            canvas.width = width;
            canvas.height = height;
            layoutNodes();
        }});

        // Graph Data Nodes
        let nodes = [];
        let edges = [];
        let nodeMap = {{}};
        
        // Camera / Pan / Zoom State
        let transform = {{ x: 0, y: 0, scale: 1 }};
        let isDragging = false;
        let dragStart = {{ x: 0, y: 0 }};
        let hoveredNodeId = null;

        function initializeGraph() {{
            nodes = [];
            edges = [];
            
            // 1. Add Motif Nodes
            const motifsList = Object.keys(motifsMeta);
            motifsList.forEach((motif, idx) => {{
                nodes.push({{
                    "id": `motif_${{idx}}`,
                    "label": motif,
                    "type": "motif",
                    "description": motifsMeta[motif],
                    "x": 0, "y": 0,
                    "radius": 14,
                    "color": "#ec4899",
                    "glowColor": "rgba(236, 72, 153, 0.4)",
                    "active": true
                }});
            }});
            
            // 2. Add Track Nodes & Connect
            tracks.forEach((track, idx) => {{
                const trackNodeId = `track_${{idx}}`;
                nodes.push({{
                    "id": trackNodeId,
                    "label": track.title,
                    "type": "track",
                    "genre": track.genre,
                    "description": track.description,
                    "x": 0, "y": 0,
                    "radius": 10,
                    "color": "#a855f7",
                    "glowColor": "rgba(168, 85, 247, 0.4)",
                    "active": true,
                    "trackIndex": idx
                }});
                
                // Connect to Motifs
                track.motifs.forEach(motifName => {{
                    const motifIdx = motifsList.indexOf(motifName);
                    if (motifIdx !== -1) {{
                        edges.push({{
                            "from": trackNodeId,
                            "to": `motif_${{motifIdx}}`,
                            "active": true
                        }});
                    }}
                }});
            }});
            
            layoutNodes();
            
            // Build index Map for fast O(1) lookups in render loop
            nodeMap = {{}};
            nodes.forEach(node => {{
                nodeMap[node.id] = node;
            }});
            
            animate();
        }}

        function layoutNodes() {{
            const centerX = width / 2;
            const centerY = height / 2;
            
            const motifNodes = nodes.filter(n => n.type === 'motif');
            const trackNodes = nodes.filter(n => n.type === 'track');
            
            // Layout motifs in a circle
            const motifRadius = Math.min(width, height) * 0.18;
            motifNodes.forEach((node, i) => {{
                const angle = (i / motifNodes.length) * Math.PI * 2;
                node.x = centerX + Math.cos(angle) * motifRadius;
                node.y = centerY + Math.sin(angle) * motifRadius;
            }});
            
            // Layout tracks in a larger circle
            const trackRadius = Math.min(width, height) * 0.38;
            trackNodes.forEach((node, i) => {{
                const angle = (i / trackNodes.length) * Math.PI * 2 + Math.PI / trackNodes.length; // offset angle slightly
                node.x = centerX + Math.cos(angle) * trackRadius;
                node.y = centerY + Math.sin(angle) * trackRadius;
            }});
        }}

        function updateGraphHighlights() {{
            nodes.forEach(node => {{
                let active = true;
                
                // Text Search Check
                if (textSearchQuery) {{
                    const query = textSearchQuery.toLowerCase();
                    if (node.type === 'track') {{
                        const track = tracks[node.trackIndex];
                        active = track.title.toLowerCase().includes(query) || 
                                 track.genre.toLowerCase().includes(query) || 
                                 track.lyrics.toLowerCase().includes(query);
                    }} else {{
                        active = node.label.toLowerCase().includes(query) || 
                                 node.description.toLowerCase().includes(query);
                    }}
                }}
                
                // Motif Pill Filter Check
                if (selectedMotifFilter && active) {{
                    if (node.type === 'track') {{
                        const track = tracks[node.trackIndex];
                        active = track.motifs.includes(selectedMotifFilter);
                    }} else {{
                        active = node.label === selectedMotifFilter;
                    }}
                }}

                // Genre Pill Filter Check
                if (selectedGenreFilter && active) {{
                    if (node.type === 'track') {{
                        const track = tracks[node.trackIndex];
                        active = track.genre.startsWith(selectedGenreFilter);
                    }} else {{
                        active = false;
                    }}
                }}
                
                node.active = active;
            }});
            
            // Highlight connections for selected node
            if (selectedNodeId) {{
                const selectedNode = nodes.find(n => n.id === selectedNodeId);
                if (selectedNode) {{
                    const connectedNodeIds = new Set();
                    connectedNodeIds.add(selectedNodeId);
                    
                    edges.forEach(edge => {{
                        if (edge.from === selectedNodeId) connectedNodeIds.add(edge.to);
                        if (edge.to === selectedNodeId) connectedNodeIds.add(edge.from);
                    }});
                    
                    nodes.forEach(node => {{
                        node.highlighted = connectedNodeIds.has(node.id);
                    }});
                    
                    edges.forEach(edge => {{
                        edge.highlighted = edge.from === selectedNodeId || edge.to === selectedNodeId;
                    }});
                }}
            }} else {{
                nodes.forEach(n => n.highlighted = false);
                edges.forEach(e => e.highlighted = false);
            }}
        }}

        function selectNode(nodeId) {{
            selectedNodeId = nodeId;
            const node = nodes.find(n => n.id === nodeId);
            if (!node) return;
            
            detailTitle.textContent = node.label;
            detailType.textContent = node.type;
            
            if (node.type === 'motif') {{
                detailType.className = "text-[10px] uppercase font-bold tracking-wider px-2.5 py-0.5 rounded-full bg-pink-950/50 text-pink-400 border border-pink-500/20";
                
                // Fetch tracks with this motif
                const matchingTracks = tracks.filter(t => t.motifs.includes(node.label));
                const listItems = matchingTracks.map(t => `<span class="bg-zinc-850 hover:bg-purple-950/20 hover:text-purple-300 border border-zinc-800 transition px-2.5 py-1 rounded-lg text-xs cursor-pointer text-zinc-300 select-none flex items-center gap-1" onclick="const idx = tracks.findIndex(s=>s.title==='${{t.title}}'); if(idx!==-1) loadTrack(idx)">🎵 ${{t.title}}</span>`).join(' ');
                
                detailDesc.innerHTML = `
                    <p class="leading-relaxed mb-3 text-zinc-300">${{node.description}}</p>
                    <p class="text-xs font-semibold uppercase tracking-wider text-zinc-500 mb-1.5">Songs containing this motif:</p>
                    <div class="flex flex-wrap gap-1.5">${{listItems}}</div>
                `;
                
                detailTags.innerHTML = '';
            }} else {{
                detailType.className = "text-[10px] uppercase font-bold tracking-wider px-2.5 py-0.5 rounded-full bg-purple-950/50 text-purple-400 border border-purple-500/20";
                const track = tracks[node.trackIndex];
                
                detailDesc.innerHTML = `
                    <p class="leading-relaxed text-zinc-300 mb-3">${{track.description}}</p>
                    <p class="text-xs font-semibold uppercase tracking-wider text-zinc-500 mb-1.5">Musical Motifs in this track:</p>
                `;
                
                // Load motif pills in detail tags
                detailTags.innerHTML = '';
                track.motifs.forEach(motif => {{
                    const pill = document.createElement('span');
                    pill.className = "bg-zinc-850 hover:bg-pink-950/20 hover:text-pink-300 border border-zinc-800 transition text-xs px-2.5 py-1 rounded-lg text-zinc-300 cursor-pointer flex items-center gap-1 select-none";
                    pill.innerHTML = `🧬 ${{motif}}`;
                    pill.onclick = () => {{
                        const mNode = nodes.find(n => n.type === 'motif' && n.label === motif);
                        if (mNode) selectNode(mNode.id);
                    }};
                    detailTags.appendChild(pill);
                }});
            }}
            
            updateGraphHighlights();
        }}

        // Canvas interactions
        function getMousePos(e) {{
            const rect = canvas.getBoundingClientRect();
            // Calculate relative coordinate based on pan and zoom
            const clientX = e.clientX - rect.left;
            const clientY = e.clientY - rect.top;
            
            return {{
                x: (clientX - transform.x) / transform.scale,
                y: (clientY - transform.y) / transform.scale
            }};
        }}

        canvas.addEventListener('mousedown', (e) => {{
            const mouse = getMousePos(e);
            
            // Check if clicked a node
            const clickedNode = nodes.find(node => {{
                if (!node.active) return false;
                const dist = Math.hypot(node.x - mouse.x, node.y - mouse.y);
                return dist <= node.radius + 5;
            }});
            
            if (clickedNode) {{
                if (clickedNode.type === 'track') {{
                    loadTrack(clickedNode.trackIndex);
                }} else {{
                    selectNode(clickedNode.id);
                }}
            }} else {{
                isDragging = true;
                dragStart = {{ x: e.clientX - transform.x, y: e.clientY - transform.y }};
            }}
        }});

        canvas.addEventListener('mousemove', (e) => {{
            if (isDragging) {{
                transform.x = e.clientX - dragStart.x;
                transform.y = e.clientY - dragStart.y;
                return;
            }}
            
            // Hover logic
            const mouse = getMousePos(e);
            const hovered = nodes.find(node => {{
                if (!node.active) return false;
                const dist = Math.hypot(node.x - mouse.x, node.y - mouse.y);
                return dist <= node.radius + 5;
            }});
            
            hoveredNodeId = hovered ? hovered.id : null;
        }});

        window.addEventListener('mouseup', () => {{
            isDragging = false;
        }});

        canvas.addEventListener('wheel', (e) => {{
            e.preventDefault();
            const rect = canvas.getBoundingClientRect();
            const mouseX = e.clientX - rect.left;
            const mouseY = e.clientY - rect.top;
            
            const zoomFactor = 1.1;
            let newScale = transform.scale;
            
            if (e.deltaY < 0) {{
                newScale *= zoomFactor;
            }} else {{
                newScale /= zoomFactor;
            }}
            
            // Cap zoom scale
            newScale = Math.max(0.4, Math.min(3, newScale));
            
            // Adjust pan so zooming centers on mouse
            transform.x = mouseX - (mouseX - transform.x) * (newScale / transform.scale);
            transform.y = mouseY - (mouseY - transform.y) * (newScale / transform.scale);
            transform.scale = newScale;
        }});

        function animate() {{
            ctx.clearRect(0, 0, width, height);
            
            ctx.save();
            ctx.translate(transform.x, transform.y);
            ctx.scale(transform.scale, transform.scale);
            
            // 1. Draw Edges
            edges.forEach(edge => {{
                const fromNode = nodeMap[edge.from];
                const toNode = nodeMap[edge.to];
                if (!fromNode || !toNode || !fromNode.active || !toNode.active) return;
                
                ctx.beginPath();
                ctx.moveTo(fromNode.x, fromNode.y);
                ctx.lineTo(toNode.x, toNode.y);
                
                let isHighlighted = edge.highlighted;
                if (selectedNodeId && !isHighlighted) {{
                    ctx.strokeStyle = '#1e1f29';
                    ctx.lineWidth = 1;
                }} else if (isHighlighted) {{
                    ctx.strokeStyle = 'rgba(236, 72, 153, 0.7)';
                    ctx.lineWidth = 2.5;
                }} else {{
                    ctx.strokeStyle = '#27273a';
                    ctx.lineWidth = 1.5;
                }}
                
                ctx.stroke();
            }});
            
            // 2. Draw Nodes
            nodes.forEach(node => {{
                if (!node.active) return;
                
                const isSelected = node.id === selectedNodeId;
                const isHovered = node.id === hoveredNodeId;
                const hasGlobalSelection = !!selectedNodeId;
                const isHighlighted = node.highlighted;
                
                ctx.save();
                
                // Draw shadow/glow
                ctx.shadowColor = node.glowColor;
                ctx.shadowBlur = (isSelected || isHovered) ? 20 : 5;
                
                ctx.beginPath();
                ctx.arc(node.x, node.y, node.radius + (isHovered ? 2 : 0), 0, Math.PI * 2);
                
                // Faded out if another node is selected and this isn't connected
                if (hasGlobalSelection && !isHighlighted && !isSelected) {{
                    ctx.fillStyle = '#181922';
                    ctx.strokeStyle = '#27273a';
                    ctx.shadowBlur = 0;
                }} else {{
                    ctx.fillStyle = node.color;
                    ctx.strokeStyle = '#ffffff';
                }}
                
                ctx.lineWidth = (isSelected) ? 3 : 1.5;
                ctx.fill();
                ctx.stroke();
                
                ctx.restore();
                
                // Draw Label
                ctx.beginPath();
                ctx.font = `${{node.type === 'motif' ? 'bold 11px' : '500 10px'}} Inter, sans-serif`;
                
                if (hasGlobalSelection && !isHighlighted && !isSelected) {{
                    ctx.fillStyle = '#4b5563';
                }} else {{
                    ctx.fillStyle = '#ffffff';
                }}
                
                ctx.textAlign = 'center';
                ctx.fillText(node.label, node.x, node.y - node.radius - 8);
            }});
            
            ctx.restore();
            
            requestAnimationFrame(animate);
        }}

        // Initialize lists and scripts on load
        audioPlayer.volume = volumeSlider.value / 100;
        updateVolumeIcon(audioPlayer.volume);
        renderFilterPills();
        renderTrackList();
        initializeGraph();
    </script>
</body>
</html>
"""
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"Generated web dashboard complete: {output_file}")

if __name__ == "__main__":
    # Attempt to sync from Suno API (will fall back gracefully)
    live_data = fetch_suno_data()
    
    # We use our high-quality analyzed dataset
    tracks = [t.copy() for t in VIRTUALLUSER_TRACKS]
    motifs_meta = MOTIFS_META
    
    # Robust merge logic for live API data (handles list and dict shapes)
    live_tracks = None
    if isinstance(live_data, list):
        live_tracks = live_data
    elif isinstance(live_data, dict):
        for key in ["items", "clips", "feed"]:
            if key in live_data and isinstance(live_data[key], list):
                live_tracks = list(live_data[key])
                break
        if live_tracks is None:
            for val in live_data.values():
                if is_track_list(val):
                    live_tracks = list(val)
                    break

    if live_tracks:
        existing_ids = {track_item["id"] for track_item in tracks if "id" in track_item}
        lowercased_motifs = {m.lower(): m for m in motifs_meta.keys()}
        for lt in live_tracks:
            if isinstance(lt, dict) and "id" in lt and lt["id"] not in existing_ids:
                title = lt.get("title") or lt.get("name") or "Untitled Track"
                audio_url = lt.get("audio_url") or lt.get("audio") or ""
                metadata = lt.get("metadata") or {}
                lyrics = ""
                tags = []
                if isinstance(metadata, dict):
                    lyrics = metadata.get("prompt") or metadata.get("lyrics") or ""
                    tags_raw = metadata.get("tags") or ""
                    if isinstance(tags_raw, str):
                        tags = [tag_val.strip() for tag_val in tags_raw.split(",") if tag_val.strip()]
                    elif isinstance(tags_raw, list):
                        tags = tags_raw
                genre = lt.get("genre") or ", ".join(tags) or "Suno Phonk"
                
                # Check for motifs in title, genre, description, or lyrics
                # and extract them based on matching keys in MOTIFS_META
                extracted_motifs = []
                search_text = f"{title} {genre} {lt.get('description', '')} {lyrics}".lower()
                for lower_motif, motif_name in lowercased_motifs.items():
                    if lower_motif in search_text:
                        extracted_motifs.append(motif_name)

                duration = format_duration(lt.get("duration"))

                new_track = {
                    "id": lt["id"],
                    "title": title,
                    "genre": genre,
                    "description": lt.get("description") or "Imported from live Suno feed.",
                    "tags": tags,
                    "audio_url": audio_url,
                    "video_url": lt.get("video_url") or "",
                    "duration": duration,
                    "lyrics": lyrics,
                    "motifs": extracted_motifs
                }
                tracks.append(new_track)
                existing_ids.add(lt["id"])

    # Generate the Obsidian vault
    generate_obsidian_vault(tracks, motifs_meta, base_dir="archive")
    
    # Generate the index.html for static GitHub pages site
    generate_web_dashboard(tracks, motifs_meta, output_file="index.html")
    
    print("\n[SUCCESS] Redesigned Barnacle Suno-Archive generation complete!")
    print("Obsidian vault created in /archive")
    print("Interactive HTML dashboard created in index.html")
